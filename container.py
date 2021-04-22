"""Assignment 1 - Container (Task 3)

This file contains the classes representing the Container
and Priority Queue data types.

You are responsible for completing the 'add' method of
PriorityQueue.
"""


class Container:
    """A container that holds objects.

    This is an abstract class. Only child classes should be instantiated.
    """

    def add(self, item):
        """Add <item> to this Container.

        @type self: Container
        @type item: object
        @rtype: None
        """
        raise NotImplementedError

    def remove(self):
        """Remove and return a single item from this Container.

        @type self: Container
        @rtype: object
        """
        raise NotImplementedError

    def is_empty(self):
        """Return True iff this Container is empty.

        @type self: Container
        @rtype: bool
        """
        raise NotImplementedError


class PriorityQueue(Container):
    """A queue of items that operates in priority order.

    Items are removed from the queue according to priority; the item with the
    highest priority is removed first. Ties are resolved in FIFO order,
    meaning the item which was inserted *earlier* is the first one to be
    removed.

    Priority is defined by the rich comparison methods for the objects in the
    container (__lt__, __le__, __gt__, __ge__).

    If x < y, then x has a *HIGHER* priority than y. (Intuitively, "priority 1"
    is more important than "priority 10".)

    All objects in the container must be of the same type.
    """

    # === Private Attributes ===
    # @type _items: list
    #     The items stored in the priority queue.
    #
    # === Representation Invariants ===
    # _items is a sorted list, where the front item is the one with the
    # highest priority.

    def __init__(self):
        """Initialize an empty PriorityQueue.

        @type self: PriorityQueue
        @rtype: None
        """
        self._items = []

    def remove(self):
        """Remove and return the next item from this PriorityQueue.

        Precondition: <self> should not be empty.

        @type self: PriorityQueue
        @rtype: object

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq.remove()
        'arju'
        >>> pq.remove()
        'fred'
        >>> pq.remove()
        'hat'
        >>> pq.remove()
        'mona'
        """
        return self._items.pop(0)

    def is_empty(self):
        """
        Return true iff this PriorityQueue is empty.

        @type self: PriorityQueue
        @rtype: bool

        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.add('fred')
        >>> pq.is_empty()
        False
        """
        return len(self._items) == 0

    def add(self, item):
        """Add <item> to this PriorityQueue.

        @type self: PriorityQueue
        @type item: object
        @rtype: None

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq._items
        ['arju', 'fred', 'hat', 'mona']
        """
        # TODO: Implement this method.
        loc = 0
        if not self._items:
            #print('works fine')
            self._items = [item]

        else:
            for event in self._items:
                # _item contains 3 events with the timestamps
                # 4,8 and 16
                #print(f'{item.timestamp} < {event.timestamp}')
                #print(item.__lt__(event)#)

                if item.__lt__(event):
                    #print(f'{item.timestamp} > {event.timestamp}')
                    #print(item.__lt__(event))
                    break
                #print(loc)
                loc+=1
            self._items.insert(loc,item)
            #print(self._items)
