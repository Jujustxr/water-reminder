
# 💧 Water Reminder

A simple **drinking water reminder web application** built with **Python (Flask)**.  
This project helps users stay hydrated by setting reminders to drink water, complete with notifications and sound alerts.  
This is a little web application that I created for my college project. Feel free to use.  

---

## 📋 Features

- 🕒 Set custom reminders for drinking water  
- 🔔 Audio notifications when it’s time  
- 📜 Reminder history tracking (optional)  
- 🌐 Web-based interface with Flask  
- 🎨 HTML templates + static assets (images, CSS, audio)  

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask  
- **Frontend:** HTML, CSS, JavaScript (via `templates/` and `static/`)  
- **Environment:** Virtualenv (`venv`)  

---

## 📂 Project Structure

```bash
waterreminder/
├── static/             # Static assets (images, CSS, audio, etc.)
├── templates/          # HTML templates (e.g., index.html)
├── venv/               # Virtual environment (ignored in git)
├── app.py              # Main Flask app
├── reminder_checker.py # Reminder logic in Python
├── tes_pyqt5.py        # (Optional) Experimental PyQt5 version
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
````
---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Jujustxr/water-reminder.git
cd waterreminder
````

### 2. Create and activate virtual environment

```bash
# Create venv
python -m venv venv
# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Linux/Mac)
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

The app will start on:

```
http://127.0.0.1:5000
```

---

## 📜 requirements.txt

You can generate it by:

```bash
pip freeze > requirements.txt
```

Typical contents might look like:

```
Flask==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
Werkzeug==3.0.3
```

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m "Add NewFeature"`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License.
See `LICENSE` for more information.

---

⭐ **Don’t forget to give a star if this project helps you stay hydrated!** ⭐
