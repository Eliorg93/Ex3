from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
if __name__ == '__main__':
    # graph = DiGraph()
    # algo = GraphAlgo(graph)
    #
    # print(algo.load_from_json("../data/T0.json"))
    #
    # print(algo.get_graph())
    #
    # print(algo.save_to_json("../data/Test.json"))

    graph = DiGraph()
    tup= (7,6,8)
    tup1 = (5, 4, 8)
    tup2 = (2, 4, 8)
    tup3 = (3, 4, 8)

    print("add node ", graph.add_node(1,tup))
    print("add node ", graph.add_node(2, tup1))
    print("add node ", graph.add_node(3, tup2))
    print("add node ", graph.add_node(4, tup3))
    print("add edge ", graph.add_edge(1, 2, 1))
    print("add edge ", graph.add_edge(2, 3, 2))
    print("add edge ", graph.add_edge(3,1, 1))

    algo = GraphAlgo(graph)

    # print(algo.shortest_path(1,3))
    print(algo.connected_component(1))
    print(algo.connected_components())
    # algo.plot_graph()