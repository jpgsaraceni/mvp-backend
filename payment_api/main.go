package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
)

// authorize receives a request and, if the method is POST, writes a json with status: accepted.
func authorize(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if req.Method == "POST" {
		response := map[string]string{
			"payment": "confirmed",
		}

		json.NewEncoder(w).Encode(response)

		return
	}
	http.Error(w, "Invalid request method.", http.StatusMethodNotAllowed)
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	http.HandleFunc("/authorize", authorize)

	log.Fatal(http.ListenAndServe(os.Getenv("SERVER_PORT"), nil))
}
