import pandas as pd

def score_user_form(user_csv_path, reference_excel_path):
    # Read user and reference data
    user_df = pd.read_csv(user_csv_path)
    ref_df = pd.read_excel(reference_excel_path)

    # Calculate average values for each column (joint angles)
    user_avg = user_df.mean()
    ref_avg = ref_df.mean()

    joint_names = [
        'left_knee_angle', 'right_knee_angle',
        'left_hip_angle', 'right_hip_angle',
        'left_elbow_angle', 'right_elbow_angle'
    ]

    max_score = 100
    threshold = 10
    output_lines = []
    joint_scores = []

    for joint in joint_names:
        your_avg = user_avg[joint]
        ref_avg_joint = ref_avg[joint]
        diff = abs(your_avg - ref_avg_joint)

        # Apply penalties differently based on joint type
        if 'knee' in joint:
            penalty = max(0, (diff - threshold) / (50 * 0.4))
        elif 'elbow' in joint:
            penalty = max(0, (diff - threshold) / (50 * 0.6))
        else:
            penalty = max(0, (diff - threshold) / 50)

        score = max_score * (1 - penalty)
        score = max(score, 0)  # Ensure score doesn't go below 0
        joint_scores.append(score)

        # Build detailed score breakdown in HTML
        output_lines.append(
            f"<b>{joint}:</b><br>"
            f"&nbsp;&nbsp;▶ Your Avg: {your_avg:.2f}°<br>"
            f"&nbsp;&nbsp;▶ Ref Avg:  {ref_avg_joint:.2f}°<br>"
            f"&nbsp;&nbsp;▶ Difference: {diff:.2f}° → Score: {score:.2f}/100<br><br>"
        )

    # Calculate final average score safely
    if joint_scores:
        final_score = sum(joint_scores) / len(joint_scores)
    else:
        final_score = 0.0

    # Append final score with 2 decimal places
    output_lines.append(
        f"<h3>🏁 Final Form Similarity Score: <b>{final_score:.2f}/100</b></h3>"
    )

    html_output = "\n".join(output_lines)
    return final_score, html_output
