
# Session API

API responsible to control register and login

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

#### Login an user

```http
  POST /login
```

**You should use Basic Authorization for this project, to know more**: <https://pt.stackoverflow.com/questions/254503/o-que-%C3%A9-basic-auth>

### Expected response

* **Content:** `{ id: 4, "email": "coolemail@hotmail.com", name: "coolname", token: "cool jwt token" }`
&nbsp;

## Run Locally

Clone the project

```bash
  git clone https://github.com/jpgsaraceni/mvp-backend.git
```

Go to the project directory

```bash
  cd mvp-backend/session_api
```

Install dependencies

```bash
  npm install or yarn
```

**IMPORTANT: Configure your .env following the .env.example BEFORE GO TO THE NEXT STEP**

After, Run Prisma migrations

```bash
  npx prisma migrate dev --name init
```

**Important: after this re-open your visual studio code/IDE**

Start the DEV server

```bash
  npm run dev or yarn dev
```

**OR**

To Build for production

```bash
  npm run build or yarn build
```

To run optimized build

```bash
  npm run start or yarn start
```
