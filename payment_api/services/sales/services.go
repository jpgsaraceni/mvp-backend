package sl_service // sales service

import (
	"database/sql"
	"fmt"
	"os"
	"strconv"

	paymentsdb "github.com/jpgsaraceni/mvp-backend/payment_api/database"
	"github.com/jpgsaraceni/mvp-backend/payment_api/models"

	"github.com/joho/godotenv"
)

func CreateSale(sale models.Sale) (int, error) {
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	if sale.Amount < 1 {
		return 0, &models.RequestError{Code: 422, Message: "The amount cannot be zero or negative"}
	}

	if sale.ClientId < 1 {
		return 0, &models.RequestError{Code: 400, Message: "Invalid client ID"}
	}

	if sale.PaymentMethodId < 1 {
		return 0, &models.RequestError{Code: 400, Message: "Invalid payment method ID"}
	}

	if sale.Price < 0 {
		return 0, &models.RequestError{Code: 422, Message: "The price cannot be zero or negative"}
	}

	if sale.ProductId < 1 {
		return 0, &models.RequestError{Code: 400, Message: "Invalid product ID"}
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		INSERT INTO %v.sales (client_id, product_id, payment_method_id, amount, price)
		VALUES
			($1, $2, $3, $4, $5)
		RETURNING id
	`, os.Getenv("DB_SCHEMA"))

	var id int

	err = db.QueryRow(
		sqlStatement,
		sale.ClientId,
		sale.ProductId,
		sale.PaymentMethodId,
		sale.Amount,
		sale.Price,
	).Scan(&id)

	if err != nil {
		return 0, &models.RequestError{Code: 500, Message: "Unable to create sale"}
	}

	return id, err
}

func GetAllSales(filter models.SalesFilter) ([]models.Sale, error) {
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	filterByClient := ""
	filterByProduct := ""
	filterByPaymentMethod := ""

	if filter.Client != "" {
		clientId, err := strconv.Atoi(filter.Client)

		if err != nil {
			return nil, &models.RequestError{Code: 422, Message: "The client filter must be the number of a client ID"}
		}

		if clientId < 1 {
			return nil, &models.RequestError{Code: 400, Message: "The client filter must be a number greater than zero"}
		}

		filterByClient = fmt.Sprintf("WHERE client_id = %v", clientId)
	}

	if filter.PaymentMethod != "" {
		paymentMethodId, err := strconv.Atoi(filter.PaymentMethod)

		if err != nil {
			return nil, &models.RequestError{Code: 422, Message: "The payment method filter must be the number of a payment method ID"}
		}

		if paymentMethodId < 1 {
			return nil, &models.RequestError{Code: 400, Message: "The payment method filter must be a number greater than zero"}
		}

		filterByPaymentMethod = fmt.Sprintf("WHERE payment_method_id = %v", paymentMethodId)
	}

	if filter.Product != "" {
		productId, err := strconv.Atoi(filter.Product)

		if err != nil {
			return nil, &models.RequestError{Code: 422, Message: "The product filter must be the number of a product ID"}
		}

		if productId < 1 {
			return nil, &models.RequestError{Code: 400, Message: "The product filter must be a number greater than zero"}
		}

		filterByProduct = fmt.Sprintf("WHERE product_id = %v", productId)
	}

	sqlStatement := fmt.Sprintf(`
		SELECT id, client_id, product_id, payment_method_id, amount, price
			FROM %v.sales`,
		os.Getenv("DB_SCHEMA"))

	if filterByClient != "" {
		sqlStatement = fmt.Sprintf(`
			SELECT * FROM (%v) AS all_sales %v`, sqlStatement, filterByClient,
		)
	}

	if filterByProduct != "" {
		sqlStatement = fmt.Sprintf(`
			SELECT * FROM (%v) AS filter1 %v`, sqlStatement, filterByProduct,
		)
	}

	if filterByPaymentMethod != "" {
		sqlStatement = fmt.Sprintf(`
			SELECT * FROM (%v) AS filter2 %v`, sqlStatement, filterByPaymentMethod,
		)
	}

	var allSales []models.Sale

	db := paymentsdb.CreateConnection()
	defer db.Close()

	rows, err := db.Query(sqlStatement)
	// close the statement
	defer rows.Close()

	if err != nil {
		return nil, &models.RequestError{Code: 500, Message: "Unable to execute the sql statement"}
	}

	// iterate over the rows
	for rows.Next() {
		var sale models.Sale

		// unmarshal the row object to method
		err = rows.Scan(&sale.ID, &sale.ClientId, &sale.ProductId, &sale.PaymentMethodId, &sale.Amount, &sale.Price)

		if err != nil {
			return nil, &models.RequestError{Code: 500, Message: "Unable to unmarshal data"}
		}

		// append the method in the methods slice
		allSales = append(allSales, sale)
	}

	return allSales, err
}

func GetSingleSale(id string) (models.Sale, error) {
	var sale models.Sale

	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	numberID, err := strconv.Atoi(id)

	if err != nil {
		return sale, &models.RequestError{Code: 422, Message: "The ID must be a number"}
	}

	if numberID < 1 {
		return sale, &models.RequestError{Code: 400, Message: "The ID must be a number greater than zero"}
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		SELECT id, client_id, product_id, payment_method_id, amount, price
		FROM %v.sales
			WHERE id = $1
	`, os.Getenv("DB_SCHEMA"))

	row := db.QueryRow(sqlStatement, id)

	err = row.Scan(&sale.ID, &sale.ClientId, &sale.ProductId, &sale.PaymentMethodId, &sale.Amount, &sale.Price)

	if err != nil {
		switch err {
		case sql.ErrNoRows:
			return sale, &models.RequestError{Code: 404, Message: "Sale not found"}
		default:
			return sale, &models.RequestError{Code: 500, Message: "Unexpected failure while fetching data"}
		}
	}

	return sale, err
}
