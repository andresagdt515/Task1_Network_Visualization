import pandas as pd #import pandas library 
import json #import json library 

edges_df = pd.read_csv('edges.csv', sep = ";") #get the Dataframes from edges.csv
nodes_df = pd.read_csv('nodes.csv', sep = ";") #get the Dataframes from nodes.csv

N = len(nodes_df) #total number of nodes
L = len(edges_df) #total number of edges

nodes = [{ 'id': str(nodes_df['node_id'][k]), 'color' : hex(int(nodes_df['node_color'][k][1:],16)), 'label': nodes_df['node_label'][k]} for k in range(N)]
#create nodes variable with a given structure, ready for the 2D JavaScript simulation (json format)

edges=[{'source': str(edges_df['source_id'][k]), 'target': str(edges_df['target_id'][k]), 'weight' : edges_df['weights'][k]*0.1} for k in range(L)]
#create edges variable with a given structure, ready for the 2D JavaScript simulation (json format)

graph = { #ensembling nodes and edges in graph variable (json format)
    'nodes': nodes,
    'edges': edges
}

with open("data.json", "w") as f: f.write(json.dumps(graph)) # create a json file called data.json from the graph variable