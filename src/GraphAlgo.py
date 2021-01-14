from typing import List
from GraphInteface import GraphInteface as GraphInterface
from DiGraph import *
import json
import math
from queue import PriorityQueue
import matplotlib.pyplot as plot_to_graph
import random

# mistnim globalim
list_path = []
lists_path = []
ids = dict()


class GraphAlgo:
    def __init__(self, g=DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as file:
                json_file = json.load(file)
            self.graph = DiGraph()
            # {"id": 0}
            # {"pos": "35.19381366747377,32.102419275630254,0.0", "id": 16}
            for n in json_file['Nodes']:
                if n.get('pos') is None:
                    self.graph.add_node(n.get('id'))
                else:
                    str = n.get('pos')
                    str_split = str.split(",")
                    position = tuple(map(float, str_split))
                    self.graph.add_node(n.get('id'), position)
            # {"src":0,"w":1.4004465106761335,"dest":1}
            for e in json_file['Edges']:
                self.graph.add_edge(e.get('src'), e.get('dest'), e.get('w'))
            return True
        except FileNotFoundError:
            return False

    def save_to_json(self, file_name: str) -> bool:

        vertexs = []
        for n in self.graph.get_all_v().values():
            if n.get_pos() is None:
                vertexs.append({"id": n.get_key()})
            else:
                pos = str(n.get_pos()[0]) + "," + str(n.get_pos()[1]) + "," + str(n.get_pos()[2])
                vertexs.append({"id": n.get_key(), "pos": pos})
        edges = []
        for n in self.graph.get_all_v().keys():
            for e in self.graph.all_out_edges_of_node(n).values():
                edges.append({"src": e.get_src(), "w": e.get_weight(), "dest": e.get_dest()})
        lists = {"Edges": edges, "Nodes": vertexs}
        try:
            with open(file_name, 'w') as file:
                json.dump(lists, file)
            return True
        except FileNotFoundError:
            return False

    def __init_all_varibales(self):
        # self.tag = 0
        # self.weight =0
        # self.info = 0
        for node in self.graph.get_all_v().values():
            node.tag = 0
            node.weight = math.inf
            node.info = ""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return math.inf, []
        self.__init_all_varibales()

        q = PriorityQueue()

        node_id1 = self.graph.get_all_v()[id1]
        node_id1.weight = 0
        node_id1.tag = -1
        q.put(node_id1)

        while not q.empty():
            v1 = q.get()
            for edge in self.graph.all_out_edges_of_node(v1.get_key()).values():
                v2 = self.graph.get_all_v()[edge.get_dest()]
                dist = v1.weight + edge.get_weight()
                if dist < v2.weight:
                    v2.weight = dist
                    v2.tag = v1.get_key()
                    q.put(v2)

        node_id2 = self.graph.get_all_v()[id2]
        if node_id2.weight is math.inf:
            return math.inf, []
        path = []

        path.insert(0, node_id2.get_key())

        tag = node_id2.tag
        while tag != -1:
            node = self.graph.get_all_v()[tag]
            path.insert(0, node.get_key())
            tag = node.tag

        return node_id2.weight, path

    def connected_component(self, id1: int) -> list:
        if self.graph is None or id1 not in self.graph.get_all_v():
            return []

        global ids, list_path, lists_path

        list_path = []
        lists_path = []

        for n in self.graph.get_all_v().keys():
            ids.update({n: int(0)})
        self.__sconnect(id1)
        return list_path

    def __sconnect(self, v: int):
        id = 0
        low = dict()
        onStack = dict()
        stack = []

        for n in self.graph.get_all_v().keys():
            low.update({n: 0})
            onStack.update({n: False})

        global list_path, lists_path, ids

        work = [(v, 0)]  # NEW: Recursion stack.
        while work:
            v, i = work[-1]  # i is next successor to process.
            del work[-1]
            if i == 0:  # When first visiting a vertex:
                stack.append(v)
                onStack.update({v: True})
                id += 1
                ids.update({v: id})
                low.update({v: id})
            recurse = False
            j = 0
            for to in self.graph.all_out_edges_of_node(v).keys():
                w = to
                if ids.get(w) == 0:
                    # CHANGED: Add w to recursion stack.
                    work.append((v, j + 1))
                    work.append((w, 0))
                    recurse = True
                    j += 1
                    break
                elif onStack.get(to) is True:
                    j += 1
                    low.update({v: min(low.get(v), low.get(to))})

            if recurse: continue  # NEW
            if ids.get(v) is low.get(v):
                list_path = []
                while stack:
                    node = stack.pop()
                    list_path.insert(0, node)
                    onStack.update({node: False})
                    low.update({node: (ids.get(v))})
                    if node == v: break
                lists_path.insert(0, list_path)
            if work:  # NEW: v was recursively visited.
                w = v
                v, _ = work[-1]
                low.update({v: min(low.get(v), low.get(w))})

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []

        global ids, list_path, lists_path

        list_path = []
        lists_path = []

        for n in self.graph.get_all_v().keys():
            ids.update({n: int(0)})

        for n in self.graph.get_all_v().keys():
            if ids.get(n) == 0:
                self.__sconnect(n)

        return lists_path

    def plot_graph(self) -> None:
        x_arr = []
        y_arr = []

        for node in self.graph.get_all_v().values():
            if node.get_pos() is None:
                tup = (random.uniform(0, 50), random.uniform(0, 50))
                node.set_pos(tup)
                x_arr.append(node.get_pos()[0])
                y_arr.append(node.get_pos()[1])
            else:
                x_arr.append(node.get_pos()[0])
                y_arr.append(node.get_pos()[1])

        n = [j for j in self.graph.get_all_v().keys()]
        fig, ax = plot_to_graph.subplots()
        ax.scatter(x_arr, y_arr)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (x_arr[p], y_arr[p]))

        for n in self.graph.get_all_v().keys():
            for e in self.graph.all_out_edges_of_node(n).values():
                # src - > dest
                x_src = self.graph.get_all_v().get(e.get_src()).get_pos()[0]
                y_src = self.graph.get_all_v().get(e.get_src()).get_pos()[1]

                x_dest = self.graph.get_all_v().get(e.get_dest()).get_pos()[0]
                y_dest = self.graph.get_all_v().get(e.get_dest()).get_pos()[1]
                plot_to_graph.title("Ex3 OOP")

                plot_to_graph.arrow(x_src, y_src, (x_dest - x_src), (y_dest - y_src), length_includes_head=True,
                                    width=0.0001, head_width=0.0001, color='green')

        plot_to_graph.plot(x_arr, y_arr, "*")

        plot_to_graph.show()
