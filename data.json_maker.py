import pandas as pd #import pandas library 
import json

edges_df = pd.read_csv('edges.csv', sep = ";")
nodes_df = pd.read_csv('nodes.csv', sep = ";")


N = len(nodes_df)
L = len(edges_df)

nodes = [{ 'id': str(nodes_df['node_id'][k]), 'color' : hex(int(nodes_df['node_color'][k][1:],16)), 'label': nodes_df['node_label'][k]} for k in range(N)]

edges=[{'source': str(edges_df['source_id'][k]), 'target': str(edges_df['target_id'][k]), 'weight' : edges_df['weights'][k]*0.1} for k in range(L)]

graph = {
    'nodes': nodes,
    'edges': edges
}

with open("data.json", "w") as f: f.write(json.dumps(graph))