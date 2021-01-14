# Ex3


# Ex3
oop university course assignment

***oop university course assingment authours : Saeed Esawi & Elior Gueta***

**summery:**

the project focused about directional weighted graph in python


in this project we need to implement some algorithm (like shortest path,connected component,tarjan algorithm)


and we need to examine the results between our Workspace and compare the runtimes on python,java and networkX.


**description:**


in our directional weighted graph we have an edges,which every edge has a weight and a direction.


We got 3 classes who help us to create our graph:

***1.Node_Data(an inner class in our DiGraph):***

every object in this class has its own:
*key
*tag
*weight 
*info 
*position
**the functions in this class and a short description about them:**

**get_key():**
This function return us the unique key of this node.

**get_pos():**
This function return the exact position of the node.null if none.

**set_pos():**
sets a new position for the node.

**get_info():**
This function returns the information of this node.

**set_info():**
This function sets new information to our node.

**repr():**
This function return us the graph nicely(like tostring in java)

***2.DiGraph:***

This class represents a directed weighted graph . this class implements "Graphinterface" class.
Every object in this class has its own fields:

*3 dictionaries who represent us the nodes,the neighbours ,and the neighbours who get in to this node.
*Mc- A mode** counter who tell us about every change in our graph.
*size_edges:** counter for count all the edges in our graph .

**the functions in this class, and a short description about them:**
**v_size():**
This function Returns the number of vertices (nodes) in the graph

**e_size():**
This function returns the number of edges.

**all_in_edges_of_node():**
This function give us the dict who representing all the edges getting out of the given node.

**all_out_edges_of_node():**
This function give us the dict who representing all the edges getting in of the given node.

**get_mc:**
Returns our mode-counter , the number of the changes that used on our graph.

**add_edge():**
this function connect an edge (with weight) between 2 nodes(src,dest).

**add_node:**
adding an vertex to the graph with the given id.

**remove_node(node_id):**
remove a vertex from the graph by the given id.

**remove_node(node_id1,node_id2)**:
remove the edge between node_id1 and node_id2.

**repr():**
represents the graph nicely(like tostring in java).


***3.GraphAlgo:***

This class implements the classGraphAlgoInterface,this class represents graph algorithms.
in this class the graph is our object.

**the functions in this class and a short description about them:**

**1.init():**
Initiate the graph algorithm to point on a graph.

**2.get_graph():**
Return the underlying graph of which this class works .

**3.load_from_json():**
This function creates a new graph by loading a json file and init graph(with the Json file details) to our class.

**4.save_to_json():**
Saving the graph in Json format to a new file(String).

**5.init_all_variables():**
Initiate all the variables in our graph.

**6.shortest_path():**
This function Returns the distance of the shortest path from the vertex to a different vertex and returns a list with the id's of the path vertices.

**7.connected_component(id_1):**
This function return us a list with all the id's of the nodes in the connected component of a given vertex.

**8.connected_component():**
This function return us a list of all the connected components.

**9.sconnect():**
This function based on Df's algorithm but in iterative way(seems like tarjan algorithm).
Depth-first search (DFS) is an algorithm for traversing or searching graph data structures.
A directed graph is strongly connected if there is a path between all pairs of vertices. 
A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.

<img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Tarjan%27s_Algorithm_Animation.gif">


***Some examples for our graphs:***
![](https://github.com/Eliorg93/Ex3/blob/master/wiki_images/G1.jpg)



![](https://github.com/Eliorg93/Ex3/blob/master/wiki_images/G2.jpg)





![](https://github.com/Eliorg93/Ex3/blob/master/wiki_images/G3.jpg)














