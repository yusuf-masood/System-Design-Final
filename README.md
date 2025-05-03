# System-Design-Final
# 🎒 Lost & Found Management System for Campus

This is a backend implementation of a Lost & Found Management System for a university campus. It allows users to report lost and found items, stores them in a central database, and uses a simple matching engine to suggest potential matches. Users can also submit claims to reclaim their items.

---

## 🔧 Features Implemented (Partial Scope)

✅ JWT-based Authentication  
✅ Submit Lost Items  
✅ Submit Found Items  
✅ Match Engine (basic category match)  
✅ View All Matches  
✅ Submit Claims for Items  
✅ Role-based access using DRF permissions  

---

## 📂 Project Structure

LostAndFound/
├── backend/ # Django settings and URLs
├── api/ # Core app with models, views, serializers
├── venv/ # Virtual environment (ignored by Git)
├── manage.py # Django entry point
└── .gitignore # Git exclusions

yaml
Copy
Edit

---

## ⚙️ Tech Stack

- **Backend:** Django 5.x + Django REST Framework
- **Auth:** JWT (using `djangorestframework-simplejwt`)
- **Database:** SQLite (for demo; can be switched to PostgreSQL)
- **Tools:** Postman for API testing

---

## 🚀 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yusuf-masood/System-Design-Final
   cd lost-and-found
Create & activate virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations & start server

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
🔐 Authentication
Obtain JWT token using:

bash
Copy
Edit
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
Use Bearer <your-access-token> in Authorization headers for all protected requests.

🔄 API Endpoints Summary
Endpoint	Method	Description
/api/lost-items/	GET/POST	Submit or view lost items
/api/found-items/	GET/POST	Submit or view found items
/api/matches/	GET	View all matches
/api/claims/	GET/POST	Submit/view item claims
/api/match-engine/	POST	Trigger matching engine
/api/token/	POST	Get JWT tokens

📌 Notes
Matching logic is basic (category-based) for demo purposes.

Only ~30% of the full system is implemented as per system design scope.

Designed with scalability and modularity in mind (refer to design_document.pdf).

🧠 Future Improvements
Add image similarity or NLP-based matching

Admin claim approval dashboard

Notifications via email (SendGrid)

Frontend (React or Angular)

Detailed logging and analytics

---
**Created by:** Sayed Yusuf Masood  
_Kazakh-British Technical University_  
_Computer Science, 4th Year_  
📧 **Email:** yusuf.masood2001@gmail.com
