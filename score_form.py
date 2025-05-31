import pandas as pd

def score_based_on_angle_differences(comparison_df, threshold=10):
    score_components = []
    max_score = 100

    print("🔍 Joint-wise Breakdown:\n")
    for joint, row in comparison_df.iterrows():
        diff = abs(row['Difference'])

        if 'knee' in joint:
            penalty = max(0, (diff - threshold) / (50 * 0.4))  # stricter
        elif 'elbow' in joint:
            penalty = max(0, (diff - threshold) / (50 * 0.6))  # milder
        else:
            penalty = max(0, (diff - threshold) / 50)

        joint_score = max_score * (1 - penalty)
        joint_score = max(joint_score, 0)

        score_components.append(joint_score)

        print(f"{joint}:")
        print(f"  ▶ Your Avg: {row['Your_Avg_Angle']:.2f}°")
        print(f"  ▶ Ref Avg:  {row['Reference_Avg_Angle']:.2f}°")
        print(f"  ▶ Difference: {diff:.2f}° → Score: {joint_score:.2f}/100\n")

    avg_score = sum(score_components) / len(score_components)
    print(f"🏁 Final Form Similarity Score: **{avg_score:.2f}/100**")
    return avg_score

# Load your user and reference (Usain) data
user_df = pd.read_csv("output/user_form_angles.csv")
usain_df = pd.read_excel("ideal_data/usain_form.xlsx")

# Align frame count
min_len = min(len(user_df), len(usain_df))
user_df = user_df.iloc[:min_len]
usain_df = usain_df.iloc[:min_len]

# Compute average per joint
angles = ['left_knee_angle', 'right_knee_angle', 'left_hip_angle',
          'right_hip_angle', 'left_elbow_angle', 'right_elbow_angle']

data = {
    'Joint': [],
    'Your_Avg_Angle': [],
    'Reference_Avg_Angle': [],
    'Difference': []
}

for angle in angles:
    your_avg = user_df[angle].mean()
    ref_avg = usain_df[angle].mean()
    diff = abs(your_avg - ref_avg)

    data['Joint'].append(angle)
    data['Your_Avg_Angle'].append(your_avg)
    data['Reference_Avg_Angle'].append(ref_avg)
    data['Difference'].append(diff)

comparison_df = pd.DataFrame(data).set_index("Joint")

# Score using your custom method
score_based_on_angle_differences(comparison_df)
