import pandas as pd


file_path = 'dataset-1.csv'

# Read the dataset into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame or perform operations as needed
print(df.head())  # Display the first few rows of the DataFrame

#1
def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    # Pivot the DataFrame to create the matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    
    # Set diagonal values to 0
    for col in car_matrix.columns:
        car_matrix.loc[col, col] = 0
    
    return car_matrix
    
# Generate the car matrix
result_matrix = generate_car_matrix(df)
print(result_matrix)

#2
def categorize_car_type(value):
    if value <= 15:
        return 'low'
    elif 15 < value <= 25:
        return 'medium'
    else:
        return 'high'
    
def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df['car_type'] = df['car'].apply(categorize_car_type)
    type_counts = df['car_type'].value_counts().to_dict()
    sorted_counts = dict(sorted(type_counts.items()))
    return sorted_counts

result = get_type_count(df)
print(result)
   
#3
def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    mean_bus = df['bus'].mean()
    selected_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    return sorted(selected_indexes)

result = get_bus_indexes(df)
print(result)

#4
def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    routes_above_7 = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()
    return sorted(routes_above_7)

result = filter_routes(df)
print(result)

#5
def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_matrix = matrix.copy()  # Make a copy of the input DataFrame
    
    for i in range(len(modified_matrix)):
        for j in range(len(modified_matrix.columns)):
            value = modified_matrix.iloc[i, j]
            if value > 20:
                modified_matrix.iloc[i, j] = value * 0.75
            else:
                modified_matrix.iloc[i, j] = value * 1.25
    
    return modified_matrix

modified_result = multiply_matrix(result_matrix)
print(modified_result)

#6
# Read the dataset into a DataFrame

file_path = 'dataset-2.csv'
df1= pd.read_csv(file_path)

# Display the DataFrame or perform operations as needed
print(df1.head())  # Display the first few rows of the DataFrame

def time_check(df1)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
     # Convert timestamp column to datetime format
   #df1['timestamp'] = pd.to_datetime(df1['timestamp'])

    # Extract day of the week and hour from timestamp
    #df1['day_of_week'] = df1['timestamp'].dt.day_name()
    #df1['hour'] = df1['timestamp'].dt.hour

    # Group by (id, id_2) pairs
    
    #grouped = df1.groupby(['id', 'id_2'])

    # Check for completeness of time data
    #completeness_check = grouped.apply(lambda x: (
       # x['day_of_week'].nunique() == 7 and
        #x['hour'].nunique() == 24
   # ))

    #return completeness_check


# Call the function and get the boolean series indicating incorrect timestamps
#result = time_check(df1)
