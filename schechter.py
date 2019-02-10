#%%
import networkx as nx
import graphviz
import matplotlib.pyplot as plt
import networkx.drawing.nx_pylab as pg


#%%
def draw_dot(G,path=None):
    A=nx.nx_agraph.to_agraph(G)
    A.layout('dot')
    if path:
        A.draw(path)
    return A.to_string()

#%% 
def new_graph():
    G=nx.Graph()
    G.graph['graph']={'rankdir':'BT','dpi':1200}
    G.add_node(0)
    for x in G.nodes:
        G.node[x]['label']=''
        G.node[x]['color']='blue'
    G.node[0]['label']='Root'
    return(G)
G=new_graph()

#%% [markdown]
## Counting Trees
# *Combinatorics* is a branch of mathematics that is about counting things.
# Today we will count a kind of diagram called a *tree*.
#
# Although this may seem a simple idea, it turns out to be important in many
# situations in both mathematics and computer science.

#%% [markdown]
### Growing a tree
# To grow a tree, start with a dot that we call the "root".
# This is the simplest tree. 

#%%
graphviz.Source(draw_dot(G,path='G0.png'))


#%% [markdown]
# You grow a tree by starting with this simple tree and adding dots and edges.
# There are some rules:
# - The root gets left alone.
# - Every new dot you add gets connected to a dot that's already in the tree by an edge.
# - You always add dots in pairs, with each of the new dots connected to the same dot that's already in the tree.

# Trees always follow these rules:
# - A tree has a root dot at the bottom and either zero or two lines connected to it. 
# - Every dot in a tree except for the root has either three lines connected to it, or one.


#%% [markdown]
# Here is what happens when we add two new dots to the top of our simple tree:
# We get a tree with 3 dots and 2 lines.
#%%
G.add_edge(0,1)
G.add_edge(0,2)
G.node[1]['label']='New'
G.node[2]['label']='New'
graphviz.Source(draw_dot(G,path='G1.png'))


#%% [markdown]
# We can keep growing our tree following the rules. For example,
# we can add two new leaves to the top right of our tree:
# We get a tree with 5 dots and 4 lines.
#%%
G.node[1]['label']=''
G.node[2]['label']=''
G.add_edge(1,3)
G.add_edge(1,4)
G.node[3]['label']='New'
G.node[4]['label']='New' 
graphviz.Source(draw_dot(G,path='G2.png'))


#%% [markdown]
# We can add also two new leaves to the top right of our tree:

S=new_graph()
S.add_edges_from([(0,1),(0,2),(2,3),(2,4)])
for i in S.node:
    S.node[i]['label']=''
S.node[0]['label']='Root'
S.node[3]['label']='new'
S.node[4]['label']='new'
graphviz.Source(draw_dot(S,path='G3.png'))
#%% [markdown]
# **But we have to follow the rules!** So this is NOT a tree:
# Why not?

#%%
H=new_graph()
H.add_edges_from([(0,1),(1,2),(0,3),(3,4)])
H.node[1]['label']=''
H.node[2]['label']='New'
H.node[4]['label']='New'
H.node[3]['label']=''
graphviz.Source(draw_dot(H,path='G4.png'))

#%% [markdown]
## Observations

## First Question: How many leaves?
# We have three kinds of dots in our trees:
# - The root, and there's only one of those.
# - The leaves -- these are the dots with only one connecting edge.
# - the inner dots -- these are the ones with 3 connecting edges.

#%% [markdown]
# Total | Root | Inner | Leaves |
#  ---|---|---|---|
# 1 | 1 | 0 | 0 |
# 3 | 1 | 0 | 2 |
# 5 | 1 | 2 | 2 |
# 7 | 1 | 3 | 3 |
# 9 | 1 | ? | ? |

# What's the rule, and why?

#%% [markdown]

## Second Question: How many different trees are there with 7 dots? WIth 9?

#%% [markdown]
# Dots | Lines | Trees|
#  ---|---|---|
# 1 | 0 | 1
# 3 | 2 | 1
# 5 | 4 | 2
# 7 | ? | ?
# 10 | ? | ?


#%%


#%%
