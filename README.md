# BDA-ASSIGNMENT
Question: Use MapReduce to find the shortest path between two people in a social graph. Hint: Use an adjacency list to model a graph, and for each node store the distance from the original node, as well as a back pointer to the original node. Use the mappers to propagate the distance to the original node, and the reducer to restore the state of the graph. Iterate until the target node has been reached.

Answer:
# Shortest Path using MapReduce (BFS)

This project implements a MapReduce algorithm to find the shortest path between two nodes in a social graph using Hadoop Streaming.

### Problem:
Given a graph where nodes represent people and edges represent connections (e.g., friendships), find the shortest path from a **source node** to a **target node**.

### Approach:
This is a parallel BFS implementation using:
- **Mapper**: Propagates distances to neighboring nodes.
- **Reducer**: Aggregates minimum distances and updates the graph state.

### Folder Structure:
shortest-path-mapreduce/ ├── mapper.py # Mapper script ├── reducer.py # Reducer script ├── driver.sh # Shell script to run on Hadoop ├── input_graph.txt # Sample input graph └── README.md # This file


### Input Format:
Each line represents a node:
<NodeID> <distance_from_source> <backpointer> <comma-separated_neighbors>


### Example:
A 0 - B,C B -1 - D C -1 - D D -1 -



Modelling the graph using an adjacency list, where each node stores:

Neighbors (list of directly connected nodes) Distance from the source node (initialized as ∞ except for the source, which is 0) Back-pointer to track the path The MapReduce process iterates until the shortest path to the target is found.

Steps

Input Format (Adjacency List) Each node has: node_id [neighbor1, neighbor2, ...] distance backpointer
For example, in a social graph: A [B, C] 0 null B [A, D, E] ∞ null C [A, F] ∞ null D [B] ∞ null E [B, F] ∞ null F [C, E] ∞ null

Mapper: Spread Distances Each node emits: Itself (to retain structure) New distance for neighbors (if shorter)
For example, if A has distance = 0, it emits: A [B, C] 0 null (retains original) B null 1 A C null 1 A

Reducer: Merge Updates The reducer: Keeps adjacency list Updates shortest distance and back-pointer Emits updated node
If B gets updates: B [A, D, E] ∞ null B null 1 A

The reducer picks distance = 1 (shorter), updates B: B [A, D, E] 1 A

Iteration Until Target Found The process repeats until the target node has a distance (i.e., it's reached).
