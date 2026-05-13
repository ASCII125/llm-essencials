# LLM Essentials

Este projeto demonstra conceitos básicos de integração de Large Language Models (LLMs) usando Python e FastAPI, focado em uma arquitetura modular e extensível.

## 🚀 Como Inicializar

Este projeto utiliza o [uv](https://github.com/astral-sh/uv) para gerenciamento de dependências e ambiente virtual.

### 1. Configuração do Ambiente

Primeiro, clone o repositório e configure as variáveis de ambiente:

```bash
# Copie o arquivo de exemplo para o .env
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da API do Groq:
- `GROQ_KEY`: Sua chave de API do Groq.
- `API_PORT`: (Opcional) A porta em que a API será executada (padrão: 8000).

### 2. Instalação e Execução

Com o `uv` instalado, você pode sincronizar as dependências e rodar o projeto com um único comando:

```bash
# Sincroniza dependências e executa a aplicação
uv run src/main.py
```

A API estará disponível em `http://localhost:8000` (ou na porta definida no `.env`). Você pode acessar o frontend simples na raiz `/` ou a documentação Swagger em `/docs`.

## 📂 Estrutura de Módulos

O projeto está organizado de forma a separar as responsabilidades:

- **`src/api/`**: Contém a definição da aplicação FastAPI.
    - `app.py`: Configuração principal do servidor, middlewares e roteamento.
    - `routers.py`: Definição dos endpoints da API (ex: `/llm/chat`).
- **`src/integrations/llms/`**: Camada de integração com modelos de linguagem.
    - `interfaces.py`: Define o contrato (`IAgent`) que qualquer adaptador de LLM deve seguir.
    - `adapters/`: Implementações concretas das interfaces (ex: `GroqAgent`).
    - `schemas.py`: Modelos de dados (Pydantic) usados na comunicação com as LLMs.
- **`src/setup.py`**: Centraliza a carga de configurações do arquivo `.env` e a instanciação de serviços (Injeção de Dependência).
- **`src/main.py`**: Ponto de entrada da aplicação que inicia o servidor Uvicorn.
- **`resources/`**: Arquivos estáticos e templates para a interface frontend da aplicação.
    - `static/`: Arquivos CSS e JavaScript.
    - `templates/`: Templates HTML (index.html).

## 🛠 Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido.
- **Groq SDK**: Integração com a infraestrutura de inferência rápida do Groq.
- **uv**: Gerenciador de pacotes e ambientes Python ultrarrápido.
- **Python Dotenv**: Gerenciamento de variáveis de ambiente.
