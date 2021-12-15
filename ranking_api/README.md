
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



## Run Locally

Clone the project

```bash
  git clone https://github.com/jpgsaraceni/mvp-backend.git
```

Go to the project directory

```bash
  cd mvp-backend/ranking-api
```

Install dependencies

```bash
  npm install
```

**Configure your .env following the .env.example**

After, build the DB Model and run migrations

```bash
  npx prisma migrate dev --name init
```

Start the server

```bash
  npm run start
```

