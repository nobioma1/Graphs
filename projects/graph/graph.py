"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # initialize a queue to hold vertices
        queue = Queue()
        # instantiate set to hold visited vertexes
        visited = set()
        # enqueue the starting vertex
        queue.enqueue(starting_vertex)
        # while the is a vertex in the queue:
        while queue.size():
            # dequeue vertex
            current_vertex = queue.dequeue()
            # check if vertex is not in visited
            if current_vertex not in visited:
                # print vertex
                print(current_vertex)
                # enqueue the the neighbors of the vertex
                for neighbor in self.vertices[current_vertex]:
                    queue.enqueue(neighbor)
                # add vertex to visited
                visited.add(current_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize stack to hold vertices
        stack = Stack()
        # instantiate a set to hold visited vertexes
        visited = set()
        # push starting_vertex into stack
        stack.push(starting_vertex)
        # while there is a vertex in the stack
        while stack.size():
            # pop vertex
            current_vertex = stack.pop()
            # if vertex is not in visited
            if current_vertex not in visited:
                # print vertex
                print(current_vertex)
                # add the neighbors to the stack
                for neighbor in self.vertices[current_vertex]:
                    stack.push(neighbor)
                # add vertex to visited
                visited.add(current_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        # if there is a vertex passed in
        if starting_vertex:
            # add the vertex to visited
            visited.add(starting_vertex)
            # print the vertex
            print(starting_vertex)
            # loop through the neighbors
            for neighbor in self.vertices[starting_vertex]:
                # check if the vertex has been visited
                if neighbor not in visited:
                    # call the dft_recursive  passing in the neighbor and visited
                    self.dft_recursive(neighbor, visited)

        return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create set to hold visited vertex
        visited = set()

        # Initialize queue
        queue = Queue()

        # enqueue starting_vertex in a list
        queue.enqueue([starting_vertex])

        # while there is path in queue
        while queue.size():
            # dequeue path
            path = queue.dequeue()

            # get the last vertex in the dequeued path
            last_vertex = path[-1]

            # if last vertex is not already visited
            if last_vertex not in visited:
                # loop through the neighbors of the last_vertex
                for neighbor in self.vertices[last_vertex]:
                    # create new path list
                    new_path = list(path)
                    # append all the neighbors of current vertex to list
                    new_path.append(neighbor)
                    # check if the current neighbor is the destination
                    if neighbor == destination_vertex:
                        # return the new path
                        return new_path
                    # enqueue the new path
                    queue.enqueue(new_path)
                # add the last vertex to visited
                visited.add(last_vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create set to hold visited vertex
        visited = set()

        # Initialize stack
        stack = Stack()

        # push starting_vertex in a list
        stack.push([starting_vertex])

        # while there is path in stack
        while stack.size():
            # pop path
            path = stack.pop()

            # get the last vertex in the dequeued path
            last_vertex = path[-1]

            # if last vertex is not already visited
            if last_vertex not in visited:
                # loop through the neighbors of the last_vertex
                for neighbor in self.vertices[last_vertex]:
                    # create new path list
                    new_path = list(path)
                    # append all the neighbors of current vertex to list
                    new_path.append(neighbor)
                    # check if the current neighbor is the destination
                    if neighbor == destination_vertex:
                        # return the new path
                        return new_path
                    # pop the new path
                    stack.push(new_path)
                # add the last vertex to visited
                visited.add(last_vertex)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
