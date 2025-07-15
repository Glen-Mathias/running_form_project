
## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/running-form-project.git
cd running-form-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The app will be available at [http://127.0.0.1:10000](http://127.0.0.1:10000) by default.

## Usage

1. Open the web app in your browser.
2. Upload a running video.
3. Wait for processing and view the analysis and feedback.

## Notes

- This is a development server. For production, use a WSGI server like Gunicorn or uWSGI.
- Make sure you have the required pose estimation models in the correct directories if needed.
- Output and uploads folders may need write permissions.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Folder Structure 

├── app.py # Main Flask application
├── compare_forms.py # Script for comparing forms
├── ideal_data/ # Reference/ideal pose data
├── output/ # Stores output results
├── static/uploads/ # Uploaded video files
├── templates/index.html # Main HTML template
├── uploads/ # Temporary upload storage
├── utils/
│ ├── extract_angles.py # Angle extraction utilities
│ └── score_form.py # Scoring utilities
├── requirements.txt # Python dependencies
└── render.yaml # Deployment config (if using Render)
