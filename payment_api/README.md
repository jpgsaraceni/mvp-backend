# Payment API

Mock payment route.

This API accepts all `POST` requests on `/authorization` route, and always responds with

```json
{
    "payment": "confirmed"
}
```

There is no authentication on this route, because there is no actual payment.

## Running locally

You will need [golang](https://go.dev/dl/) installed on your machine. In the `payment_api` directory, run

```bash
go run main.go
```

in your terminal. Make sure to configure your .env variables. Currently, only SERVER_PORT is needed. Then you can make POST requests to `localhost:{PORT_YOU_SET_ON_DOTENV}/authorize`.

## Future implementation

The initial idea is that this api will continue to only listen to POST requests on `/authorize` route. The difference will be the request body (currently not being read), and response body `"payment"` may also be `"denied"`.
