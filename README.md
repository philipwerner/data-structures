# Data Structure
Various data structure written in python by Han Bao and Phillip Werner



# Linked-Lists

Ordered list, where each node has a one way reference to the next.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- Size: O(1)
    - Returns the current size

- Search: O(n)
    - Searches for the given value

- Remove: O(n)
    - Remove the given value

- Display: O(n)
    - Display the current list as a string of tuple

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Doubly-Linked-Lists

Ordered list, where each node has two way reference to its previous and next node.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- Append: O(1)
    - Insert given value to the tail

- Shift: O(1)
    - Remove the tail value

- Remove: O(n)
    - Remove the given value from the list

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Stack

FILO (First In Last Out), where the frist node pushed in is the last node that will be pop.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Queues

FIFO (First In First Out), where the first node enqueued is the first node that will be dequeued.

- Enqueue: O(1)
    - Insert given value to the tail

- Dequeue: O(1)
    - Remove the head value

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Deque

Ordered list, where each node has two way reference to its previous and next node.

- Append: O(1)
    - Insert given value to the tail

- Append_Left : 0(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the tail value

- Pop_Left: 0(1)
    - Remove the head value

- Peek: O(1)
    - Returns the tail value

- Peek_Left: O(1)
    - Returns the head value

- Size: 0(1)
    - Returns the size of the deque

- \__len\__: O(1)
    - Declare len() method which returns the value from self._counter.


# Binheap

Min heap that stores value using min-heap artictiure

- Push: O(N)
    - Insert a value into the heap, perculate up to proper node.

- Pop: O(N)
    - Pop the top value from the heap(min value for min heap)


# Graph (unweighted & directional)

A graph structure where each node can be direct/point to another node.

- nodes: O(n)
    - return a list of all nodes in the graph.

- edges: O(n^2)
    - return a list of all edges in the graph.

- add_node: O(1)
    - add a new node to the graph if not already existed.

- add_edge: O(1)
    - add a new directed edge from the two nodes inputted, add node(s) if not existed.

- del_node: O(n)
    - delete the given node from the graph, raise error if no such node exists.

- del_edge: O(1)
    - delete the edge from inputted nodes(1 to 2), raise error if no such edge exists.

- has_node: O(1)
    - return true if given node is in the graph, false if it's not.

- neighbors: O(1)
    - return a list of all nodes the given node can reach(directed to).

- adjacent: O(1):
    - return true if an edge exist between node 1 and node 2 (either direction), false otherwise.
