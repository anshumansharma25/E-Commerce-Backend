# 🛒 E-Commerce Backend API

This project is a scalable and modular **E-Commerce backend** built using **FastAPI** and **PostgreSQL**. It handles core functionalities such as user management, product browsing, cart operations, checkout processing, and order history tracking.

---

## 🎯 Objective

To design a fully functional backend system capable of handling essential operations of an online store, including authentication, secure transactions, and order lifecycle management — all while maintaining modularity, reusability, and API responsiveness.

---

## ⚙️ Core Features

### 🔐 Authentication & Security
- User registration and JWT-based login
- Secure password hashing and validation
- Forgot & Reset password via email with token-based verification

### 🛍️ Product Browsing
- View products with category, price, and sorting filters
- Search by keyword
- Detailed product information
- Admin-only: Create, update, and delete products

### 🛒 Cart Operations
- Add items to cart
- Remove items or update quantities
- View current cart with calculated total

### 💳 Checkout & Order Management
- Checkout endpoint (with dummy payment handling)
- Automatic order creation with full details
- Cart clearance post-purchase
- View order history and detailed order line items

---

## 🧠 Technologies Used

- **FastAPI**: For building high-performance REST APIs
- **SQLite**: Reliable and scalable relational database
- **SQLAlchemy**: ORM for managing database models and queries
- **Pydantic**: Data validation and schema management
- **JWT**: Authentication and authorization
- **SMTP**: Email service for password reset
- **dotenv**: Secure environment variable management

---

## 📌 Highlights

- Modular codebase: Each functionality (auth, products, cart, orders) is split into separate modules
- Clean REST API design following best practices
- Strong security principles with token expiration, hashed passwords, and secure email-based password reset
- Well-handled user sessions and error responses
- Environment isolation via `.env` and `.gitignore` to protect sensitive credentials

---

## 🔗 Postman Collection

You can test all the API endpoints using the following Postman collection:

**[👉 Click here to access the Postman Collection](https://github.com/anshumansharma25/E-Commerce-Backend/blob/main/postman/E-commerce%20Backend%20API.postman_collection.json)**
---

## 📦 Future Enhancements

- Integration with real payment gateways like Razorpay or Stripe
- Rate limiting and email verification for accounts
- Admin dashboard for product and order management
- Docker containerization for deployment

---

## 👨‍💻 Developed By

**Anshuman Sharma**  
GitHub: [@anshumansharma25](https://github.com/anshumansharma25)
