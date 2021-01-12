from DiGraph import *
if __name__ == '__main__':
    tup= (5,4,3)
    # node = Node_Data(0,tup)
    # node.tag=500
    # print(node.tag)
    # print(node.get_key())
    # print(node)
    # edge =Edge_Data(0,1,500)
    # print(edge)
    # print(edge.get_src(),edge.get_dest())

    graph = DiGraph()

    print("        add node          ")
    print("add node ", graph.add_node(0,tup))
    print("add node ", graph.add_node(0, tup))
    print("add node ", graph.add_node(1, tup))
    print("add node ", graph.add_node(2))
    print("add node ", graph.add_node(3, tup))
    print("size mc" , graph.get_mc())
    print("size edge" , graph.e_size())
    print("size vertexs" , graph.v_size())


    print( "            add edge               ")

    print("add edge " , graph.add_edge(0,5,5000))
    print("add edge ", graph.add_edge(5, 0, 5000))
    print("add edge ", graph.add_edge(1, 1, 5000))
    print("add edge ", graph.add_edge(0, 1, 5000))
    print("add edge ", graph.add_edge(0, 1, 5000))
    print("add edge ", graph.add_edge(1, 2, 5000))

    print("size mc" , graph.get_mc())
    print("size edge" , graph.e_size())
    print("size vertexs" , graph.v_size())



    print("                remove edge               ")
    print("remove edge ", graph.remove_edge(0,5))
    print("remove edge ", graph.remove_edge(5, 0))
    print("remove edge ", graph.remove_edge(1, 1))
    print("remove edge ", graph.remove_edge(0, 1))
    print("remove edge ", graph.remove_edge(0, 1))

    print("size mc" , graph.get_mc())
    print("size edge" , graph.e_size())
    print("size vertexs" , graph.v_size())


    print(graph)

    print(graph.get_all_v())

    print(graph.all_out_edges_of_node(1))
    print(graph.all_in_edges_of_node(2))





    graph1= DiGraph()
    print("                 remove node              ")
    print("add node ", graph1.add_node(1,tup))
    print("add node ", graph1.add_node(2, tup))
    print("add node ", graph1.add_node(3, tup))
    print("add node ", graph1.add_node(4, tup))
    print("add node ", graph1.add_node(5, tup))
    print("add edge ", graph1.add_edge(1, 2, 5000))
    print("add edge ", graph1.add_edge(1, 3, 5000))
    print("add edge ", graph1.add_edge(4, 1, 5000))
    print("add edge ", graph1.add_edge(5, 1, 5000))

    print("size mc" , graph1.get_mc())
    print("size edge" , graph1.e_size())
    print("size vertexs" , graph1.v_size())

    print(graph1.all_out_edges_of_node(1))
    print(graph1.all_in_edges_of_node(1))

    print(graph1.all_in_edges_of_node(3))
    print(graph1.all_in_edges_of_node(2))

    print(graph1.all_out_edges_of_node(4))
    print(graph1.all_out_edges_of_node(5))
    print ("remove node " , graph1.remove_node(1))
    print("remove node ", graph1.remove_node(1))

    print("size mc" , graph1.get_mc())
    print("size edge" , graph1.e_size())
    print("size vertexs" , graph1.v_size())

    print(graph1.all_in_edges_of_node(3))
    print(graph1.all_in_edges_of_node(2))

    print(graph1.all_out_edges_of_node(4))
    print(graph1.all_out_edges_of_node(5))

    print(graph1)