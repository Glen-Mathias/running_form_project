# utils/extract_angles.py
import cv2
import mediapipe as mp
import math
import pandas as pd
import os

mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = abs(radians * 180.0 / math.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def extract_user_form_angles(video_path):
    cap = cv2.VideoCapture(video_path)
    pose = mp_pose.Pose()
    frame_data = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark
            data = {
                'frame': frame_count,
                'left_knee_angle': calculate_angle(lm[mp_pose.PoseLandmark.LEFT_HIP], lm[mp_pose.PoseLandmark.LEFT_KNEE], lm[mp_pose.PoseLandmark.LEFT_ANKLE]),
                'right_knee_angle': calculate_angle(lm[mp_pose.PoseLandmark.RIGHT_HIP], lm[mp_pose.PoseLandmark.RIGHT_KNEE], lm[mp_pose.PoseLandmark.RIGHT_ANKLE]),
                'left_hip_angle': calculate_angle(lm[mp_pose.PoseLandmark.LEFT_SHOULDER], lm[mp_pose.PoseLandmark.LEFT_HIP], lm[mp_pose.PoseLandmark.LEFT_KNEE]),
                'right_hip_angle': calculate_angle(lm[mp_pose.PoseLandmark.RIGHT_SHOULDER], lm[mp_pose.PoseLandmark.RIGHT_HIP], lm[mp_pose.PoseLandmark.RIGHT_KNEE]),
                'left_elbow_angle': calculate_angle(lm[mp_pose.PoseLandmark.LEFT_SHOULDER], lm[mp_pose.PoseLandmark.LEFT_ELBOW], lm[mp_pose.PoseLandmark.LEFT_WRIST]),
                'right_elbow_angle': calculate_angle(lm[mp_pose.PoseLandmark.RIGHT_SHOULDER], lm[mp_pose.PoseLandmark.RIGHT_ELBOW], lm[mp_pose.PoseLandmark.RIGHT_WRIST]),
            }
            frame_data.append(data)

    cap.release()
    df = pd.DataFrame(frame_data)

    os.makedirs('output', exist_ok=True)
    output_csv_path = os.path.join('output', 'user_form_angles.csv')
    df.to_csv(output_csv_path, index=False)
    return output_csv_path
