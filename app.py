from flask import Flask, render_template, request
import os
from utils.extract_angles import extract_user_form_angles
from utils.score_form import score_user_form

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video']
        if video:
            video_path = os.path.join(UPLOAD_FOLDER, video.filename)
            video.save(video_path)

            # 🧠 Step 1: Extract user joint angles
            user_csv_path = extract_user_form_angles(video_path)

            # 🧠 Step 2: Score against Usain Bolt's reference
            final_score, breakdown_html = score_user_form(
                user_csv_path=user_csv_path,
                reference_excel_path='ideal_data/usain_form.xlsx'
            )

            return render_template('index.html', score=final_score, breakdown=breakdown_html)

    return render_template('index.html', score=None)

if __name__ == '__main__':
    app.run(debug=True)
