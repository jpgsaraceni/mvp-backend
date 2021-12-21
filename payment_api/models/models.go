package models

import (
	"fmt"
)

type PaymentMethod struct {
	ID   int64  `json:"id"`
	Name string `json:"name"`
}

type Sale struct {
	ID              int64   `json:"id"`
	ClientId        int64   `json:"client_id"`
	PaymentMethodId int64   `json:"payment_method_id"`
	ProductId       int64   `json:"product_id"`
	Amount          int64   `json:"amount"`
	Price           float64 `json:"price"`
}

type Response struct {
	Message string `json:"message,omitempty"`
	Data    struct {
		InsertID  int64       `json:"insert_id,omitempty"`
		UpdateID  int64       `json:"update_id,omitempty"`
		DeleteID int64       `json:"deleted_id,omitempty"`
		Value     interface{} `json:"value,omitempty"`
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
	Code    int64  `json:"code,omitempty"`
	Message string `json:"message,omitempty"`
}

func (e *RequestError) Error() string {
	return fmt.Sprintf("%v: %v", e.Code, e.Message)
}
