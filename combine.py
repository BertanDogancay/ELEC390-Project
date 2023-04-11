import os
import pandas as pd

def combine_csv(directory):
    # Set the directory containing the files

    # Get a list of all the files in the directory
    file_list = os.listdir(directory)

    # Initialize an empty list to store the dataframes
    df_list = []

    # Loop through each file in the directory and append the dataframe to the list
    for file in file_list:
        if file.endswith('.csv'):  # Only consider csv files
            file_path = os.path.join(directory, file)
            df = pd.read_csv(file_path)
            if len(df_list) > 0:  # If this is not the first file
                df["Time (s)"] += df_list[-1]["Time (s)"].iloc[-1] + 1  # Add time offset
            df_list.append(df)

    # Concatenate all the dataframes in the list
    concatenated_df = pd.concat(df_list, ignore_index=True)

    # Add labels to the dataframe 0 for walk 1 for jump
    if 'walk' in directory:
        filename = 'walk_data.csv'
        concatenated_df['label'] = 0
    elif 'jump' in directory:
        filename = 'jump_data.csv'
        concatenated_df['label'] = 1
    elif 'data' in directory:
        filename = 'combined_data.csv'
    else:
        print('Something went wrong')

    # Export the concatenated dataframe as csv
    concatenated_df.to_csv('data\\'+filename, index=False)

combine_csv('raw_data\jump')
combine_csv('raw_data\walk')
combine_csv('data')