# Payment API

Mock payment route.

This API accepts all `POST` requests on `/authorization` route, and always responds with

```json
{
    "payment": "confirmed"
}
```

There is no authentication on this route, because there is no actual payment.

## Payment methods routes
This API accepts the following methods on `/payment-methods`:

### GET

```http
GET /payment-methods
```

Return all of the available payment methods.

Possible responses:
```json
- STATUS CODE 200 OK

{
	"message": "Payment methods fetched successfully",
	"data": {
		"value": [
			{
				"id": <int>,
				"name": <string>
			},
			{
				"id": <int>,
				"name": <string>
			},
		]
	}
}
```

```json
- STATUS CODE 500 Internal Server Error

{
    "detail": <string>
}
```
---
```http
GET /payment-methods/:id
```

Return a specific payment method by its ID.

Possible responses:

```json
- STATUS CODE 200 OK

{
	"message": "Payment method fetched successfully",
	"data": {
		"value": [
			{
				"id": <int>,
				"name": <string>
			}
		]
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 400 Bad Request
- STATUS CODE 404 Not Found
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```

---
### POST
```http
POST /payment-methods
```
```json
body {
    "name": <string>
}
```
Create a new payment method with the specified name.

Possible responses:

```json
- STATUS CODE 201 CREATED

{
	"message": "Payment method created successfully",
	"data": {
		"insert_id": <int>
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```

---

### PUT
```http
PUT /payment-methods/:id
```
```json
body {
    "name": <string>
}
```
Update the specified payment method with the provided name.

Possible responses:

```json
- STATUS CODE 200 OK

{
	"message": "Payment method updated successfully",
	"data": {
		"insert_id": <int>
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 400 Bad Request
- STATUS CODE 404 Not Found
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```
---
### DELETE
```http
DELETE /payment-methods/:id
```
Delete the specified payment method with the provided name.

Possible responses:

```json
- STATUS CODE 200 OK

{
	"message": "Payment method deleted successfully",
	"data": {
		"delete_id": <int>
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 400 Bad Request
- STATUS CODE 404 Not Found
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```

## Sales routes
This API accepts the following methods on `/sales`:

### GET

```http
GET /sales?client={int}&product={int}&payment-method={int}
```

Returns all sales, accepts filter by `client` ID, `product` ID and `payment-method` ID.

Possible responses:
```json
- STATUS CODE 200 OK

{
	"message": "Sales fetched successfully",
	"data": {
		"value": [
			{
				"id": <int>,
				"client_id": <int>,
				"payment_method_id": <int>,
				"product_id": <int>,
				"amount": <int>,
				"price": <float>
			},
			{
				"id": <int>,
				"client_id": <int>,
				"payment_method_id": <int>,
				"product_id": <int>,
				"amount": <int>,
				"price": <float>
			},
        ]
	}
}
```

```json
- STATUS CODE 500 Internal Server Error

{
    "detail": <string>
}
```
---
```http
GET /sales/:id
```

Return an especific sale by its ID. Possible responses:

```json
- STATUS CODE 200 OK

{
	"message": "Sale fetched successfully",
	"data": {
		"value": [
			{
				"id": <int>,
				"client_id": <int>,
				"payment_method_id": <int>,
				"product_id": <int>,
				"amount": <int>,
				"price": <float>
			},
		]
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 404 Not Found
- STATUS CODE 400 Bad Request
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```

---
### POST
```http
POST /sales
```
``` json
body {
	"client_id": <int>,
	"product_id": <int>,
	"payment_method_id": <int>,
	"amount": <int>,
	"price": <float>
}
```
Create a new sale with the specified attributes.

Possible responses:

```json
- STATUS CODE 201 CREATED

{
	"message": "Sale created successfully",
	"data": {
		"insert_id": <int>
	}
}
```

```json
- STATUS CODE 500 Internal Server Error
- STATUS CODE 422 Unprocessable Entity

{
    "detail": <string>
}
```


## Running locally

You will need [golang](https://go.dev/dl/) installed on your machine. In the `payment_api` directory, run

```bash
go run main.go
```

in your terminal. Make sure to configure your `.env` variables. Currently needed variables:
```
SERVER_PORT=portYouWantTheAPI

DB_USER=yourDatabaseUser
DB_PASS=yourDatabasePassword
DB_HOST=yourDatabaseHost
DB_PORT=yourDatabasePort
DB_NAME=yourDatabaseName
DB_SCHEMA=yourDatabaseSchema
```
Then you can make the requests you want to `http://localhost:{PORT_YOU_SET_ON_DOTENV}`.

## Future implementation

The initial idea is that this api will continue to only listen to POST requests on `/authorize` route. The difference will be the request body (currently not being read), and response body `"payment"` may also be `"denied"`.
