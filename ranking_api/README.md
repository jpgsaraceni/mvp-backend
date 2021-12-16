
# Ranking API

An API for proccess the ranking system

## API Reference

#### Add a new ranking for a player score

```http
  POST /addranking
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name`    | `string` | **Required**. Player's name |
| `score`   | `int` | **Required**. Player's score |

### Expected response

* **Content:** `{ position : 1, name : "cool player", score: 100 }`
&nbsp;

#### Get Top 10 Ranking

```http
  GET /ranking
```

### Expected response

* **Content:**

```
{ position : 1, name : "cool player", score: 100 }
{ position : 2, name : "cool player2", score: 95 }
```

&nbsp;

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
\
You can check an example inside **.env.example**

`DATABASE_URL`

## Run this api Locally

Clone the project

```bash
  git clone https://github.com/jpgsaraceni/mvp-backend.git
```

Go to the session api directory

```bash
  cd mvp-backend/ranking_api
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
