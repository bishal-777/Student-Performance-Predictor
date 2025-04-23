import pandas as pd

# Load your updated CSV
df = pd.read_csv("abc.csv")

# Reorder the columns
column_order = [
    "Name", "Attendance (%)", "Study Hours/Week", "Previous Score",
    "Extracurricular Activities", "Final Score"
]
df = df[column_order]

# Save the reordered dataset
df.to_csv("final.csv", index=False)
