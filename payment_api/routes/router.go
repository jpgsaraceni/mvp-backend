package payment_api_rotues

import (
    "github.com/jpgsaraceni/mvp-backend/payment_api/controller/payment_methods"
    "github.com/jpgsaraceni/mvp-backend/payment_api/controller/purchase"
    "github.com/jpgsaraceni/mvp-backend/payment_api/controller/sales"

    "github.com/gorilla/mux"
)

// Router is exported and used in main.go
func Router() *mux.Router {

    router := mux.NewRouter()

	// Purchase routes
	router.HandleFunc("/authorize", purchase.Authorize).Methods("POST", "OPTIONS")

	// Payment methods routes
    router.HandleFunc("/payment-methods/{id}", paymentmethods.GetPaymentMethodByID).Methods("GET", "OPTIONS")
    router.HandleFunc("/payment-methods/{id}", paymentmethods.UpdatePaymentMethod).Methods("PUT", "OPTIONS")
    router.HandleFunc("/payment-methods/{id}", paymentmethods.DeletePaymentMethod).Methods("DELETE", "OPTIONS")
    router.HandleFunc("/payment-methods", paymentmethods.GetAllPaymentMethods).Methods("GET", "OPTIONS")
    router.HandleFunc("/payment-methods", paymentmethods.CreatePaymentMethod).Methods("POST", "OPTIONS")

	// Sales routes
	router.HandleFunc("/sales/{id}", sales.GetSaleByID).Methods("GET", "OPTIONS")
	router.HandleFunc("/sales", sales.CreateSale).Methods("POST", "OPTIONS")
	router.HandleFunc("/sales", sales.GetAllSales).Methods("GET", "OPTIONS")

    return router
}