#!/bin/bash

INPUT=input_graph.txt
OUTPUT=output

hadoop fs -rm -r $OUTPUT

hadoop jar /path/to/hadoop-streaming.jar \
    -input $INPUT \
    -output $OUTPUT \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
    
