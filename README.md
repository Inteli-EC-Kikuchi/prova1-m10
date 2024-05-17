# prova1-m10

Solução proposta para o exercício prático da prova 1 do módulo 10 <br/>
**Aluno: Filipi Enzo Siqueira Kikuchi**

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

Exemplo de retorno:
```json
{
    "pedidos": [
        {
            "id": 1,
            "user_name": "Satoru Gojo",
            "user_email": "Hollow.Purple@SixEyes.com",
            "description": "Between Earth and Heaven, I alone am the honored one",
        },
    ]
}
```

- GET /pedidos/{id}: Retorna um pedido específico em formato JSON

Exemplo de retorno:
```json
{
    "id": 1,
    "user_name": "Satoru Gojo",
    "user_email": "Hollow.Purple@SixEyes.com"
    "description": "Between Earth and Heaven, I alone am the honored one",
}
```

- POST /novo: Cria um novo pedido

Exemplo de requisição:
```json
{
	"user_name": "Satoru Gojo",
	"user_email": "Hollow.Purple@SixEyes.com",
	"description": "Between Earth and Heaven, I alone am the honored one"
}
```

A resposta será o pedido criado, com um id gerado automaticamente.
```json
{
	"message": "Order created successfully",
	"order": {
		"user_name": "Satoru Gojo",
		"user_email": "Hollow.Purple@SixEyes.com",
		"id": 1,
		"description": "Between Earth and Heaven, I alone am the honored one"
	}
}
```

Caso algum campo esteja faltando, a resposta será do tipo:
```json
{
	"detail": [
		{
			"type": "missing",
			"loc": [
				"body",
				"description"
			],
			"msg": "Field required",
			"input": {
				"user_name": "Satoru Gojo",
				"user_email": "Hollow.Purple@SixEyes.com"
			}
		}
	]
}
```

- PUT /pedidos/{id}: Atualiza um pedido específico

Exemplo de requisição:
```json
{
	"user_name": "Suguru Getou",
	"user_email": "Curse.Control@Tatsumaki.com",
	"description": "Are you the Strongest Because you are Satoru Gojo, or are you Satoru Gojo because you are the strongest?"
}
```

A resposta será o pedido atualizado, caso o pedido exista.
```json
{
	"message": "Order 1 updated successfully"
}
```

Caso o pedido não exista, a resposta será:
```json
{
    "message": "Order not found"
}
```

- DELETE /pedidos/{id}: Deleta um pedido específico

A resposta será uma mensagem de sucesso.
```json
{
    "message": "Order 1 deleted successfully"
}
```

Caso o pedido não exista, a resposta será:
```json
{
    "message": "Order not found"
}
```

## Docs

O framework FASTAPI possui uma interface de documentação automática, que pode ser acessada em http://localhost:8000/docs

## Demonstração

Vídeo de demonstração: https://youtu.be/L-h0XlU_CzU