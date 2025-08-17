#  CRUD API for Blog Posts with Proper Error Handling

A **RESTful Blog API** built using **Django REST Framework (DRF)** with **JWT authentication**.  
Users can register, log in, and manage blog posts securely.  

---

##  Tech Stack Used  
- **Backend:** Django, Django REST Framework (DRF)  
- **Authentication:** JWT (SimpleJWT)  
- **Database:** SQLite (default, can use PostgreSQL/MySQL)  
- **Language:** Python 3.x  

---

##  Setup & Run Instructions  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/blog-api.git
cd blog-api
```

### 2️⃣ Create a virtual environment & activate it  
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations  
```bash
python manage.py migrate
```

### 5️⃣ Start the development server  
```bash
python manage.py runserver
```

API will be available at: **http://127.0.0.1:8000/api/**  

---

##  API Endpoints & Sample Requests  

### 🔹 Register a User  
**POST** `/api/register/`  
Request:  
```json
{
  "username": "RajaArbab",
  "email": "rajaarbab@gmail.com",
  "password": "mypassword123"
}
```  
Response:  
```json
{
  "message": "User registered successfully!",
  "user": {
    "id": 1,
    "username": "RajaArbab",
    "email": "rajaarbab@gmail.com"
  }
}
```

---

### 🔹 Login (JWT Token)  
**POST** `/api/token/`  
Request:  
```json
{
  "username": "RajaArbab",
  "password": "mypassword123"
}
```  
Response:  
```json
{
  "refresh": "eyJhbGciOiJIUzI1...",
  "access": "eyJhbGciOiJIUzI1..."
}
```

---

### 🔹 Refresh Access Token  
**POST** `/api/token/refresh/`  
Request:  
```json
{
  "refresh": "eyJhbGciOiJIUzI1..."
}
```  
Response:  
```json
{
  "access": "eyJhbGciOiJIUzI1..."
}
```

---

### 🔹 Get All Posts  
**GET** `/api/posts/`  
Response:  
```json
[
  {
    "id": 1,
    "title": "First Post",
    "description": "This is my first blog post",
    "content": "Full content of the post...",
    "author": {
      "id": 1,
      "username": "RajaArbab",
      "email": "rajaarbab@gmail.com"
    },
    "created_at": "2025-08-16T10:20:30Z",
    "updated_at": "2025-08-16T10:20:30Z"
  }
]
```

---

### 🔹 Create a Post (Auth Required)  
**POST** `/api/posts/`  
Headers:  
```
Authorization: Bearer <access_token>
```  
Request:  
```json
{
  "title": "My Second Post",
  "description": "Short blog description",
  "content": "This is the detailed content of my second post."
}
```  
Response:  
```json
{
  "id": 2,
  "title": "My Second Post",
  "description": "Short blog description",
  "content": "This is the detailed content of my second post.",
  "author": {
    "id": 1,
    "username": "RajaArbab",
    "email": "rajaarbab@gmail.com"
  },
  "created_at": "2025-08-16T10:25:30Z",
  "updated_at": "2025-08-16T10:25:30Z"
}
```

---

##  Notes  
- **Authentication required** for creating, updating, or deleting posts.  
- Tokens must be included in headers for protected routes.  
