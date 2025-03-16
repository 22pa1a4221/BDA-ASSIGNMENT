#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) < 3:
        continue

    node_id = parts[0]
    distance = int(parts[1])
    backpointer = parts[2]
    neighbors = parts[3].split(',') if len(parts) > 3 else []

    # Emit the node structure itself
    print(f"{node_id}\tNODE {distance} {backpointer} {' '.join(neighbors)}")

    # If node is active, propagate to neighbors
    if distance != -1:
        for neighbor in neighbors:
            print(f"{neighbor}\tDISTANCE {distance + 1} {node_id}")
          
