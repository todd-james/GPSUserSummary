# Snakefile 
# Summarize Raw GPS Pings
# Get User Attributes and Ping Counts
# James Todd - Jan '24 

import glob 
import os 
import re

# Environment Variables
envvars: 
    "rawdata_path"

# Parameters
yearmonths = [f"{x.split('/')[4]}" for x in glob.glob(f"{os.environ['rawdata_path']}/*/")]

def get_files_for_yearmonth(yearmonth):
    pattern = f"{os.environ['rawdata_path']}/{yearmonth}/*.csv"
    return glob.glob(pattern)

rule all: 
    input: 
        f"{os.environ['month_summary_path']}/uuid_summary_2122.csv"


# Get User Summaries for 1 month
for yearmonth in yearmonths: 
    files_for_yearmonth = get_files_for_yearmonth(yearmonth)

    rule: 
        name: 
            f"summarize_{yearmonth}"
        input: 
            files_for_yearmonth
        output: 
            f"{os.environ['month_summary_path']}/Monthly_Totals/{yearmonth}_uuid_summary.csv"
        shell: 
            "python process_month.py {output} {input}"


# Combine all montly summaries into one file
rule combine_all: 
    input: 
        expand(f"{os.environ['month_summary_path']}/{yearmonth}_uuid_summary.csv", yearmonth = yearmonths) 
    output: 
        f"{os.environ['month_summary_path']}/uuid_summary_2122.csv"
