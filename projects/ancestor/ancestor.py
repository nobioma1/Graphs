class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if both vertex 1 and vertex 2 are in vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        # otherwise through error
        else:
            raise KeyError('The vertex does not exist')


def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    graph = Graph()

    # create graph vertexes with the child and parent
    for (parent, child) in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        
        # connect the edges
        graph.add_edge(child, parent)
    
    # initialize a queue
    queue = Queue() 

    visited = set()

    queue.enqueue(starting_node)

    current_vertex = None
    
    while queue.size():
        current_vertex = queue.dequeue()
        if current_vertex not in visited:
            for neighbor in graph.vertices[current_vertex]:
                queue.enqueue(neighbor)
            visited.add(current_vertex)
    
    # if the current vertex is still same ad the starting vertex, there is no ancestor
    if current_vertex == starting_node:
        return -1
    
    # return current vertex
    return current_vertex
