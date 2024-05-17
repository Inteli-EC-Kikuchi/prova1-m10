# prova1-m10

Solução proposta para o exercício prático da prova 1 do módulo 10
Aluno: Filipi Enzo Siqueira Kikuchi

Para rodar o projeto, basta executar os seguintes comandos:

```bash
git clone https://github.com/Inteli-EC-Kikuchi/prova1-m10.git
```

```bash
docker build -t <nome-da-imagem> .
```

```bash
docker run --name <nome-do-container> -p 8000:8000 <nome-da-imagem>
```

## API

A api possui 4 endpoints:

- GET /pedidos: Retorna todos os pedidos em formato JSON
- GET /pedidos/{id}: Retorna um pedido específico em formato JSON
- POST /novo: Cria um novo pedido
- PUT /pedidos/{id}: Atualiza um pedido específico
- DELETE /pedidos/{id}: Deleta um pedido específico


Vídeo de demonstração: https://youtu.be/L-h0XlU_CzU