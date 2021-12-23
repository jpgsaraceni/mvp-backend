package models

import (
	"fmt"
)

type PaymentMethod struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
}

type Sale struct {
	ID              int     `json:"id"`
	ClientId        int     `json:"client_id"`
	PaymentMethodId int     `json:"payment_method_id"`
	ProductId       int     `json:"product_id"`
	Amount          int     `json:"amount"`
	Price           float64 `json:"price"`
}

type Response struct {
	Message string `json:"message,omitempty"`
	Data    struct {
		InsertID int         `json:"insert_id,omitempty"`
		UpdateID int         `json:"update_id,omitempty"`
		DeleteID int         `json:"deleted_id,omitempty"`
		Value    interface{} `json:"value,omitempty"`
	} `json:"data,omitempty"`
}

type Detail struct {
	Message string `json:"detail,omitempty"`
}

type SalesFilter struct {
	Client        string `json:"client,omitempty"`
	Product       string `json:"product,omitempty"`
	PaymentMethod string `json:"paymentMethod,omitempty"`
}

type RequestError struct {
	Code    int    `json:"code,omitempty"`
	Message string `json:"message,omitempty"`
}

func (e *RequestError) Error() string {
	return fmt.Sprintf("%v: %v", e.Code, e.Message)
}
