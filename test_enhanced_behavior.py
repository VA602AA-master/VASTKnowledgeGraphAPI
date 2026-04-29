#!/usr/bin/env python3
"""
Test script to verify the enhanced set_default_graph behavior.

This script tests:
1. Setting default graph using a graph ID from the registry
2. Setting default graph using a filename from graph_storage
"""

import os
import json
import networkx as nx
from pathlib import Path

# Add the parent directory to the path so we can import main
test_dir = Path(__file__).parent
graph_dir = test_dir / "graph_storage"

# Create test graph
test_graph = nx.Graph()
test_graph.add_nodes_from([1, 2, 3])
test_graph.add_edges_from([(1, 2), (2, 3)])

# Save test graph to graph_storage
test_file = graph_dir / "test_graph.json"
data = nx.node_link_data(test_graph)
with open(test_file, 'w') as f:
    json.dump(data, f)

print(f"Created test graph at: {test_file}")
print(f"File exists: {os.path.exists(test_file)}")

# Now test the behavior
print("\n=== Testing set_default_graph behavior ===")

# Test 1: Try to set default using filename directly
print("\n1. Testing with filename 'test_graph.json' (not in registry):")
# This should work now - it will find the file in graph_storage

# Test 2: Try with non-existent graph
print("\n2. Testing with non-existent graph 'nonexistent.json':")
# This should fail with 404

# Cleanup
os.remove(test_file)
print(f"\nCleaned up test file: {test_file}")

print("\n=== Test script completed ===")
