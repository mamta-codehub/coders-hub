Coder’s Hub is a web-based platform built using Python Django that connects coders and companies on a centralized portal. It allows coders to showcase their skills and download PDF résumés, while companies can post job openings, search developers, and contact relevant candidates. A custom admin panel is provided to manage users, reports, and verification activities.

🔑 Key Features
👤 User Roles: Coders, Companies, and Admin

📄 PDF Export: Generate coder profiles as downloadable PDFs using xhtml2pdf

🔎 Search & Filter: Find coders by skills, location, or experience

🏢 Company Dashboard: Post and manage job vacancies

🛡️ Admin Panel: Approve users, export reports, monitor site usage

📂 File Uploads: Users can upload profile pictures, documents, and résumés

🛠️ Built With
Backend: Django 4.x, MySQL

Frontend: HTML5, Bootstrap 5, jQuery

PDF Engine: xhtml2pdf

Tools: Virtualenv, Git

🚀 How to Run the Project
Clone the repo:
git clone https://github.com/mamta-codehub/coders-hub.git

Create a virtual environment:
python -m venv code

Activate the virtual environment:
.\code\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Run the server:
python manage.py runserver
