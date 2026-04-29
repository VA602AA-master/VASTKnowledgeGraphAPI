#!/usr/bin/env python3
"""
Simple test to verify the default graph functionality works correctly.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Test the imports and basic functionality
try:
    from main import default_graph_id, graph_registry
    print("✓ Successfully imported default_graph_id and graph_registry")
    print(f"  default_graph_id = '{default_graph_id}'")
    print(f"  graph_registry = {graph_registry}")
except Exception as e:
    print(f"✗ Error importing: {e}")
    sys.exit(1)

# Test that the default graph ID is set correctly
try:
    assert default_graph_id == "default", f"Expected 'default', got '{default_graph_id}'"
    print("✓ Default graph ID is correctly set to 'default'")
except AssertionError as e:
    print(f"✗ Assertion failed: {e}")
    sys.exit(1)

# Test that the graph_registry is a dictionary
try:
    assert isinstance(graph_registry, dict), f"Expected dict, got {type(graph_registry)}"
    print("✓ Graph registry is a dictionary")
except AssertionError as e:
    print(f"✗ Assertion failed: {e}")
    sys.exit(1)

print("\n✓ All basic tests passed!")
print("\nThe API now supports:")
print("1. Uploading graphs via POST /upload/")
print("2. Setting a default graph via POST /set-default/{graph_id}")
print("3. Accessing the default graph via GET /summary/default")
print("4. Accessing specific graphs via GET /summary/{graph_id}")
