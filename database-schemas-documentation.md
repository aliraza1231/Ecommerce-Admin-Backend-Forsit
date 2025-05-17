# Database Tables Documentation

## Tables

### `products` Table

| Column   | Type         | Description                                                         |
| -------- | ------------ | ------------------------------------------------------------------- |
| id       | Integer (PK) | Unique identifier for each product.                                 |
| name     | String       | The name of the product (e.g., iPhone 14).                          |
| category | String       | The category the product belongs to (e.g., Electronics, Furniture). |
| price    | Float        | The price of the product.                                           |

<b>Purpose:</b>

Stores details of all available products. It serves as the main reference for product-related operations like inventory management, sales, and stock history.


###  `inventory` Table
| Column      | Type         | Description                                                                       |
| ----------- | ------------ | --------------------------------------------------------------------------------- |
| id          | Integer (PK) | Unique identifier for each inventory record.                                      |
| product_id | Integer (FK) | Foreign Key referencing `products.id`. Links the inventory record to its product. |
| quantity    | Integer      | The number of units available in stock.                                           |

<b>Purpose:</b>

Maintains the stock levels for each product. This is the main source for checking availability and updating stock.

<b>Relationships:</b>

product_id → products.id: Links each inventory entry to its corresponding product.

### `sales` Table
| Column      | Type         | Description                                                           |
| ----------- | ------------ | --------------------------------------------------------------------- |
| id          | Integer (PK) | Unique identifier for each sale transaction.                          |
| product_id | Integer (FK) | Foreign Key referencing `products.id`. Links the sale to its product. |
| quantity    | Integer      | Number of units sold in the transaction.                              |
| sale_date  | DateTime     | The date and time the sale occurred.                                  |

<b>Purpose:</b>

Tracks all sales transactions, including which products were sold, the quantity, and the date of sale. It is used for revenue calculations and sales analytics.

<b>Relationships:</b>

product_id → products.id: Links each sale to its respective product.

### `inventory_history` Table
| Column       | Type         | Description                                                                    |
| ------------ | ------------ | ------------------------------------------------------------------------------ |
| id           | Integer (PK) | Unique identifier for each inventory history record.                           |
| product_id  | Integer (FK) | Foreign Key referencing `products.id`. Links the history entry to its product. |
| quantity     | Integer      | Quantity recorded at the time of change.                                       |
| change_date | DateTime     | The timestamp of the inventory change.                                         |

<b>Purpose:</b>

Logs every change in inventory levels (additions or subtractions) for historical reference. This helps in auditing stock movements and diagnosing discrepancies.

<b>Relationships:<b/>

product_id → products.id: Links each inventory change to its corresponding product.

## Database Relationships
* products → inventory → inventory_history
  A product has an associated inventory record, and every change in that inventory is logged in the `inventory_history`.

* products → sales
  A product can have multiple sales transactions linked to it.

