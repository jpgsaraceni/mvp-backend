
# BFF API

API for handle all the requests





## API Reference

#### Get top 10 from ranking

```http
  GET /ranking
```
### Expected response
* **Content:** `{ position : 1, name : "cool name", score: 100 }`
&nbsp;


#### Insert rank

```http
  POST /ranking
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Player's name |
| `score`     | `number` | **Required**. Player's score |

### Expected response
* **Content:** `{ success: "Ranking added" }`
&nbsp;

#### Return all products

```http
  GET /products
```
* **Content:**
```
{ id : 1, name : "cool product1", description: "cool description1", price: 100, image: cool image  }
{ id : 2, name : "cool product2", description: "cool description2", price: 220, image: cool image  }
```
&nbsp;

#### Get one product

```http
  GET /product
```

| Query      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. Product's ID |

### Expected response
* **Content:** `{ id : 1, name : "cool product1", description: "cool description1", price: 100, image: cool image  }`
&nbsp;


#### Purchase one product

```http
  POST /purchase/{product_id}
```

| Params      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `product_id`      | `number` | **Required**. Product's ID |

### Expected response
* **Content:** `{ "payment": "confirmed" }`
&nbsp;

#### Register an account

```http
  POST /register
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. Person's email |
| `name`       | `string` | **Required**. Person's name |
| `password`   | `string` | **Required**. Person's password |

### Expected response
* **Content:** `{ "success": "Account created" }`
&nbsp;


#### Return user data

```http
  POST /login
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. Person's email |
| `password`   | `string` | **Required**. Person's password |

### Expected response
* **Content:** `{ "id": 1, "name": cool name, "token": cool jwt token }`
&nbsp;

