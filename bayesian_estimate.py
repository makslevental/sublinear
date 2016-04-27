import networkx as nx
import os
import random
import matplotlib.pyplot as plt


G=nx.read_edgelist(os.path.join(os.path.dirname(__file__)+os.path.sep+'wiki-Vote.clean.txt.gz'))

degs = nx.degree(G)
print(max(degs))
print(sum(degs.values())/len(degs))

hist = 1000*[0]
for i in range(50):
    ls = random.sample(list(G.nodes_iter()),10)
    for deg,count in nx.degree(G,ls).items():
        hist[count] += 1


plt.hist(hist)
plt.show()

# nx.draw(G)
# plt.show()