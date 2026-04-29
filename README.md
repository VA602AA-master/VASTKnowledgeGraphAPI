# NetworkX Graph API

A FastAPI application for uploading, storing, and analyzing NetworkX graphs.

## Features

- Upload NetworkX graphs in JSON format
- Retrieve comprehensive graph summaries
- Unique ID assignment for each uploaded graph
- Local storage of graph files
- **Set a default graph** that can be accessed without uploading a file
- Access graphs using the special "default" graph ID

## Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /upload/

Upload a NetworkX graph JSON file.

**Parameters:**
- `file` (required): JSON file containing a NetworkX graph

**Response:**
```json
{
  "graph_id": "unique-id-for-this-graph",
  "message": "Graph uploaded successfully",
  "filename": "original-filename.json"
}
```

**Example:**
```bash
curl -X POST -F "file=@sample_graph.json" http://localhost:8000/upload/
```

### POST /set-default/{graph_id}

Set a graph as the default graph that can be accessed without uploading a file.

**Parameters:**
- `graph_id` (path): The unique ID of the graph to set as default

**Response:**
```json
{
  "message": "Graph set as default successfully",
  "default_graph_id": "default",
  "graph_id": "original-graph-id"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/set-default/your-graph-id-here
```

### GET /summary/{graph_id}

Get a summary of the properties of a NetworkX graph.

**Parameters:**
- `graph_id` (path): The unique ID returned when uploading the graph, or "default" to access the default graph

**Response:**
```json
{
  "graph_id": "unique-id-for-this-graph",
  "basic_properties": {
    "number_of_nodes": 5,
    "number_of_edges": 7,
    "is_directed": true,
    "is_weakly_connected": true,
    "is_strongly_connected": true,
    "is_connected": null
  },
  "degree_properties": {
    "average_degree": 2.8,
    "degree_centrality": {"1": 0.42857142857142855, "2": 0.42857142857142855, ...}
  },
  "node_properties": {
    "node_count": 5,
    "nodes_with_highest_degree": [[1, 2], [2, 2], [3, 2], [4, 1], [5, 1]]
  },
  "edge_properties": {
    "edge_count": 7,
    "edges_with_highest_weight": [[4, 5, 2.0], [1, 2, 2.5], [3, 4, 3.0], [2, 4, 1.5], [1, 3, 1.0], [5, 1, 1.0], [2, 3, 0.5]]
  }
}
```

**Example:**
```bash
# Access a specific graph by its ID
curl http://localhost:8000/summary/your-graph-id-here

# Access the default graph
curl http://localhost:8000/summary/default
```

### GET /health/

Health check endpoint to verify the API is running.

**Response:**
```json
{
  "status": "healthy",
  "graph_count": 1
}
```

## Default Graph Usage

The default graph feature allows you to set one graph as the "default" so you can access it without uploading a file each time.

### Setup Process:

1. **Upload a graph** using the POST /upload/ endpoint
2. **Set it as default** using POST /set-default/{graph_id}
3. **Access it** using GET /summary/default

### Example Workflow:

```bash
# 1. Upload a graph
curl -X POST -F "file=@my_graph.json" http://localhost:8000/upload/
# Response: {"graph_id": "abc123...", "message": "Graph uploaded successfully", ...}

# 2. Set it as default
curl -X POST http://localhost:8000/set-default/abc123...
# Response: {"message": "Graph set as default successfully", "default_graph_id": "default", ...}

# 3. Access the default graph
curl http://localhost:8000/summary/default
# Response: {graph summary...}
```

## Testing

Run the test script to create a sample graph and test the API endpoints:

```bash
python test_api.py
```

## Graph Format

The JSON file should contain a NetworkX graph in node-link format, which can be created using:

```python
import networkx as nx
data = nx.node_link_data(G)  # Where G is your NetworkX graph
```

## Project Structure

```
.
├── main.py                # FastAPI application
├── requirements.txt       # Dependencies
├── test_api.py            # Test script
├── setup_default_graph.py # Script to help set up default graphs
├── README.md              # This file
└── graph_storage/        # Directory for stored graphs (created automatically)
```

## Dependencies

- FastAPI: Web framework
- Uvicorn: ASGI server
- NetworkX: Graph library

## License

This project is open source and available under the MIT License.
