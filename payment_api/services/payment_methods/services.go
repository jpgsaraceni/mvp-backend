package pm_service // payment methods service

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	paymentsdb "github.com/jpgsaraceni/mvp-backend/payment_api/database"
	"github.com/jpgsaraceni/mvp-backend/payment_api/models"

	"github.com/joho/godotenv"
	"strconv"
)

func CreatePaymentMethod(paymentMethod models.PaymentMethod) (int64, error) {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatal("Error loadinf .env file")
	}

	if paymentMethod.Name == "" {
		return 0, &models.RequestError{Code: 422, Message: "Name is required"}
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		INSERT INTO %v.payment_methods (name)
		VALUES
			($1)
		RETURNING id
	`, os.Getenv("DB_SCHEMA"))

	var id int64

	err = db.QueryRow(sqlStatement, paymentMethod.Name).Scan(&id)

	if err != nil {
		return 0, &models.RequestError{Code: 500, Message: "Unable to create payment method"}
	}

	return id, err
}

func GetSinglePaymentMethod(id string) (models.PaymentMethod, error) {
	var method models.PaymentMethod

	err := godotenv.Load(".env")

	if err != nil {
		log.Fatal("Error loading .env file")
	}
	numberID, err := strconv.Atoi(id)

	if err != nil {
		return method, &models.RequestError{Code: 422, Message: "The ID must be a number"}
	}

	if numberID < 1 {
		return method, &models.RequestError{Code: 400, Message: "The ID must be a number greater than zero"}
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		SELECT id, name FROM %v.payment_methods
			WHERE id = $1 AND inactivated_at IS NULL
	`, os.Getenv("DB_SCHEMA"))


	row := db.QueryRow(sqlStatement, id)

	err = row.Scan(&method.ID, &method.Name)

	if err != nil {
		switch err {
		case sql.ErrNoRows:
			return method, &models.RequestError{Code:404, Message: "Payment method not found"}
		default:
			return method, &models.RequestError{Code:500, Message: "Unexpected failure while fetching data"}
		}
	}

	return method, err
}

func GetAllPaymentMethods() ([]models.PaymentMethod, error) {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatal("Error loading .env file")
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		SELECT id, name FROM %v.payment_methods WHERE inactivated_at IS NULL
	`, os.Getenv("DB_SCHEMA"))

	var methods []models.PaymentMethod

	rows, err := db.Query(sqlStatement)
	// close the statement
	defer rows.Close()

	if err != nil {
		return nil, &models.RequestError{Code: 500, Message: "Unexpected failure while fetching data"}
	}

	// iterate over the rows
	for rows.Next() {
		var method models.PaymentMethod

		// unmarshal the row object to method
		err = rows.Scan(&method.ID, &method.Name)

		if err != nil {
			return nil, &models.RequestError{Code: 500, Message: "Unable to unmarshal data"}
		}

		// append the method in the methods slice
		methods = append(methods, method)
	}

	return methods, err
}

func UpdatePaymentMethod(id int64, paymentMethod models.PaymentMethod) (int64, error) {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatal("Error loadinf .env file")
	}

	if paymentMethod.Name == "" {
		return 0, &models.RequestError{Code: 422, Message: "Name is required"}
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		UPDATE %v.payment_methods
		SET
			name = $1
		WHERE
			id = $2
		RETURNING id
	`, os.Getenv("DB_SCHEMA"))

	err = db.QueryRow(sqlStatement, paymentMethod.Name, id).Scan(&id)

	if err != nil {
		return 0, &models.RequestError{Code: 500, Message: "Unable to update payment method"}
	}

	return id, err
}

func DeletePaymentMethod(id int64) (int64, error) {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatal("Error loadinf .env file")
	}

	db := paymentsdb.CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf(`
		UPDATE %v.payment_methods
		SET
			inactivated_at = now()
		WHERE
			id = $1
		RETURNING id
	`, os.Getenv("DB_SCHEMA"))

	err = db.QueryRow(sqlStatement, id).Scan(&id)

	if err != nil {
		return 0, &models.RequestError{Code: 500, Message: "Unable to delete payment method"}
	}

	return id, err
}