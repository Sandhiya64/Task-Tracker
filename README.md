# 📝 Flask Task Tracker

A simple yet extensible task tracker built with Flask. Easily add, edit, complete, archive, and manage your tasks.
A lightweight, extensible task management web application built with Flask. Designed to help users create, track, update, complete, and archive tasks with ease — all in a minimal UI powered by Python and Jinja templates.

---

## 🚀 Features

- 🔐 User-friendly interface for managing tasks
- 🗂️ Add, edit, delete tasks with title, description, due date, and priority
- ✅ Mark tasks as completed
- 📦 Archive completed tasks to keep active task list clean
- 📅 Due date tracking
- 🏷️ Priority labels
- 🔄 Real-time status updates
- 📁 SQLite for local persistent storage

---

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, Bootstrap, Jinja2
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)
- **Version Control**: Git + GitHub

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/sandhiyasethu/flask-task-tracker.git
   cd flask-task-tracker


### Create virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the app:

```bash
flask run
```

### Navigate:

Open [http://localhost:5000](http://localhost:5000) in your browser.

## 🔧 Project Structure

```
flask-task-tracker/
│
├── main.py
├── extensions.py
├── requirements.txt
├── task/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_task.html
│   ├── edit_task.html
│
└── static/           # Optional: CSS, JS, images
```

## 🧠 Future Enhancements

- User authentication (login/register)
- Tag-based categorization
- Search and filtering
- REST API with Flask-Restful
- Docker containerization
- PostgreSQL deployment

## 📄 License

This project is open-source under the MIT License.

## ✨ Author

**Sandhiya** — Engineer. Innovator. Future CEO.

🔗 [Portfolio](https://sandhiyaportfolio.netlify.app/)  
🔗 [GitHub](https://github.com/Sandhiya64)  
🔗 [LinkedIn](https://www.linkedin.com/in/sandhiya-shree-924a801b4/)
