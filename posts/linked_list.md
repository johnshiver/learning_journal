
One of the hardest parts about becoming a web developer without a CS degree
(aside from the obvious bits) is learning data structures and algorithms on your own.
A lot of self taught programmers dont realize the importance of these concepts until they
already have an interview lined up, and by then it’s already too late!
I was fortunate enough to attend the CodeFellows Python Dev Accelerator,
where a section of the curriculum was dedicated to basic data structures and algorithms,
but 8 whirlwind weeks were not enough to solidify these concepts so I thought it’d be beneficial,
both for my own edification and for other budding Pythonistas, to write a series on
basic data structures, starting with the linked list.

In its most basic form a linked list is a string of nodes, sort of like a string of pearls,
with each node containing both data and a reference to the next node in the list
(note: this is a singly linked list. the nodes in a doubly linked list will contain references
to both the next node and the previous node).
The main advantage of using a linked list over a simlar data structure, like the static array,
is the linked list’s dynamic memory allocation: if you dont know the amount of data you want to
store before hand, the linked list can adjust on the fly*.  Of course this advantage comes at a price: dynamic memory allocation requires more space and commands slower look up times.

_*In practice this means certain insertions are more expensive. For example,
if the list initially allocates enough space for 8 nodes, on the ninth insertion
the list will have to double it’s allocated space to 16 and copy over the original
8 nodes, a more expensive operation than a normal insertion._

##The node

The node is where data is stored in the linked list (they remind me of those plastic easter eggs that hold treats)
Along with the data each node also holds a pointer, which is a reference to the next node in the list.  Below is a simple implementation.


    ::python
    class Node(object):

        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def set_next(self, new_next):
            self.next_node = new_next


The node initializes with a data point, it’s pointer set to None by default
(this is because the first node inserted into the list will have nothing to point at!).
We also add a few convenience functions: one that returns the stored data,
another that returns the node the current node points at,
and a function to reset the pointer to a new node.  These will come in
handy when we implement the LinkedList.

##The Linked List

My simple implementation of a linked list includes the following methods:

- Insert: inserts a new node into the list
- Size: returns size of list
- Search: searches the list for a node with the requested data and returns that if found, otherwise raises an error
- Delete: searches list for node with requested data and removes it if found, otherwise raises an error

###The Head of the List

The first architectural piece of the linked list is the ‘head node’,
which is simply the top node in the list. When the list is first initialized it has no nodes,
so the head is set to None. (Note: the linked list doesnt necessarily require a node to initialize,
the head argument will default to None if a node is not provided)

    ::python
    class LinkedList(object):
        def __init__(self, head=None):
            self.head = head

###Insert

This insert function takes data, initializes a new node with the given data,
and adds it to the list. Technically you can insert a node anywhere in the list,
but the simplest way to do it is to place it at the head of the list
and point the new node at the old head (sort of pushing the other nodes down the line).

As for time complexity, this implementation of insert is constant O(1) (efficient!).
This is because the insert function, no matter what, will always take the same amount
of time: it can only take one data point, it can only ever create one node, and the new
node doesnt need to interact with all the other nodes in the list, the inserted node will
only ever interact with the head.


    ::python
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

###Size

The size method is very simple, it basically counts nodes until it cant find anymore,
and returns how many nodes it found. The method starts at the head node, iterates through
the list until it reaches the end (current will be None when it reaches the end)
while keeping track of how many nodes it has seen.

The time complexity of size is O(n) because each time the method is called it will always
visit every node in the list but only interact with them once, so n * 1 operations.


    ::python
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

###Search

Search is actually very similar to size, but instead of travsering the whole list
of nodes it checks at each stop to see whether the current node has the requested
data.  If the method goes through the entire list but still hasnt found the data,
it raises a value error, and tells the user that the data is not in the list.

The time complexity of search is O(n) in the worst case
(you often hear about best case / average case / worst case for Big O analysis.
For this purpose of this blog post, we'll assume worst case is the one we care about it, because
it often is!)


    ::python
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current


###Delete

You'll be happy to know that delete is very similar to search! The delete method
traverses the list in the same way that search does, but in addition to keeping
track of the current node, the delete method also remembers the last node it visited.
When delete finally arrives at the node it wants to delete, it simply removes it from the
chain by "leap frogging" it.  By this I mean that when the delete method reaches the node it wants
to delete, it looks at the last node it visited (the 'previous' node), and resets that previous
node's pointer so that, rather than pointing to the soon-to-be-deleted node, it will point to the
next node in line.  Since no nodes are pointing to the poor node that is being deleted, it is
effectively removed from the list!


The time complexity for delete is also O(n), because in the worst case it will visit
every node, interacting with each node a fixed number of times.


    ::python
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

That wraps up the linked list implementation! If I made a mistake please shoot me an email.
At the bottom I've provided a link to the source code and have also added a test suite
that tests all the functionality described in this blog post. Happy coding!

[LinkedList Source](https://github.com/johnshiver/algorithms/blob/master/linked_list/linked_list.py)
[LinkedList Tests](https://github.com/johnshiver/algorithms/blob/master/linked_list/test_linked.py)


