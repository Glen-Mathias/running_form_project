import pandas as pd
import numpy as np

# Load CSVs
user_df = pd.read_csv("output/user_form_angles.csv")
usain_df = pd.read_excel("ideal_data/usain_form.xlsx")  # Usain's Excel

# Trim to minimum length
min_len = min(len(user_df), len(usain_df))
user_df = user_df.iloc[:min_len]
usain_df = usain_df.iloc[:min_len]

# Compute difference
angles = ['left_knee_angle', 'right_knee_angle', 'left_hip_angle',
          'right_hip_angle', 'left_elbow_angle', 'right_elbow_angle']

diff_df = pd.DataFrame()
diff_df['frame'] = user_df['frame']

for angle in angles:
    diff_df[angle + "_diff"] = abs(user_df[angle] - usain_df[angle])

# Calculate Mean Absolute Error
mae = diff_df[[col for col in diff_df.columns if "_diff" in col]].mean()
similarity_score = 100 - mae.mean()  # basic similarity %

# Save the differences
diff_df.to_csv("output/angle_differences.csv", index=False)

# Display result
print(f"✅ Comparison done! Similarity Score: {similarity_score:.2f}%")
if similarity_score > 85:
    print("🏃‍♂️ Great form! Almost like Usain Bolt! 🔥")
elif similarity_score > 70:
    print("👍 Good form, but there's room to improve.")
else:
    print("⚠️ Significant differences detected. Check the tips below.")

# Basic Tips (could be enhanced later)
for angle in angles:
    avg_diff = diff_df[angle + "_diff"].mean()
    if avg_diff > 15:
        print(f"🔧 Tip: Improve your {angle.replace('_', ' ')} — average deviation: {avg_diff:.2f}°")
