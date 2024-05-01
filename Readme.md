# Invoice Management System

This is an Invoice Management System built using Flask. It allows users to manage invoices, invoice lines, payments, approval history, school beneficiaries, and loan products.

## Features

- **User Management**: Users can register, login, and manage their profiles. Admin users have additional privileges.
- **Invoice Management**: Users can create, view, and update invoices. Invoices contain details such as invoice number, amount, date submitted, and extracted text.
- **Invoice Line Management**: Users can manage individual line items within invoices, including description, quantity, unit price, and total price.
- **Payment Management**: Users can record payments against invoices, including the amount paid and payment date.
- **Approval History**: The system keeps track of the approval history of invoices, including the approver, approval status, and approval date.
- **School Beneficiary Management**: Users can manage beneficiaries associated with schools, including their names and descriptions.
- **Loan Product Management**: Users can manage loan products, including the name, interest rate, and maximum loan amount.

## Prerequisites

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask RESTful
- PIL (Python Imaging Library)
- Pytesseract

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Morgan-Ngetich/hackathon.git
    cd invoice-management-system
    ```

2. Install dependencies:

    ```bash
   source venv/bin/activate
    ```

3. Initialize the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. Run the application:

    ```bash
    flask run
    ```

## Usage

Once the application is running, you can access the API endpoints using a REST client like Postman or by making HTTP requests programmatically.

### Endpoints

- **User Resource**:
    - `GET /users/<user_id>`: Get user details by user ID.
    
- **School Resource**:
    - `GET /schools/<school_id>`: Get school details by school ID.
    
- **Invoice Resource**:
    - `GET /invoices/<invoice_id>`: Get invoice details by invoice ID.
    - `POST /invoices/<invoice_id>`: Upload an image file for OCR processing and update invoice with extracted text.
    
- **Invoice Line Resource**:
    - `GET /invoice-lines/<line_id>`: Get invoice line details by line ID.
    
- **Payment Resource**:
    - `GET /payments/<payment_id>`: Get payment details by payment ID.
    
- **Approval History Resource**:
    - `GET /approval-history/<approval_id>`: Get approval history details by approval ID.
    
- **School Beneficiary Resource**:
    - `GET /school-beneficiaries/<beneficiary_id>`: Get school beneficiary details by beneficiary ID.
    
- **Loan Product Resource**:
    - `GET /loan-products/<product_id>`: Get loan product details by product ID.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your contributions.

## License

This project is licensed under the [MIT License](LICENSE).
