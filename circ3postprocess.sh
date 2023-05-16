#!/bin/bash

# check if file name is passed as an argument
if [ $# -eq 0 ]; then
    echo "No arguments provided"
    echo "Usage: ./scriptname filename"
    exit 1
fi

# read the file line by line
while IFS=',' read -r col1 col2 col3 col4 col5
do
  if [ "$col1" != "Input_result_folder" ]; then
    echo "Processing: $col5"
    python circ3postprocess.py -p "$col1" -n "$col2"
    python circ3postprocess.py -p "$col3" -n "$col4"
    
    echo "---------------------------------"
  fi
done < "$1"
