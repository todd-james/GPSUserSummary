# Combine all monthly user summaries
# James Todd - Jan '24 

import sys
import pandas as pd

def combine_files(input_files, output_file):
    # Create an empty DataFrame to store the combined data
    combined_data = pd.DataFrame(columns=['uuid', 'os', 'home', 'work', 'gender', 'age'])

    # Loop through the input files
    for file in input_files:
        # Read each file into a DataFrame
        df = pd.read_csv(file)

        # Merge dataframes based on common columns ('uuid', 'os', 'home', 'work', 'gender', 'age')
        combined_data = pd.merge(combined_data, df, how='outer',
                                 on=['uuid', 'os', 'home', 'work', 'gender', 'age'])

    # Save the combined data to a new CSV file
    combined_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print("Useage: python combine_months.py output_file input_file1 input_file2 ... input_fileN")
        sys.exit(1)     

    output_file = sys.argv[1]
    input_files = sys.argv[2:]

    combine_files(input_files, output_file)