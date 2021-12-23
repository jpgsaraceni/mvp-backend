package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	paymentsdb "github.com/jpgsaraceni/mvp-backend/payment_api/database"
	payment_api_rotues "github.com/jpgsaraceni/mvp-backend/payment_api/routes"
)

func main() {
	paymentsdb.SetUpDatabase()

	err := godotenv.Load()
	if err != nil {
		fmt.Print("Error loading .env file")
	}

	r := payment_api_rotues.Router()

	PORT := os.Getenv("SERVER_PORT")
	STR_PORT := fmt.Sprintf(":%v", PORT)

	log.Printf("Server started on port %s", PORT)
	log.Fatal(http.ListenAndServe(STR_PORT, r))
}
