class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    #directed graph    
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for triple in self.edges:
            edge_list.append((triple.value,triple.node_from.value,triple.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        lst = self.get_edge_list()
        count = self.get_count()
        adj_lst = [None]*(count+1)
        for triple in lst:
            if adj_lst[triple[1]] == None:
                adj_lst[triple[1]] = [(triple[2],triple[0])]
            else:
                adj_lst[triple[1]].append((triple[2],triple[0]))
        return adj_lst

    def get_count(self):
        lst = self.get_edge_list()
        count = 0
        for triple in lst:
            if triple[2]>count:
                count = triple[2]
        return count
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        lst = self.get_adjacency_list()
        count = self.get_count()
        adj_matrix = matrix = [ [ 0 for i in range(count+1) ] for j in range(count+1) ]
        for i in range(len(lst)):
            if lst[i]:
                for j in range(len(lst[i])):
                    adj_matrix[i][lst[i][j][0]]= lst[i][j][1]
        return adj_matrix



graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print (graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print (graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print (graph.get_adjacency_matrix())