
One of the hardest parts about becoming a web developer without a CS degree (aside from the obvious bits) is learning data structures and algorithms on your own.  A lot of self taught programmers dont realize the importance of these concepts until they already have an interview lined up, and by then it’s already too late! I was fortunate enough to attend the CodeFellows Python Dev Accelerator, where a section of the curriculum was dedicated to basic data structures and algorithms, but 8 whirlwind weeks were not enough to solidify these concepts so I thought it’d be beneficial, both for my own edification and for other budding Pythonistas, to write a series on basic data structures, starting with the linked list.

In its most basic form a linked list is a string of nodes, sort of like a string of pearls,with each node containing both data and a reference to the next node in the list (note: this is a singly linked list. the nodes in a doubly linked list will contain references to both the next node and the previous node) .  The main advantage of using a linked list over, say, a static array, is the linked list’s dynamic memory allocation: if you dont know the amount of data you want to store before hand, the linked list can adjust on the fly*.  Of course this advantage comes at a price: dynamic memory allocation requires more space and commands slower look up times.

*In practice this means certain insertions are more expensive. For example, if the list initially allocates enough space for 8 nodes, on the ninth insertion the list will have to double it’s allocated space to 16 and copy over the original 8 nodes, a more expensive operation than a normal insertion.

##The node

The node is where data is stored in the linked list (I like to think of them as little treasure chests of knowledge) Along with the data each node also holds a pointer, which is a reference to the next node in the list.  Below is a simple implementation.


    ::python
    class Node(object):
        def __init__(self, date): 
            self.data = data
            self.nextNode = None

The node initializes with a data point, it’s pointer set to None by default (this is because the first node inserted into the list will have nothing to point at!).

##The Linked List

My simple implementation of a linked list includes the following methods:

- Insert: inserts a new node into the list
- Search: searches the list for a given node, returns that node if found otherwise returns a message indicating that it is not in the list
- Size: returns size of list
- Delete: Takes a node as an argument, if that node is in the list it is removed

##The Head of the List

The last architectural piece of the linked list is the ‘head node’, which is simply the top node in the list. When the list is first initialized it has no nodes, so the head is set to None. (Note: the linked list doesnt necessarily require a node to initialize, the head argument will default to None if a node is not provided. This will be useful later when we use recursion to search the list)

    ::python
    class LinkedList(object):
        def __init__(self, head=None):
            self.head = head 

###Insert

Technically you can insert a node anywhere in the list, but the simplest way to do it is to insert a new node at the head of the list and point the new node at the old head.   As for time complexity, this implementation of insert is constant O(1). This is because the operation only requires interaction with the node being inserted, each time the insert method is called it will only ever interact with the inserted node.  Therefore insert is very efficient!

    ::python
    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node

###Search

Searching a linked list can be done iteratively or recursively.  I chose a recursive implementation because it is a little more fun :D The basic idea is to check whether the head of the list is the node you’re looking for, if it is return the head node and if not call the search method again but with the second node as the head of the list.  If there is no second node (i.e. you are down to one node and you haven’t found the one you want), the method raises a value error and says the node is not in the list.

The time complexity of search is O(n): in the worst case scenario the search method will look at each node before resolving. The space complexity is worse, because on each recursive call a new list is created whose size is n-1 compared to the last call.

    ::python
    def search(self, lList, Node):
        if self.head == Node:
            return self.head
        else:
            if lList.head.nextNode:
                self.search(LinkedList(lList.head.nextNode), Node)
            else:
                raise ValueError("Node not in Linked List")

###Size

The size method is similar to search. The method starts at the head node and iterates through the list until it reaches the end, keeping track of how many nodes it has seen.  The time complexity of size is also O(n) because in order to know the size it must visit each node in the list.

    ::python
    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.nextNode
        return size

###Delete 

Delete is the trickiest method to implement on the linked list.  The obvious first thing to do is to check whether the list is empty, you obviously cant delete an item from an empty list! This can be done by checking whether the size of the list is 0, raising a ValueError if it is.

If the list isnt empty (and assuming the node is in the list*), deleting a node is simply a matter of ‘leap frogging’ the deleted node by removing all references to it.  To do this requires that you keep track of the node you are currently on, the ‘current’ node, and the node you just looked at, the ‘previous’ node.  If the current node is the node you want to delete, move the previous node’s pointer to the node after the current node, ‘leap frogging’ the current node.  Since there are no longer any nodes pointing to the current node it is no longer in the list.

The time complexity for delete is O(n), because in the worst case scenario the node you want to delete will be the last item in the list, and in order to get there you’ll have to look at all the nodes before it, or n nodes.

*to make sure the node is in the list, I check whether the current node has a value.  If is is None a ValueError is raised.

    ::python
    def delete(self, node):
        if self.size() == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.nextNode
            if previous is None:
                self.head = current.nextNode
            else:
                previous.nextNode = current.nextNode

That wraps up the linked list implementation! If I made a mistake please leave a comment or shoot me an email.  In the next post I will analyze common linked list interview questions.
