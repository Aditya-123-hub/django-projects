# Django Portfolio Projects 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/django-5.2-green)](https://www.djangoproject.com/) 
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

Welcome! This repository showcases my **top 3 real-world Django projects**, demonstrating skills in backend development, real-time communication, and e-commerce platforms.

---

## 🔥 Projects Overview

### 1️⃣ SocialProject
**A fully functional social media platform with Django.**

**Features:**
- ✅ User Authentication: Signup, Login, Logout, Password Reset  
- ✅ CRUD Operations: Create, Read, Update, Delete posts  
- ✅ Likes & Comments: Engage with other users’ posts  
- ✅ User Profile: View and update profile information  
- ✅ Posts Feed: Browse all posts from all users  
- ✅ Responsive design for desktop and mobile

**Usage:**
1. Run Django server  
2. Sign up/login  
3. Create, edit, delete posts  
4. Like and comment on posts  
5. Explore other users’ posts in the feed

---

### 2️⃣ RealTimeChatApp
**Real-time chat application using Django Channels and WebSockets.**

**Features:**
- ✅ User Authentication: Signup, Login, Logout  
- ✅ Real-time messaging between users  
- ✅ Multiple chat rooms support  
- ✅ WebSocket implementation for live updates  
- ✅ User-friendly interface

**Usage:**
1. Run Django server with Channels configured  
2. Connect to chat rooms  
3. Send and receive messages instantly  
4. Explore multiple rooms for real-time communication

---

### 3️⃣ Multivendor E-commerce Platform
**A full-fledged multivendor platform with dashboard and analytics.**

**Features:**
- ✅ Robust User Authentication  
- ✅ CRUD operations for products: Create, Edit, Delete  
- ✅ Purchase and dashboard tracking for vendors and users  
- ✅ Analytics: Total sales, Daily sales, 7-day sales, 365-day sales  
- ✅ Payment integration (Instamojo, Razorpay – currently under maintenance)  
- ✅ Comprehensive user experience: My Purchases, My Dashboard, Manage Products  

**Note:** Payment integration is currently being fixed. All other features are fully functional.

**Usage:**
1. Run Django server  
2. Sign up/login as vendor or customer  
3. Create, manage, and browse products  
4. Track sales and analytics  
5. Payment integration will be fully functional after update

---

## 🗂 Project Structure

django-projects/ # Root folder
├── multivendorwebapp/ 
├── realtimechatapp/ 
├── socialproject/
└── .gitignore 
├── README.md 


---

## 💻 Installation

1. **Clone the repository**
git clone https://github.com/Aditya-123-hub/django-projects.git
cd django-projects

2. **Create & activate virtual environment**
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run migrations**
python manage.py migrate 

5. **Run serveer for any project**
cd socialproject        # or realtimechatapp / multivendor
python manage.py runserver

6. **Open in browser**
http://127.0.0.1:8000/


🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m "Added some feature"

Push to the branch: git push origin feature/YourFeature

Create a Pull Request


📜 License
This project is open-source and available under the MIT License.