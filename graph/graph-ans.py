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
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        # Fill up adjacency list and return it when done
        adjacency_list = []
        adjacency_list_index = 0
        # Loop through the nodes, if node value matches to adjacency list index, find all edges coming from that node and append to adjacency list,
        # if no node with that index nor edge coming from that node then append None
        for node in self.nodes:
            while True:
                if node.value == adjacency_list_index:
                    edges_from_node = []
                    # Find edges coming from that node and append to edges from that node list
                    for edge in node.edges:
                        if edge.node_from == node:
                            edges_from_node.append(((edge.node_to.value, edge.value)))
                    # Append edges from that node to adjacency list, or append None if no edges
                    if len(edges_from_node) != 0:
                        adjacency_list.append(edges_from_node)
                    else:
                        adjacency_list.append(None)
                    break
                # Append None to adjacency list if node does not match with index
                else:
                    adjacency_list.append(None)
                adjacency_list_index += 1
            # Increment index to match the movement of node
            adjacency_list_index += 1
        return adjacency_list
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        # Return Adjacency Matrix when done
        adj_matrix = []
        adj_matrix_index = 0
        # Loop through each node
        for node in self.nodes:
            # Keep on incrementing the matrix index until it matches with node value
            while True:
                if node.value != adj_matrix_index:
                    adj_matrix.append(0)
                    adj_matrix_index += 1
                # When node value matches with matrix index, Create another node loop and edge list
                else:
                    adj_edges = []
                    adj_edges_index = 0
                    for node_inner in self.nodes:
                        # Keep on incrementing the edge list index until it matches with inner node vlaue
                        while True:
                            if node_inner.value != adj_edges_index:
                                adj_edges.append(0)
                                adj_edges_index += 1
                            # If inner node value matches with edge list index, append the edge that comes from node and goes to inner node
                            else:
                                for edge in node_inner.edges:
                                    if edge.node_from == node and edge.node_to == node_inner:
                                        adj_edges.append(edge.value)
                                        break
                                else:
                                    adj_edges.append(0)
                                adj_edges_index += 1
                                break
                    # After finding all edges that comes from node and goes to inner node, append the edge list to adjacency matrix
                    adj_matrix.append(adj_edges)
                    adj_matrix_index += 1
                    break
        # Return the adj matrix but first, turn the all 0 integers to list full of zeros (0 int comes from index that do not match to node value)
        return [[0]*len(adj_matrix) if not isinstance(element, list) else element for element in adj_matrix]


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())











# graph = Graph()
# graph.insert_edge(100, 1, 2)
# graph.insert_edge(101, 1, 3)
# graph.insert_edge(102, 1, 4)
# graph.insert_edge(103, 3, 4)
# graph.insert_edge(104, 10, 3)
# # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
# print(graph.get_edge_list())
# # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
# print(graph.get_adjacency_list())
# # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
# print(graph.get_adjacency_matrix())