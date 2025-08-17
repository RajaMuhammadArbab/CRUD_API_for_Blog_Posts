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

## PROJECT-DEMO ##

## REGISTER ##
<img width="1393" height="676" alt="2" src="https://github.com/user-attachments/assets/69b3c1d6-3251-4dbc-9899-69fe6e630fc5" />

## LOGIN ##
<img width="1404" height="663" alt="3" src="https://github.com/user-attachments/assets/fec5c7e1-3647-4012-ba93-bbfe25814ad7" />

## CREATE 1 POST ##
<img width="1395" height="747" alt="4" src="https://github.com/user-attachments/assets/59e3666e-e00c-4c5a-a50e-12fa8132afaf" />

## CREATE 2 POST ##
<img width="1397" height="745" alt="5" src="https://github.com/user-attachments/assets/6ab82bf7-d86c-4b7c-a5a5-c514470a505e" />

## GET ALL THE POSTS ##
<img width="1397" height="877" alt="6" src="https://github.com/user-attachments/assets/6bced76b-0c43-4512-a0a5-5620a495b74e" />

## GET THE POST BY ITS ID ##
<img width="1409" height="749" alt="7" src="https://github.com/user-attachments/assets/fccba27f-5b61-4bc0-a880-8a3ca2bd86a7" />

## UPDATE THE POSTS ##
<img width="1398" height="768" alt="8" src="https://github.com/user-attachments/assets/5b2f98ef-8284-464c-8200-e508ca28e280" />

## DELETE THE POST ##
<img width="810" height="443" alt="9" src="https://github.com/user-attachments/assets/23cf1555-bcd8-4bfb-b941-6d582de64b84" />

## RESULT OF DELETED POST ##
<img width="1398" height="467" alt="10" src="https://github.com/user-attachments/assets/69257f54-be71-4e34-9f10-d21a621dd8fe" />
