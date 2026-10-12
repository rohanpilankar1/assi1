# Data Science Project

import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("Student Marks Dataset:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
