import networkx as nx
import time
import Algorithms

if __name__ == '__main__':
    time_base = time.time()
    random_tree = nx.random_tree(30000, 264)
    tree_links = list(random_tree.edges)

    nodes = sorted(list(random_tree.nodes))
    file = open("Algorithm2_random_tree_results.txt", 'w')
    for node in nodes[25378:]:
        print(node)
        tree = nx.DiGraph(tree_links)
        file.write("\n" + str(str(node)+ "\t" + str(sorted(list(tree.neighbors(node))))))
        file.write("\n" + str("Node "+ str(node) +  " : "+ str(Algorithms.count_trees(tree, node))))

    file.close()

    print("The process took ", (time.time()-time_base)/60, "minutes to accomplish")