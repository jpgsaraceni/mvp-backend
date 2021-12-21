package purchase

import (
	"encoding/json" // package to encode and decode the json into struct and vice versa

	"net/http" // used to access the request and response object of the api
)

// authorize receives a request and, if the method is POST, writes a json with status: accepted.
func Authorize(w http.ResponseWriter, req *http.Request) {
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
