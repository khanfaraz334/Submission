import pandas as pd

file_path = 'dataset-3.csv'

# Read the dataset into a DataFrame
df3= pd.read_csv(file_path)

# Display the DataFrame or perform operations as needed
print(df3.head())  # Display the first few rows of the DataFrame

#1
def calculate_distance_matrix(df3)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
     # Get unique IDs
    unique_ids = sorted(list(set(df3['id_start']) | set(df3['id_end'])))
    
    # Initialize distance matrix with infinity values
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    distance_matrix = distance_matrix.fillna(float('inf'))
    
    # Set diagonal values to 0
    for idx in unique_ids:
        distance_matrix.at[idx, idx] = 0
    
    # Populate distance matrix with given distances
    for index, row in df3.iterrows():
        from_id = row['id_start']
        to_id = row['id_end']
        distance = row['distance']
        
        # Update distance_matrix with bidirectional distances
        distance_matrix.at[from_id, to_id] = distance
        distance_matrix.at[to_id, from_id] = distance
    
    # Calculate cumulative distances for indirect routes
    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                if distance_matrix.loc[i, k] + distance_matrix.loc[k, j] < distance_matrix.loc[i, j]:
                    distance_matrix.loc[i, j] = distance_matrix.loc[i, k] + distance_matrix.loc[k, j]
    
    return distance_matrix
   
result_matrix = calculate_distance_matrix(df3)

# Print the resulting distance matrix
print(result_matrix)

#2
def unroll_distance_matrix(result_matrix)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    ids = result_matrix.index
    
    # Initialize lists to store unrolled data
    id_starts = []
    id_ends = []
    distances = []
    
    # Iterate over the IDs to create combinations and extract distances
    for start_id in ids:
        for end_id in ids:
            # Skip if start and end IDs are the same
            if start_id != end_id:
                id_starts.append(start_id)
                id_ends.append(end_id)
                distances.append(result_matrix.loc[start_id, end_id])
    
    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame({
        'id_start': id_starts,
        'id_end': id_ends,
        'distance': distances
    })
    
    return unrolled_df
unrolled_distances = unroll_distance_matrix(result_matrix)

# Print the resulting unrolled DataFrame
print(unrolled_distances)

#3
def find_ids_within_ten_percentage_threshold(unrolled_distances, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    # Calculate average distance for the reference value
    avg_distance = unrolled_distances[unrolled_distances['id_start'] == reference_id]['distance'].mean()

    # Calculate the threshold values
    lower_threshold = avg_distance * 0.9  # 10% below the average
    upper_threshold = avg_distance * 1.1  # 10% above the average

    # Filter IDs within the threshold
    within_threshold = unrolled_distances[
        (unrolled_distances['distance'] >= lower_threshold) &
        (unrolled_distances['distance'] <= upper_threshold)
    ]['id_start'].tolist()

    # Sort the IDs and return
    return sorted(within_threshold)

result = find_ids_within_ten_percentage_threshold(unrolled_distances, 1001400)
print("IDs within 10% threshold of reference value's average distance:", result)


#4
def calculate_toll_rate(unrolled_distances)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    # Adding columns for each vehicle type with their respective rate coefficients
    unrolled_distances['moto'] = unrolled_distances['distance'] * 0.8
    unrolled_distances['car'] = unrolled_distances['distance'] * 1.2
    unrolled_distances['rv'] = unrolled_distances['distance'] * 1.5
    unrolled_distances['bus'] = unrolled_distances['distance'] * 2.2
    unrolled_distances['truck'] = unrolled_distances['distance'] * 3.6

    return unrolled_distances


result_df = calculate_toll_rate(unrolled_distances)
print(result_df)

    

#5
def calculate_time_based_toll_rates(result)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    