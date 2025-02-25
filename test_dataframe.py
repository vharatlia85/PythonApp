import pytest
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

@pytest.fixture
def dataframe():
    return pd.DataFrame(data)

def test_dataframe_creation(dataframe):
    # Check if DataFrame is created correctly
    assert list(dataframe.columns) == ['Name', 'Age', 'City']
    assert len(dataframe) == 4

def test_select_column(dataframe):
    # Check if Age column is selected correctly
    ages = dataframe['Age']
    assert ages.tolist() == [25, 30, 35, 40]

def test_filter_rows(dataframe):
    # Check if filtering rows works correctly
    filtered_df = dataframe[dataframe['Age'] > 30]
    assert filtered_df['Name'].tolist() == ['Charlie', 'David']
    assert filtered_df['Age'].tolist() == [35, 40]

def test_add_column(dataframe):
    # Add a new column and check if it's added correctly
    dataframe['Occupation'] = ['Engineer', 'Doctor', 'Artist', 'Teacher']
    assert list(dataframe.columns) == ['Name', 'Age', 'City', 'Occupation']
    assert dataframe['Occupation'].tolist() == ['Engineer', 'Doctor', 'Artist', 'Teacher']

def test_average_age(dataframe):
    # Calculate and check the average age
    average_age = dataframe['Age'].mean()
    assert average_age == 32.5
