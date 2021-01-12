from typing import Dict
class DiGraph:

    def __init__(self):
        self.__mc=0
        self.__size_edges=0
        self.__nodes : Dict[int,Node_Data]=dict()
        self.__neighbors :Dict[int,Dict[int,Edge_Data]]=dict()
        self.__neighbors_in : Dict[int,Dict[int,Edge_Data]]=dict()

    def v_size(self) -> int:
        return len(self.__nodes)

    def e_size(self) -> int:
        return self.__size_edges

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__neighbors_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__neighbors.get(id1)

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float, ) -> bool:
        if id1 is not id2 and id1 in self.__nodes and id2 in self.__nodes and id2 not in self.__neighbors.get(id1):
            #add edge
            edge = Edge_Data(id1,id2,weight)
            self.__neighbors.get(id1).update({id2:edge})
            self.__neighbors_in.get(id2).update({id1: edge})
            self.__mc+=1
            self.__size_edges+=1
            return True
        else:return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.__nodes:
            node = Node_Data(node_id,pos)
            self.__nodes.update({node_id:node})
            self.__neighbors.update({node_id:dict()})
            self.__neighbors_in.update({node_id:dict()})
            self.__mc+=1
            return True
        else: return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__nodes:
            #remove node
            size_=len(self.all_out_edges_of_node(node_id))+len(self.all_in_edges_of_node(node_id))
            self.__mc+=size_
            self.__size_edges-=size_
            #in to node_id
            for key in self.all_in_edges_of_node(node_id):
                self.__neighbors.get(key).pop(node_id)
            # out to node_id
            for key in self.all_out_edges_of_node(node_id):
                self.__neighbors_in.get(key).pop(node_id)
            # pop node_id in out
            self.__neighbors_in.pop(node_id)
            self.__neighbors.pop(node_id)
            #pop from vertexs
            self.__nodes.pop(node_id)
            self.__mc+=1
            return True
        else:return False

    def remove_edge(self, node_id1, node_id2: int) -> bool:
        if node_id1 is not node_id2 and node_id1 in self.__nodes and node_id2 in self.__nodes and node_id2 in self.__neighbors.get(node_id1):
            #remve edge
            self.__neighbors.get(node_id1).pop(node_id2)
            self.__neighbors_in.get(node_id2).pop(node_id1)
            self.__mc+=1
            self.__size_edges-=1
            return True
        else:return False
    def __repr__(self):
        return "Graph: (vertexs: %s neighbors: %s )"%(self.__nodes,self.__neighbors)

class Node_Data:

    def __init__(self, key:int,pos:tuple):
        self.tag = 0
        self.weight =0
        self.info = 0
        self.__key=key
        self.__position = pos

    def get_key(self) -> int:
        return self.__key

    def get_pos(self)->tuple:
        return self.__position

    def set_pos(self,pos:tuple):
        self.__position=pos

    def __lt__(self, other):
        selfPriority = (self.weight, self.__key)
        otherPriority = (other.weight, other.get_key())
        return selfPriority < otherPriority

    def __repr__(self):
        return "Node Data: (key: %s pos %s ) "%(self.get_key(),self.get_pos())

class Edge_Data:
    def __init__(self,src:int,dest:int,weight:float):
        self.__src=src
        self.__dest=dest
        self.__weight=weight
        self.tag=0
        self.info=""

    def get_src(self)->int:
        return self.__src
    def get_dest(self)->int:
        return self.__dest

    def get_weight(self) -> float:
        return self.__weight

    def __repr__(self):
        return "Edge Data: (src: %s dest: %s weight: %s )"%(self.get_src(),self.get_dest(),self.get_weight())

