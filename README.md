# Taking Backend

Backend para plataforma de busca híbrida com RAG (Retrieval-Augmented Generation), utilizando Python, FastAPI e Qdrant.

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Executar Localmente](#como-executar-localmente)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints Principais](#endpoints-principais)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Sobre o Projeto

Este backend implementa uma API para busca híbrida, combinando busca semântica (embeddings), busca esparsa (BM25) e reranking (ColBERT), integrando com Qdrant para armazenamento vetorial e OpenAI para geração de respostas contextuais.

---

## Requisitos

- Python 3.10+
- [Qdrant](https://qdrant.tech/) (local ou cloud)
- [uv](https://github.com/astral-sh/uv) (opcional, para instalação rápida)
- Docker (opcional, para rodar Qdrant localmente)

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/taking.git
cd taking/backend
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou, usando [uv](https://github.com/astral-sh/uv):

```bash
uv venv .venv
uv pip install -r requirements.txt
```

---

## Configuração

Copie o arquivo de exemplo de variáveis de ambiente e ajuste conforme necessário:

```bash
cp .env.example .env
```

Edite o arquivo `.env` para configurar URLs do Qdrant, chaves de API, etc.

---

## Como Executar Localmente

1. **Certifique-se que o Qdrant está rodando**  
   Você pode rodar o Qdrant localmente com Docker:

   ```bash
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
   ```

2. **Inicie a API**  
   No diretório `backend`:

   ```bash
   uvicorn app.main:app --reload
   ```

   A API estará disponível em [http://localhost:8000](http://localhost:8000).

---

## Testes

Execute os testes automatizados com:

```bash
pytest
```

---

## Estrutura do Projeto

```
backend/
├── app/
│   ├── main.py
│   ├── config/
│   ├── models/
│   ├── routers/
│   └── services/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

---

## Endpoints Principais

- `GET /` — Mensagem de boas-vindas
- `GET /health` — Health check da API
- `POST /search` — Busca híbrida (Qdrant)
- `POST /openai` — Geração de resposta contextualizada (OpenAI)
- `POST /openai/stream` — Streaming de resposta (OpenAI)

A documentação interativa está disponível em `/docs` (Swagger) e `/redoc`.

---

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.

---

## Licença

MIT
