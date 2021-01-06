from gbf_cleaner import clean_file
from gbf_turn_formatter import tabulate
from gbf_pandas import get_statistics
import sys
import os
import re
"""
Argument(s): 1. The directory path of the fight's JSON data
Output: No return output. It will print out the results from calling get_statistics from gbf_pandas.py

Details: 
This program only handles gathering the filepaths and calling other functions. 
    Sorted Files
        |
        V
    gbf_cleaner.py
        |
        V
    gbf_turn_formatter.py
        |
        V
    gbf_pandas.py
        |
        V
    print()
    
Assumptions:
There is an assumption that the files names are the number of their order. The regex matcher name_filter will handle the ordering
"""
name_filter = r'(\d+).txt'

def getNum(name):
    test = int(re.match(name_filter, name).group(1))
    return test

def main():
    data_list = []
    json_data_dir = sys.argv[1]
    files = [name for name in os.listdir (json_data_dir)]
    sorted_files = sorted(files, key=lambda x: getNum(x))
    for file in sorted_files:
        cleaned_data = clean_file(json_data_dir+file)
        if cleaned_data != "":
            data_list.append(cleaned_data)

    arr = tabulate(data_list)
    print(get_statistics(arr))
        
if __name__ == "__main__":
    main()