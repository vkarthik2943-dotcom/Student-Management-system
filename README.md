# 🎓 Student Management System

A web-based **Student Management System** developed using Python, FastAPI, SQLite, and Jinja2 templates. This application helps manage student records efficiently through a simple and user-friendly interface.

This project was developed as part of my Full Stack Development learning journey.

## 🚀 Features

- **Add Students** – Register new students with their personal and academic details.
- **View Students** – Display all registered student records.
- **Student Details** – View individual student information.
- **Update Students** – Edit existing student information.
- **Delete Students** – Remove student records from the database.
- **Form Validation** – Validate student information using Pydantic.
- **Database Integration** – Store and manage student records using SQLite.
- **Dynamic Web Pages** – Render HTML pages using Jinja2 templates.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLite | Database |
| HTML5 | Web Page Structure |
| CSS3 | Styling |
| JavaScript | Frontend Interactivity |
| Jinja2 | HTML Templates |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Git & GitHub | Version Control |

## 📂 Project Structure

```text
Student-Management-system/
│
├── practice/
│
├── templates-1/
│   ├── home.html
│   ├── add-std.html
│   ├── single_std.html
│   └── update.html
│
├── p1.py
├── p2.py
├── requirements.txt
├── students.db
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vkarthik2943-dotcom/Student-Management-system.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn p1:app --reload
```

### 7. Open in Browser

Application:

```text
http://127.0.0.1:8000
```

FastAPI Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔗 Application Routes

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display all students |
| GET | `/students/add` | Open student registration form |
| POST | `/students/add` | Add a new student |
| GET | `/students/{std_id}` | View individual student details |
| GET | `/students/edit/{std_id}` | Open student edit form |
| POST | `/students/edit/{std_id}` | Update student information |
| POST | `/std/delete/{std_id}` | Delete a student |

## 🗄️ Database

This project uses SQLite to store student information.

The student table contains the following fields:

- ID
- Name
- Age
- Gender
- Marks
- Course
- Image
- Status

The database table is created automatically when the application starts.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building RESTful routes using FastAPI.
- Working with SQLite databases.
- Performing CRUD operations.
- Connecting Python backend with HTML templates.
- Using Jinja2 for dynamic web pages.
- Validating data using Pydantic.
- Handling HTML form submissions.
- Managing projects using Git and GitHub.

## 🔮 Future Enhancements

- User authentication and authorization.
- Student search and filtering.
- Pagination.
- Student data export to Excel and PDF.
- Dashboard analytics.
- Cloud deployment.

## 👨‍💻 Author

**Valiveti Karthik**

- GitHub: [@vkarthik2943-dotcom](https://github.com/vkarthik2943-dotcom)
- Project Repository: [Student Management System](https://github.com/vkarthik2943-dotcom/Student-Management-system)

---

⭐ If you find this project useful, feel free to explore the repository!

**Thank you for visiting my project!**
