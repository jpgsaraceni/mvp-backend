# STORE API

This API is responsible for managing the store products.
You can create, read, update and delete products using it.

## Testing locally
### Requirements:
- Python 3.8 or later (**3.8.9 recommended**)
- pip 21.3.1
- Postgres 13 or later (**14.1 recommended**)

You can check your `Python`, `pip` and `Postgres` version by running:
```
$ python3 --version && pip --version && postgres -V postgres 
```

By this point, we suppose you have already cloned this repository, if you don't, do it.

```
$ git clone https://github.com/jpgsaraceni/mvp-backend
```

Now you will need to create a `.env` file in the `store_api` directory containing the following variables:
```
DB_USER=yourDatabaseUser
DB_PASS=yourDatabasePassword
DB_HOST=yourDatabaseHost
DB_PORT=yourDatabasePort
DB_NAME=yourDatabaseName
```

If you've followed all the steps until here, we are almost ready to run the API.

The last step is running the following command, in the `store_api/app` directory:

```
$ python3 -m pip install -r requirements.txt
```

It will install all the python packages we need to run the API.

You may need to update the `requirements.txt` path according to your location in the repository.

Now, inside the `store_api` directory, run the following command:

```
$ python3 -m uvicorn main:app --reload --port 5000 
```

The output will be something like this:

```
  Will watch for changes in these directories: ['{yourAbsolutePath}/mvp-backend/store_api']
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [7368] using statreload
INFO:     Started server process [7371]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then you can just open the link shown in the first INFO line in your browser.

If you go to `/docs`, you will find all the API documentation, its endpoints, the parameters the endpoints receive, the responses and even try them out (will modify your database).
