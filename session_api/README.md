
# Session API

API responsible for controlling register and login

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file\
**For an example see .env.example**

`DATABASE_URL`

`SECRET`

## API Reference

#### Register an user

```http
  POST /register
```

| Body      | Type     | Description                         |
| :-------- | :------- | :-------------------------          |
| `name`    | `string` | **Required**. Person's name         |
| `email`   | `string` | **Required**. Person's email        |
| `password`| `string` | **Required**. Person's password     |

### Expected response

* **Content:** `{ id: 4, "email": "coolemail@hotmail.com", name: "coolname", password: "coolbcryptpassword", "created_at": "cool date" }`
&nbsp;

#### Get coins

```http
  GET /coins
```

| Cookies      | Type     | Description                         |
| :-------- | :------- | :-------------------------          |
| `auth`    | `string` | **Required**. Person's JWT Cookie         |

### Expected response

* **Content:** `{ 20 }`
&nbsp;

#### Update coins

```http
  PUT /coins
```

| Cookies/Body      | Type     | Description                         |
| :-------- | :------- | :-------------------------          |
| `auth`(cookie)    | `string` | **Required**. Person's JWT Cookie         |
| `coins`(body)    | `number` | **Required**. Person's coins to update         |

### Expected response

* **Content:** `{ 40 }`
&nbsp;

#### Login an user

```http
  POST /login
```

**You should use Basic Authorization for this project, to know more**: <https://pt.stackoverflow.com/questions/254503/o-que-%C3%A9-basic-auth>

### Expected response

* **Content:** `{ id: 4, "email": "coolemail@hotmail.com", name: "coolname", token: "cool jwt token" }`
&nbsp;

## Run this api Locally

Clone the project

```bash
  git clone https://github.com/jpgsaraceni/mvp-backend.git
```

Go to the session api directory

```bash
  cd mvp-backend/session_api
```

Install dependencies

```bash
  npm install
```

OR

```bash
  yarn
```

**IMPORTANT: Configure your .env following the .env.example BEFORE GOING TO THE NEXT STEP**

After, Run Prisma migrations

```bash
  npx prisma migrate dev --name init
```

**Important: after this reopen your visual studio code/IDE**

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
