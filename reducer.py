#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    node_id, value = line.split("\t", 1)
    node_id = node_id.strip()
    
    if 'buffer' not in locals():
        buffer = {}
        
    if node_id not in buffer:
        buffer[node_id] = []
    buffer[node_id].append(value)

for node_id, values in buffer.items():
    min_distance = -1
    backpointer = '-'
    neighbors = []

    for value in values:
        parts = value.strip().split()
        if parts[0] == 'NODE':
            distance = int(parts[1])
            backpointer = parts[2]
            neighbors = parts[3:] if len(parts) > 3 else []
            if distance != -1:
                min_distance = distance
        elif parts[0] == 'DISTANCE':
            tentative_distance = int(parts[1])
            src_node = parts[2]
            if min_distance == -1 or tentative_distance < min_distance:
                min_distance = tentative_distance
                backpointer = src_node

    neighbors_str = ','.join(neighbors)
    print(f"{node_id}\t{min_distance} {backpointer} {neighbors_str}")
  
