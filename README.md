# 💰 Personal Finance Tracker API

A REST API backend for tracking personal income, expenses, budgets, and generating financial summaries — built with Django REST Framework, PostgreSQL (Neon), and JWT authentication.

🔗 **Live API:** https://expense-tracker-api-8zx7.onrender.com

---

## 🚀 Features

- 🔐 JWT-based user authentication (Register/Login)
- 💵 Add and track income & expense transactions
- 📊 Monthly financial summary with category breakdown
- 🎯 Set budget limits per category
- 🚨 Real-time alerts when budget is exceeded or nearing limit

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL (hosted on Neon)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Deployment:** Render
- **API Testing:** Postman

---

## 📋 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|--------------|----------------|
| POST | `/api/auth/register/` | Register a new user | ❌ |
| POST | `/api/auth/login/` | Login and get JWT token | ❌ |
| POST | `/api/auth/refresh/` | Refresh access token | ❌ |
| POST | `/api/transactions/` | Add income/expense | ✅ |
| GET | `/api/transactions/` | List transactions (with filters) | ✅ |
| GET | `/api/summary/monthly/` | Get monthly financial summary | ✅ |
| POST | `/api/budgets/` | Set a budget limit | ✅ |
| GET | `/api/budgets/` | List all budgets | ✅ |

---

## 🔧 Local Setup

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/Navyaam91/expense_tracker_api

cd finance-tracker-api
\`\`\`

### 2. Create virtual environment
\`\`\`bash
python -m venv venv
venv\\Scripts\\activate  # Windows
\`\`\`

### 3. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Create `.env` file
\`\`\`env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-postgresql-connection-string
\`\`\`

### 5. Run migrations
\`\`\`bash
python manage.py migrate
\`\`\`

### 6. Start server
\`\`\`bash
python manage.py runserver
\`\`\`

---

## 📬 API Usage Examples

### Register
\`\`\`json
POST /api/auth/register/
{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepass123"
}
\`\`\`

### Login
\`\`\`json
POST /api/auth/login/
{
    "email": "user@example.com",
    "password": "securepass123"
}
\`\`\`

### Add Transaction
\`\`\`json
POST /api/transactions/
Authorization: Bearer <token>

{
    "type": "expense",
    "category": "food",
    "amount": 500.00,
    "description": "Lunch",
    "date": "2026-06-22"
}
\`\`\`

### Set Budget
\`\`\`json
POST /api/budgets/
Authorization: Bearer <token>

{
    "category": "food",
    "limit": 5000.00,
    "month": 6,
    "year": 2026
}
\`\`\`

---

## 📦 Postman Collection

Import \`finance-tracker.postman_collection.json\` into Postman to test all endpoints quickly.

---

## 👤 Author
## 👤 Author

Built by Navya as a backend portfolio project.

🔗 GitHub: [@Navyaam91](https://github.com/Navyaam91)

---

## 📄 License

This project is open source and available under the MIT License.