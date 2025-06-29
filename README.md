# ⚖️ Bail Reckoner

**Bail Reckoner** is a law-tech web platform built using Django to streamline the bail application process. It is designed to help legal professionals, judicial authorities, and individuals understand bail eligibility and generate bail recommendations based on legal parameters. The project incorporates user management, legal logic, and admin control, providing an accessible and user-friendly interface.


## 🌟 About

Bail Reckoner simplifies the judicial workflow with:
- Rule-based bail recommendation system based on IPC/CrPC sections.
- Smart bail eligibility analysis with categorized case inputs.
- User-friendly authentication and dashboard interface.
- Admin control for managing users, rules, and cases.
- Legal-themed UI for a professional and thematic feel.

## ✅ Features

- 🔐 User Authentication (Signup, Login, Logout)  
- 🧾 Bail Recommendation System (Rule-Based Logic)  
- 📋 Case Details Form with Categorized Input (Cognizable, Non-Cognizable, etc.)  
- 🧑‍⚖️ Admin Panel for User & Case Management  
- 🎨 Legal Themed UI Design  
- 📩 Contact Form with Email Functionality via Gmail SMTP  
- 📊 Dashboard for Viewing Case Results  
- 🗃️ Case History Management  
- 🧠 Scalable for Machine Learning/AI-based Legal Predictions

## 🛠️ Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap, JavaScript (Legal-themed UI)  
- **Database:** SQLite (Default)  
- **Email:** Gmail SMTP for Contact Form  
- **Hosting:** Localhost / Deployment Ready  


## 📂 Project Structure

bail_reckoner/
├── bailapp/
│ ├── templates/
│ ├── static/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── media/
├── db.sqlite3
├── manage.py
└── ...


## 🎯 Screenshots

### 🏠 Home Page

![Home](https://github.com/user-attachments/assets/legal-theme-homepage.png)

### 🔐 Login Page

![Login](https://github.com/user-attachments/assets/legal-theme-login.png)

### 📝 Signup Page

![Signup](https://github.com/user-attachments/assets/legal-theme-signup.png)

### 📄 Case Form Page

![Case Form](https://github.com/user-attachments/assets/legal-theme-case-form.png)

### 📊 Case Result Page

![Result](https://github.com/user-attachments/assets/legal-theme-result.png)

### 📧 Contact Form (Email Integrated)

![Contact](https://github.com/user-attachments/assets/legal-theme-contact.png)


## 📧 Email Configuration (Gmail SMTP)

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'


