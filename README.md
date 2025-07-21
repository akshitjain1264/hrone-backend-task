# 🛍️ E-Commerce API — FastAPI + MongoDB

A production-ready, modular **E-Commerce REST API** built using **FastAPI** and **MongoDB Atlas**, ideal for managing products and customer orders. This project demonstrates clean architecture with separate layers for routes, models, and schemas.

---

## 📂 Project Structure

├── app/
│ ├── models/ # Database models and helper functions
│ ├── routes/ # API route handlers for products and orders
│ ├── schemas/ # Pydantic models for request and response validation
│ └── database.py # MongoDB connection via Motor
├── main.py # FastAPI app entry point
├── requirements.txt # Dependencies
├── render.yaml # Deployment config for Render
├── .env # Environment variables (Mongo URI, etc.)
└── README.md # You're here!


---

## ⚙️ Tech Stack

- **Framework**: FastAPI
- **Database**: MongoDB Atlas
- **Async Driver**: Motor
- **Language**: Python 3.10+
- **Deployment**: Render (optional)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- A MongoDB Atlas cluster & connection URI

### 📦 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/<your-username>/hrone-backend-task.git
cd hrone-backend-task

## 🛠️ Setup Instructions

### ✅ Create a Virtual Environment and Activate It

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### Run app

```bash
uvicorn main:app --reload

### 🧾 Orders

#### ➕ Create Order  
**POST** `/orders/`

**Body:**
```json
{
  "user_id": "abc123",
  "products": ["prod1", "prod2"],
  "total_amount": 999.99,
  "status": "pending"
}

#### 📥 Get Orders for a User  
**GET** `/orders/{user_id}?limit=10&offset=0`

**Path Parameter:**
- `user_id` — ID of the user whose orders are to be fetched

**Query Parameters:**
- `limit` *(optional, default: 10)* — Number of orders to return
- `offset` *(optional, default: 0)* — Number of records to skip

**Response:** List of orders for the specified user

### 📦 Products

#### ➕ Create Product  
**POST** `/products/`

**Body:**
```json
{
  "name": "T-Shirt",
  "size": "M",
  "price": 499.99,
  "description": "Premium cotton tee"
}

#### 🔍 List Products  
**GET** `/products/?name=shirt&size=M&limit=10&offset=0`

**Query Parameters:**
- `name` *(optional)* — Filter products by name (case-insensitive)
- `size` *(optional)* — Filter products by size
- `limit` *(default: 10)* — Number of products to return
- `offset` *(default: 0)* — Number of records to skip

**Response:** List of matching products

