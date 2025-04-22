import pandas as pd

# Create a dictionary with some data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Select a specific column
print("\nAges of all individuals:")
print(df['Age'])

# Filter rows based on a condition
print("\nIndividuals older than 30:")
print(df[df['Age'] > 30])

# Add a new column
df['Occupation'] = ['Engineer', 'Doctor', 'Artist', 'Teacher']
print("\nDataFrame with a new column added:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print(f"\nThe average age is: {average_age:.2f}")

print("Execution Completed")
