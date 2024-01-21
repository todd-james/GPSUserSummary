# Get summary of raw GPS ping locations by user
# Extract user attribues (uuid, os, home, work, gender, age) and number of pings
# James Todd - Jan '24 

import sys 
import pandas as pd 

def agg_file(input_files, output_file): 
    # Initialize an empty DataFrame
    summary = pd.DataFrame(columns=['uuid', 'os', 'home', 'work', 'gender', 'age', yrmnth])

    for input_file in input_files: 
        # Load in file 
        data = pd.read_csv(input_file,
                           header=None,
                           names=['uuid', 'unixtime', 'timestamp', 'lat', 'long','accuracy',
                                   'mesh', 'os', 'home', 'work', 'gender', 'age'])

        # Summarize data
        data = data.groupby(['uuid', 'os', 'home', 'work', 'gender', 'age'], dropna=False).size().reset_index(name=yrmnth)

        # Append data summary to summary
        summary = pd.concat([summary, data])
    
    summary.to_csv(output_file, header=True, index=False)


if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print("Useage: python month_summary.py output_file input_file1 input_file2 ... input_fileN")
        sys.exit(1)     

    output_file = sys.argv[1]
    input_files = sys.argv[2:]

    yrmnth = input_files[0].split('/')[4]

    agg_file(input_files, output_file)