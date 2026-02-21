# 🚀 Django Projects Portfolio

This repository contains three Django-based projects showcasing backend development, real-time communication, and e-commerce platform design.

---

## 🔥 Projects Overview

### 1️⃣ SocialProject  
A social media platform built with Django.

**Features**

✅ User Authentication (Signup, Login, Logout, Password Reset)  
✅ CRUD Operations for Posts  
✅ Likes & Comments System  
✅ User Profile Management  
✅ Global Posts Feed  
✅ Responsive UI  

**Usage**

- Run Django server  
- Sign up / log in  
- Create, edit, delete posts  
- Like & comment on posts  

---

### 2️⃣ RealTimeChatApp  
Real-time chat application using Django Channels & WebSockets.

**Features**

✅ User Authentication  
✅ Real-time Messaging  
✅ Multiple Chat Rooms  
✅ WebSocket-based Live Updates  
✅ Interactive UI  

**Usage**

- Run Django server with Channels configured  
- Join chat rooms  
- Send & receive messages instantly  

---

### 3️⃣ Multivendor E-commerce Platform  
A multivendor e-commerce platform with dashboards and analytics.

**Features**

✅ Authentication System  
✅ Product CRUD (Create/Edit/Delete)  
✅ Vendor & Customer Dashboards  
✅ Sales Analytics (Daily / Weekly / Yearly)  
✅ Razorpay & Instamojo Integration *(under maintenance)*  

**Note**

Payment integration is currently being updated. All other features are fully functional.

**Usage**

- Run Django server  
- Login as Vendor / Customer  
- Manage & browse products  
- Track analytics  

---

## 🗂 Repository Structure

django-projects/
├── multivendorwebapp/
├── realtimechatapp/
├── socialproject/
├── requirements.txt
└── README.md

---

## 💻 Installation

### 1️⃣ Clone Repository

git clone https://github.com/Aditya-123-hub/django-projects.git  
cd django-projects

---

### 2️⃣ Create Virtual Environment

python -m venv env

**Activate Environment**

Windows:
env\Scripts\activate  

Linux/Mac:
source env/bin/activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶ Running a Project

Navigate into the desired project folder:

cd socialproject  
python manage.py migrate  
python manage.py runserver  

OR

cd realtimechatapp  
python manage.py migrate  
python manage.py runserver  

OR

cd multivendorwebapp  
python manage.py migrate  
python manage.py runserver  

---

## 🌐 Access Application

http://127.0.0.1:8000/

---

## 🚀 Deployment Status

Currently configured for local development.  
Deployment setup is in progress.

---

## 🤝 Contributing

Fork the repository  
Create a feature branch  
Commit changes  
Open Pull Request  

---

## 📜 License

MIT License
