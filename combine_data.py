# Import Libraries 
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Read csv files
mat_data = pd.read_csv("student_mat.csv")
por_data = pd.read_csv("student_por.csv")

# Combine two csv files
final_df = pd.concat([mat_data, por_data])

# Save the combined DataFrame to a CSV file
final_df.to_csv("combined_student_data.csv", index=False)


