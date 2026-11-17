# Student-Management-system
🎓 Student Management Application
A web application to manage student records, built with FastAPI, SQLite, and Jinja2 templates as part of my Full Stack Development training at Innomatics Research Labs.

✨ Features
Create – Add new students with details and a profile photo
Read – View all students in a clean, responsive table
Update – Edit existing student information
Delete – Remove records with a confirmation prompt
Live Search – Filter students by name or course instantly
Dashboard Stats – Total students, active students, and average marks
Marks Progress Bar – Quick visual view of each student's marks
Status Badges – Active / Inactive indicators
🛠️ Tech Stack
Layer	Technology
Backend	Python, FastAPI
Database	SQLite
Frontend	HTML, CSS, JavaScript, Jinja2
Server	Uvicorn
📁 Project Structure
Student-Management-Application/
├── main.py            # FastAPI app and routes
├── students.db        # SQLite database
├── templates/         # Jinja2 HTML templates
├── static/
│   └── uploads/       # Uploaded student photos
└── requirements.txt   # Python dependencies
🚀 Getting Started
1. Clone the repository
git clone https://github.com/elishababu-123/Student-Management-Application.git
cd Student-Management-Application
2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
3. Install dependencies
pip install fastapi uvicorn jinja2 python-multipart
4. Run the application
uvicorn main:app --reload
5. Open in your browser
http://127.0.0.1:8000
FastAPI's interactive API docs are available at http://127.0.0.1:8000/docs.

🔗 Main Routes
Method	Route	Description
GET	/	List all students
GET	/students/add	Add student form
GET	/student/{id}	View student details
GET	/student/edit/{id}	Edit student form
POST	/std/delete/{id}	Delete a student
🔮 Future Improvements
User login and authentication
Pagination for large datasets
Export student data to Excel/CSV
Deployment to a cloud platform
🙏 Acknowledgements
Thanks to Sai Balaji Sir, my trainer and mentor, and to Innomatics Research Labs and Full Stack Experts Academy for their guidance and support.

👩‍💻 Author
valiveti karthik GitHub: @valivetikarthik
