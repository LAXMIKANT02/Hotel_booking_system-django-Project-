
# 🏨 Hotel Booking Management System (Django)

A web-based **Hotel Booking Management System** built with **Django**, designed for users to browse hotels, check room availability, and make bookings. It includes a user-friendly admin panel for hotel managers to manage rooms, bookings, and customer details.

## 📌 Features

### 👤 User Side
- 🔍 Browse available hotels and rooms
- 🛏️ Book rooms with check-in/check-out dates
- 📄 View and manage your bookings
- 🔐 Secure login and registration

### 🛠️ Admin/Manager Side
- 🏨 Add, edit, and delete hotels & rooms
- 📅 View all bookings
- 📊 Dashboard for managing hotel listings and users

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Database:** SQLite3 (default for development)
- **Authentication:** Django's built-in user auth system

---

## 📁 Project Structure

```

hotelbooking/
│
├── booking/               # Main app
│   ├── templates/booking/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── hotelbooking/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3             # Database
├── manage.py
└── README.md

````

---

## 💻 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/hotelbooking.git
   cd hotelbooking
   ````

2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access in browser**

   ```
   http://127.0.0.1:8000/
   ```


## 📌 Future Enhancements

* [ ] Add payment gateway integration
* [ ] Add email/SMS notifications
* [ ] Room availability calendar
* [ ] Customer feedback system

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the project and submit a PR.

---

## 📄 License

Distributed under the MIT License.
See `LICENSE` for more information.

---

## 🙋‍♂️ Author

Developed by Laxmikant 
