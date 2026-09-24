import asyncio
import json
from playwright.async_api import async_playwright


async def executar_bot():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print("Acessando o portal dinâmico...")
        await page.goto("https://quotes.toscrape.com/login")

        print("Preenchendo credenciais...")
        await page.fill('input[id="username"]', 'usuario_teste')
        await page.fill('input[id="password"]', 'senha123')

        print("Clicando em Login...")
        await page.click('input[type="submit"]')

        await page.wait_for_selector("div.quote")

        print("Tirando um print da tela pós-login...")
        await page.screenshot(path="images/pos_login.png")

        quotes_elementos = await page.query_selector_all("div.quote")
        dados = []

        for quote in quotes_elementos:
            texto_el = await quote.query_selector("span.text")
            autor_el = await quote.query_selector("small.author")

            texto = await texto_el.inner_text() if texto_el else ""
            autor = await autor_el.inner_text() if autor_el else ""

            dados.append({"autor": autor, "frase": texto})

        with open("data/dados_dinamicos.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print(
            f"Sucesso! {len(dados)} citações capturadas e salvas em 'data/dados_dinamicos.json'."
        )
        print("Screenshot salva em 'images/pos_login.png'.")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(executar_bot())