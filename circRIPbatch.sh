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
    echo "Submit task for: $col5"
    qsub circRIPsingle.qsub $col2 $col4 $col5
    echo "---------------------------------"
  fi
done < "$1"
