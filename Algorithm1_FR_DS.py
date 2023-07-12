import networkx as nx
import csv
import random
import time
import Algorithms
import re

if __name__ == '__main__':

    with open('./Data/FR/musae_FR_edges.csv') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
        links = list()
        for i in d:
            temp = re.split(",",i[0])
            links.append((int(temp[0]),int(temp[1])))

    time_base = time.time()

    graph = nx.MultiGraph(links[0:30])

    index = random.randint(0,len(graph.nodes))
    node = list(graph.nodes)[index]
    print("Node ",node, ": ", Algorithms.count_all(graph, node))
    print("The process took ", (time.time()-time_base)/60, "minutes to complete")

