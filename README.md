# E-commerce Admin API
This is an e-commerce backend web api that handles several functionalities related to inventory, sales, and products. 


Follow the instructions to get started with the application.

## Prerequisites
* Python 3.10+
* MySQL Server

## Database Setup
1. Create a MySQL database:
   ```
   CREATE DATABASE ecommerce_db;
   ```

2. Update the `DATABASE_URL` in `database.py`.

   Replace `root` with your MySQL username and `123456789` with your MySQL password:
   ```
   DATABASE_URL=mysql+pymysql://root:123456789@localhost:3306/ecommerce_db
   ```
   
## Create a Virtual Environment
   ```
   python -m venv venv
   ```
   
   Activate it on Windows
   ```
   .\venv\Scripts\activate
   ```

  Activate it on macOS/Linux
  ```
  source venv/bin/activate
  ```

## Install Dependencies
Run the following command to install all required packages:
```
pip install -r requirements.txt
```
## Database Table Creation
Run the application once to auto-generate the database tables:
```
python main.py
```
## Populate Demo Data
To add demo data for testing, run the following script:
```
python -m scripts.populate_demo_data
```
## Start the Server
Launch the FastAPI server using:
```
uvicorn main:app --reload
```

## API Endpoints Overview
| Endpoint            | Method | Description                                                  |
| ------------------- | ------ | ------------------------------------------------------------ |
| `/products`         | GET    | Get all products                                             |
| `/products`         | POST   | Add a new product                                            |
| `/sales`            | GET    | Retrieve and filter sales data                               |
| `/sales/revenue`    | GET    | Analyze revenue on a daily, weekly, monthly, or annual basis |
| `/sales/compare`    | GET    | Compare revenue across different periods and categories      |
| `/sales`            | POST   | Record a new sale                                            |
| `/inventory`        | GET    | Get current inventory status                                 |
| `/inventory/update` | PUT    | Update inventory levels                                      |
| `/low-stock`        | GET    | Get products with low stock (default threshold: 25)          |


Open your browser and navigate to: http://127.0.0.1:8000/docs
You will find the Swagger UI with all the API endpoints ready for testing.

### Swagger Documentation
![image](https://github.com/user-attachments/assets/576d9439-64a2-4bbe-9939-d2672cef905b)


### Live API Call
![image](https://github.com/user-attachments/assets/291ab454-b579-48e2-bbc3-ace915d2d4b6)


## Testing
Unit tests are located inside the `tests` folder.
To run the tests:
```
pytest tests/ --disable-warnings
```



