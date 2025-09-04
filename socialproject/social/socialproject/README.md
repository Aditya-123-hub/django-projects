# SocialProject
A fully functional **social media platform** built with Django.  
Users can sign up, login, create posts, like, comment, and manage their profile.

---

## 🔥 Features

- **User Authentication:** Signup, login, logout, password reset.
- **CRUD Operations:** Create, read, update, delete posts.
- **Likes & Comments:** Users can like posts and add comments.
- **User Profile:** View and update profile information.
- **Posts Feed:** View all posts by all users in a feed.
- **Responsive Design:** Works on desktop and mobile (if templates are responsive).

---

## 🗂 Project Structure

social/                 # Root folder (jo tu GitHub pe push karega)
├── env/                # Virtual environment (isse push nahi karna)
├── socialproject/      # Django project folder (settings, urls, wsgi, asgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── posts/              # App for handling posts
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── users/              # App for user management
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
├── manage.py           # Django management script
├── requirements.txt
├── structue.txt
├── .gitignore
└── README.md



---

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/socialproject.git
cd socialproject

2. **Create Virtual environment**
python -m venv env
# Linux/Mac
source env/bin/activate
# Windows
env\Scripts\activate

3. **Install depedencies**
pip install -r requirements.txt

4. **Make migrations**
python manage.py migrate

5. **Run the server**
python manage.py runserver

6. **Open in browser**
http://127.0.0.1:8000/


🚀 Usage

Signup or login as a user.

Create, edit, delete posts.

Like and comment on posts.

Update profile information.

Explore other users' posts in the feed.


🤝 Contributing

Fork the repository

Create a feature branch: git checkout -b feature/YourFeature

Commit changes: git commit -m "Added some feature"

Push to the branch: git push origin feature/YourFeature

Create a Pull Request



