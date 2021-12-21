package sales

import (
	"encoding/json" // "encoding/json" // package to encode and decode the json into struct and vice versa
	// "fmt"

	"github.com/gorilla/mux" // used to get the params from the route

	"log"
	"net/http" // used to access the request and response object of the api

	"github.com/jpgsaraceni/mvp-backend/payment_api/models"
	sl_service "github.com/jpgsaraceni/mvp-backend/payment_api/services/sales"


)

func CreateSale(w http.ResponseWriter, r *http.Request) {
	// set the header to content type x-www-form-urlencoded
	// Allow all origin to handle cors issue
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "POST")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// create an empty payment method of type models.PaymentMethod
	var sale models.Sale

	// decode the json request to paymentMethod
	err := json.NewDecoder(r.Body).Decode(&sale)

	if err != nil {
		log.Fatalf("Unable to decode the request body %v", err)
	}

	insertID, err := sl_service.CreateSale(sale)

	if err != nil {
		var res models.Detail
		switch e := err.(type) {
		case *models.RequestError:
			res.Message = e.Message
			w.WriteHeader(int(e.Code))
			json.NewEncoder(w).Encode(res)
			
		default:
			res.Message = "Unexpected failure"
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(res)
		}	
		return
	}

	// format a response object
	var res models.Response

	res.Message = "Sale created successfully"
	res.Data.InsertID = insertID

	// send the response
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(res)
}

func GetAllSales(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")

	client := r.FormValue("client")
	paymentMethod := r.FormValue("payment-method")
	product := r.FormValue("product")

	var res models.Response
	var filters models.SalesFilter

	filters.Client = client
	filters.Product = product
	filters.PaymentMethod = paymentMethod

	sales, err := sl_service.GetAllSales(filters)

	if err != nil {
		var res models.Detail
		switch e := err.(type) {
		case *models.RequestError:
			res.Message = e.Message
			w.WriteHeader(int(e.Code))
			json.NewEncoder(w).Encode(res)
		default:
			res.Message = "Unexpected failure"
			w.WriteHeader(500)
			json.NewEncoder(w).Encode(res)
		}

		return
	}


	res.Message = "Sales fetched successfully"
	res.Data.Value = sales
	
	json.NewEncoder(w).Encode(res)
}

func GetSaleByID(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")

	// get the params from the request params
	id := mux.Vars(r)["id"]

	sale, err := sl_service.GetSingleSale(id)

	if err != nil {
		var res models.Detail
		switch e := err.(type) {
		case *models.RequestError:
			res.Message = e.Message
			w.WriteHeader(int(e.Code))
			json.NewEncoder(w).Encode(res)
		default:
			res.Message = "Unexpected failure"
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(res)
		}

		return
	}

	var res models.Response
	var sales[] models.Sale

	res.Message = "Sale fetched successfully"
	res.Data.Value = append(sales, sale)

	json.NewEncoder(w).Encode(res)
}