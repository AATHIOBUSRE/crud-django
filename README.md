# 🗂️ Contact Management Application (CRUD) - Django

This is a web-based **Contact Management Application** built using the **Django web framework**. It allows users to Create, Read, Update, and Delete (CRUD) contact information.

---

## 🛠️ Tech Stack Used

- **Backend**: Python (Django)
- **Frontend**: HTML5, Bootstrap 5, Django Templating
- **Database**: SQLite (default)
- **Form Rendering**: Django ModelForms with Crispy Forms

---

## 📦 Features

- Add a new contact with the following fields:
  - First Name
  - Last Name
  - Address
  - Email ID (validated)
  - Phone Number
- View the list of all contacts
- Edit an existing contact
- Delete a contact
- Email validation & form error handling
- Responsive UI with Bootstrap 5 styling

---

## 🚀 How to Run This Project

**Step-by-step instructions:**

```bash
# 1. Clone the repository (or download ZIP)
[git clone https://github.com/your-username/crud-django.git](https://github.com/AATHIOBUSRE/crud-django/
cd crud-django

# 2. Activate environment (if using Anaconda)
conda activate base

# 3. Install required packages
pip install django
pip install django-crispy-forms

# 4. Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run the server
python manage.py runserver

# 6. Open in browser
Visit: http://127.0.0.1:8000

