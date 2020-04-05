import networkx as nx
G = nx.karate_club_graph()
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
nx.draw(G, with_labels = True, node_color='lightblue', edge_color='gray')
plt.savefig('karate_club.pdf')



N = 20
p = 0.2


def er_graph(N, p):
    """generate an ER graph """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    G.number_of_nodes()
    return G

nx.draw(er_graph(30, 0.5), node_size = 40, node_color = 'gray')
plt.savefig('er_graph1.pdf')


def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel('Degree $k$')
    plt.ylabel('$P(k)$')    
    plt.title('degree_distribution')
    

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)

G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)

G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)

import numpy as np
A1 = np.loadtxt('adj_allVillageRelationships_vilno_1.csv', delimiter = ',')   
A2 = np.loadtxt('adj_allVillageRelationships_vilno_2.csv', delimiter = ',')

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_network_stats(G):
    print('number of nodes: %d' % G.number_of_nodes())
    print('number of edges: %d' % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))

basic_network_stats(G1)
basic_network_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig('villages.pdf')

def connected_component_subgraphs(G): 
    return [G.subgraph(c) for c in nx.connected_components(G)]

gen = connected_component_subgraphs(G1)  

G1_LCC = max(connected_component_subgraphs(G1), key=len)
G2_LCC = max(connected_component_subgraphs(G2), key=len)

G1_LCC.number_of_nodes() / G1.number_of_nodes()
G2_LCC.number_of_nodes() / G2.number_of_nodes()

plt.figure()
nx.draw(G1_LCC, node_color='red', edge_color='gray', node_size=20)
plt.savefig('village1.pdf')

plt.figure()
nx.draw(G2_LCC, node_color='green', edge_color='gray', node_size=20)
plt.savefig('village2.pdf')   