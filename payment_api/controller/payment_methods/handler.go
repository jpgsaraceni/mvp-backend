package paymentmethods

import (
	"encoding/json" // package to encode and decode the json into struct and vice versa
	"log"
	"net/http" // used to access the request and response object of the api
	
	"github.com/gorilla/mux" // used to get the params from the route

	"github.com/jpgsaraceni/mvp-backend/payment_api/models"
	pm_service "github.com/jpgsaraceni/mvp-backend/payment_api/services/payment_methods"
)

func CreatePaymentMethod(w http.ResponseWriter, r *http.Request) {
	// set the header to content type x-www-form-urlencoded
	// Allow all origin to handle cors issue
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "POST")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// paymentMethod creates an empty payment method of type models.PaymentMethod
	var paymentMethod models.PaymentMethod

	// decode the json request to paymentMethod
	err := json.NewDecoder(r.Body).Decode(&paymentMethod)

	if err != nil {
		log.Fatalf("Unable to decode the request body %v", err)
	}

	insertID, err := pm_service.CreatePaymentMethod(paymentMethod)

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

	// res formats a response object
	var res models.Response

	res.Message = "Payment method created successfully"
	res.Data.InsertID = insertID

	// send the response
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(res)
}

func GetPaymentMethodByID(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")

	// get the params from the request params
	id := mux.Vars(r)["id"]

	method, err := pm_service.GetSinglePaymentMethod(id)

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
	var methods[] models.PaymentMethod

	res.Message = "Payment method fetched successfully"
	res.Data.Value = append(methods, method)

	json.NewEncoder(w).Encode(res)
}

func GetAllPaymentMethods(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")

	methods, err := pm_service.GetAllPaymentMethods()

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

	res.Message = "Payment methods fetched successfully"
	res.Data.Value = methods

	json.NewEncoder(w).Encode(res)
}

func UpdatePaymentMethod(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "PUT")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// get the userid from the request params, the key is "id"
	id := mux.Vars(r)["id"]

	method, err := pm_service.GetSinglePaymentMethod(id)

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

	// create an empty payment method of type models.PaymentMethod
	var updatedMethod models.PaymentMethod

	// decode the json request to paymentMethod
	err = json.NewDecoder(r.Body).Decode(&updatedMethod)

	updatedID, err := pm_service.UpdatePaymentMethod(method.ID, updatedMethod)

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
	res.Message = "Payment method updated successfully"
	res.Data.UpdateID = updatedID
	json.NewEncoder(w).Encode(res)
}

func DeletePaymentMethod(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Context-Type", "application/x-www-form-urlencoded")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "DELETE")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// get the userid from the request params, the key is "id"
	id := mux.Vars(r)["id"]

	method, err := pm_service.GetSinglePaymentMethod(id)

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

	deletedID, err := pm_service.DeletePaymentMethod(method.ID)

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
	res.Message = "Payment method deleted successfully"
	res.Data.DeleteID = deletedID
	json.NewEncoder(w).Encode(res)
}

