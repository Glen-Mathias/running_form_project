# 🏃‍♂️ Running Form Analysis Web App

A Flask-based web application that allows users to upload a running video and receive feedback on their running form by comparing it to an ideal pose reference. The app uses joint angle extraction and scoring techniques to analyze biomechanics and provide form similarity feedback.

---

## 🚀 Features

* Upload running videos via a simple web interface
* Extract joint angles from video frames
* Compare user form with ideal running form (CSV-based reference)
* Provide similarity scores and improvement tips
* Modular design with reusable utilities
* Easy to deploy locally or to platforms like Render

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **MediaPipe** 
* **Jinja2** (for HTML templating)

---

## 📦 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/running-form-project.git
cd running-form-project
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
python app.py
```

Visit `http://127.0.0.1:10000` in your browser.

---

## 🧪 Usage

1. Open the web app in your browser
2. Upload a running video
3. Wait for processing
4. View similarity score and feedback

---

## 🗂️ Folder Structure

```
├── app.py                # Main Flask app
├── compare_forms.py      # Compares user vs ideal pose
├── ideal_data/           # Ideal reference joint angles
├── output/               # Stores result outputs
├── static/uploads/       # Uploaded videos (for display)
├── templates/index.html  # Web UI
├── uploads/              # Temporary video uploads
├── utils/
│   ├── extract_angles.py # Extracts joint angles
│   └── score_form.py     # Scores user's form
├── requirements.txt      # Python dependencies
└── render.yaml           # Render deployment config
```

---

## 📝 Notes

* This app is intended for development/testing. For production use, configure a WSGI server like **Gunicorn** or **uWSGI**.
* Ensure pose estimation models (MediaPipe or OpenPose) are correctly placed if used.
* `uploads/` and `output/` directories may require write permissions.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss improvements.

