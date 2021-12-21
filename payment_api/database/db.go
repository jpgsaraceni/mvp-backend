package paymentsdb

import (
	"database/sql"
	"fmt"
	"os"
	"github.com/joho/godotenv"
	_ "github.com/lib/pq" 
)

func CreateConnection() *sql.DB {
	// load .env file
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	url := fmt.Sprintf("postgres://%v:%v@%v:%v/%v?sslmode=disable",
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASS"),
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_NAME"))

	// open the connection
	db, err := sql.Open("postgres", url)

	if err != nil {
		panic(err)
	}

	// check the connection
	err = db.Ping()

	if err != nil {
		panic(err)
	}

	// return the connection
	return db
}

func SetUpDatabase() {
	db := CreateConnection()
	defer db.Close()

	sqlStatement := fmt.Sprintf("CREATE SCHEMA IF NOT EXISTS %v", os.Getenv("DB_SCHEMA"))

	_, errCreating := db.Query(sqlStatement)

	if errCreating != nil {
		fmt.Printf("Unable to execute the query. %v", errCreating)
	}

	createPaymentMethodsTable(db)
	createSalesTable(db)

	return
}

func createPaymentMethodsTable(db *sql.DB) {
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	sqlStatement := fmt.Sprintf(`CREATE TABLE IF NOT EXISTS %v.payment_methods (
		id serial NOT NULL,
		name varchar(50) NOT NULL,
		inactivated_at timestamp with time zone,
		updated_at timestamp with time zone,
		CONSTRAINT payment_pkey
			PRIMARY KEY (id)
	)`, os.Getenv("DB_SCHEMA"))

	_, errCreating := db.Query(sqlStatement)

	if errCreating != nil {
		fmt.Printf("Unable to execute the query. %v", errCreating)
	}

	return
}

func createSalesTable(db *sql.DB) {
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Print("Error loading .env file")
	}

	sqlStatement := fmt.Sprintf(`CREATE TABLE IF NOT EXISTS %v.sales (
		id serial NOT NULL,
		client_id integer NOT NULL,
		product_id integer NOT NULL,
		amount integer NOT NULL,
		price decimal(5,2) NOT NULL,
		payment_method_id integer NOT NULL,
		CONSTRAINT sales_pkey
			PRIMARY KEY (id),
		CONSTRAINT method_fk
			FOREIGN KEY (payment_method_id)
				REFERENCES %v.payment_methods(id)
	)`,
		os.Getenv("DB_SCHEMA"),
		os.Getenv("DB_SCHEMA"),
	)

	_, errCreating := db.Query(sqlStatement)

	if errCreating != nil {
		fmt.Printf("Unable to execute the query. %v", errCreating)
	}

	return
}
