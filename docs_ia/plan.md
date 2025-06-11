# Estratégia em Alto Nível: Recebimento de Arquivos `.doc` e Cadastro em Fila MQ

## 1. Objetivo
Desenvolver um backend capaz de receber arquivos `.doc` via API e cadastrar tarefas de processamento em uma fila de mensagens (Message Queue - MQ), desacoplando o recebimento do processamento.

## 2. Componentes Principais

- **API de Upload**: Endpoint FastAPI para upload de arquivos `.doc`.
- **Validação Inicial**: Checagem do tipo e integridade do arquivo recebido.
- **Cadastro em Fila MQ**: Após validação, os metadados do arquivo (e/ou o próprio arquivo, conforme estratégia) são enviados para uma fila MQ (ex: RabbitMQ, Redis, SQS).
- **Worker de Processamento**: Serviço separado que consome mensagens da fila e executa o processamento dos arquivos.

## 3. Fluxo de Alto Nível

1. **Cliente faz upload** de um arquivo `.doc` via endpoint FastAPI.
2. **API valida** o arquivo e gera um identificador único.
3. **API envia mensagem** para a fila MQ com informações necessárias (ex: caminho do arquivo, ID, status inicial).
4. **Worker(s)** monitoram a fila e processam os arquivos conforme disponibilidade.
5. **Status** do processamento pode ser consultado via API.

## 4. Benefícios da Arquitetura

- **Escalabilidade**: Possibilidade de múltiplos workers processando arquivos em paralelo.
- **Resiliência**: Fila MQ garante que tarefas não sejam perdidas.
- **Desacoplamento**: Upload e processamento são independentes, melhorando performance e manutenção.

## 5. Próximos Passos

1. Definir tecnologia da fila MQ (RabbitMQ, Redis, etc).
2. Implementar endpoint de upload e integração com a fila.
3. Criar worker para consumir e processar arquivos.
4. Implementar consulta de status.
5. Adicionar testes e documentação.

