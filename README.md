# Projeto Backend para Recebimento e Encaminhamento de Arquivos

Este projeto backend tem como objetivo receber arquivos do tipo documento (ex: `.doc`, `.docx`, `.pdf`) via API e encaminhá-los para processamento ou armazenamento.

## Funcionalidades

- Upload de arquivos via endpoint HTTP.
- Validação do tipo e tamanho dos arquivos recebidos.
- Encaminhamento dos arquivos para serviços internos ou externos.
- Respostas claras sobre o status do upload.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Fastapi](https://fastapi.tiangolo.com/pt/tutorial/first-steps/)
- [Werkzeug](https://werkzeug.palletsprojects.com/) para manipulação de uploads
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) para ambiente de desenvolvimento

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repo.git
    cd seu-repo
    ```
2. Inicie o ambiente de desenvolvimento com Docker Compose:
    ```bash
    docker-compose up --build
    ```

## Uso

Envie um arquivo para o endpoint `/upload` usando ferramentas como Postman ou `curl`:

```bash
curl -F "file=@/caminho/para/seuarquivo.docx" http://localhost:5000/upload
```

## Estrutura de Pastas

```
.
├── src/
│   ├── routes/
│   ├── controllers/
│   └── ...
├── uploads/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está sob a licença MIT.
