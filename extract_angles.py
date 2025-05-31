import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import os

def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba, bc = a - b, c - b
    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine, -1.0, 1.0))
    return np.degrees(angle)

def extract_joint_angles(video_path, output_csv="output/user_form_angles.csv"):
    print(f"🔍 Processing video: {video_path}")
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, model_complexity=2)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ ERROR: Could not open video: {video_path}")
        return

    frame_angles = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark
            get = lambda name: [lm[mp_pose.PoseLandmark[name].value].x,
                                lm[mp_pose.PoseLandmark[name].value].y]

            try:
                angles = {
                    "frame": frame_count,
                    "left_knee_angle": calculate_angle(get("LEFT_HIP"), get("LEFT_KNEE"), get("LEFT_ANKLE")),
                    "right_knee_angle": calculate_angle(get("RIGHT_HIP"), get("RIGHT_KNEE"), get("RIGHT_ANKLE")),
                    "left_hip_angle": calculate_angle(get("LEFT_SHOULDER"), get("LEFT_HIP"), get("LEFT_KNEE")),
                    "right_hip_angle": calculate_angle(get("RIGHT_SHOULDER"), get("RIGHT_HIP"), get("RIGHT_KNEE")),
                    "left_elbow_angle": calculate_angle(get("LEFT_SHOULDER"), get("LEFT_ELBOW"), get("LEFT_WRIST")),
                    "right_elbow_angle": calculate_angle(get("RIGHT_SHOULDER"), get("RIGHT_ELBOW"), get("RIGHT_WRIST")),
                }
                frame_angles.append(angles)
            except Exception as e:
                print(f"⚠️ Error calculating angles on frame {frame_count}: {e}")

        frame_count += 1

    cap.release()

    if frame_angles:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        df = pd.DataFrame(frame_angles)
        df.to_csv(output_csv, index=False)
        print(f"✅ Done! Angles saved to: {output_csv}")
    else:
        print("❌ No pose landmarks detected. Nothing saved.")

# ----------- ✅ MAIN CALL ----------- #
if __name__ == "__main__":
    input_video_path = "static/uploads/user_run.mp4"
    extract_joint_angles(input_video_path)
