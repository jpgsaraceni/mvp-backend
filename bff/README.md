
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

#### Return all categories
```http
GET /products/categories
```
* **Content:**

```
[
  { id : 1, name : "cool category1", description: "cool description1" }
  { id : 2, name : "cool category2", description: "cool description2" }
]
```
&nbsp;

#### Return all payment methods
```http
GET /payment-methods
```
* **Content:**

```
[
  { id : 1, name : "cool method1" }
  { id : 2, name : "cool method2" }
]
```
&nbsp;

#### Get one payment method

```http
  GET /payment-method/:id
```

| Params      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. Payment method's ID |

### Expected response

* **Content:** `[{ id : 1, name : "cool method1" }]`
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

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `payment_method`      | `number` | **Required**. Payment method ID |
| `amount`      | `number` | **Optional** Amount of products (default to 1)|

### Expected response

* **Content:** `{ "message": "Sale created successfully" }`
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

## Run this api Locally

**IMPORTANT: TO RUN THIS PROJECT YOU NEED TO CONFIGURE AND RUN ALL OTHERS API**

Clone the project

```bash
  git clone https://github.com/jpgsaraceni/mvp-backend.git
```

Go to the session api directory

```bash
  cd mvp-backend/bff
```

Install dependencies

```bash
  npm install
```

OR

```bash
  yarn
```

Start the DEV server

```bash
  npm run dev
```

OR

```bash
  yarn
```

&nbsp;

**If you wanna build to production**

To Build for production

```bash
  npm run build
```

OR

```bash
  yarn build
```

To run optimized build

```bash
  npm run start
```

OR

```bash
  yarn start
```
