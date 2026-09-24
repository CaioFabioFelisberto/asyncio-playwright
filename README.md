# Asyncio Playwright

Projeto em Python para automatizar a navegação em um portal dinâmico usando `asyncio` e `Playwright`. O script acessa a página de login, faz autenticação com credenciais fixas, coleta as citações disponíveis após o login e salva os dados em um arquivo JSON.

## Objetivo

O projeto demonstra um fluxo básico de automação web com:

- `asyncio` para execução assíncrona
- `Playwright` para automação do navegador
- coleta de elementos da página
- exportação dos resultados para `JSON`
- captura de screenshot da tela após login

## Estrutura do projeto

```text
asyncio-playwright/
├── .venv/                  # ambiente virtual Python
├── data/
│   └── dados_dinamicos.json  # arquivo gerado com as citações
├── images/
│   └── pos_login.png         # screenshot gerado após login
├── main.py                 # script principal
├── requirements.txt        # dependências do projeto
├── README.md               # documentação do projeto
└── .gitignore              # .gitignore
```

## Funcionalidade principal

Ao executar o script:

1. abre um navegador Chromium em modo headless
2. acessa o site de login em `https://quotes.toscrape.com/login`
3. preenche usuário e senha
4. clica em "Login"
5. aguarda a renderização das citações
6. captura as frases e autores
7. salva os dados em `data/dados_dinamicos.json`
8. grava uma imagem em `images/pos_login.png`

## Requisitos

- Python 3.10 ou superior
- Navegador Chromium/Playwright suportado
- Acesso à internet para carregar o site alvo

## Instalação

No diretório raiz do projeto, execute:

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale os binaries do Playwright:

```bash
python -m playwright install
```

## Execução

```bash
python main.py
```

## Saída esperada

Após a execução, o projeto gera:

- `data/dados_dinamicos.json`
- `images/pos_login.png`

Exemplo do conteúdo do arquivo JSON:

```json
[
  {
    "autor": "Albert Einstein",
    "frase": "The world as we have created it is a process of our thinking."
  }
]
```

## Observações

- O login no exemplo usa credenciais fixas para fins de demonstração.
- O script foi desenvolvido para fins de estudo e automação de testes web.
- Caso o site altere a estrutura HTML, pode ser necessário adaptar os seletores (`selectors`) usados em `main.py`.

## Dependências principais

- `playwright==1.63.0`
- `greenlet==3.5.6`
- `pyee==13.0.1`

## Licença

Este projeto foi criado para fins educacionais e de automação prática. Ajuste a licença conforme a necessidade do seu uso real.
