"""Assignment 1 - Grocery Store Simulation (Task 3)

This file should contain all of the classes necessary to model the different
kinds of events in the simulation.
"""
# Feel free to add extra imports here for your own modules.
# Just don't import any external libraries!
from container import PriorityQueue
from store import GroceryStore
from event import Event, create_event_list, Cust_arrive, Line_close


class GroceryStoreSimulation:
    """A Grocery Store simulation.

    This is the class which is responsible for setting up and running a
    simulation.
    The API is given to you: your main task is to implement the two methods
    according to their docstrings.

    Of course, you may add whatever private attributes and methods you want.
    But because you should not change the interface, you may not add any public
    attributes or methods.

    This is the entry point into your program, and in particular is used for
    autotesting purposes. This makes it ESSENTIAL that you do not change the
    interface in any way!
    """

    # === Private Attributes ===
    # @type _events: PriorityQueue[Event]
    #     A sequence of events arranged in priority determined by the event
    #     sorting order.
    # @type _store: GroceryStore
    #     The grocery store associated with the simulation.
    def __init__(self, store_file):
        """Initialize a GroceryStoreSimulation from a file.

        @type store_file: str
            A file containing the configuration of the grocery store.
        @rtype: None
        """
        self._events = PriorityQueue()
        self._store = GroceryStore(store_file)

    def run(self, event_file):
        """Run the simulation on the events stored in <event_file>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: GroceryStoreSimulation
        @type event_file: str
            A filename referring to a raw list of events.
            Precondition: the event file is a valid list of events.
        @rtype: dict[str, object]
        """
        # Initialize statistics
        stats = {
            'num_customers': 0,
            'total_time': 0,
            'max_wait': -1
        }

        initial_events = create_event_list(event_file)
        print(self._events)
        for event in initial_events:
            self._events.add(event)


        # TODO: Process all of the events, collecting statistics along the way.

        # cycle through every initial event
        print(self._events.is_empty())
        while not self._events.is_empty():

            event = self._events.remove()

            print('enter the while loop')
            # checking what type of events is being processed new customer or line closure
            if isinstance(event, Cust_arrive):
                shortest_line = 0
                for line in self._store.checkout_line_list:
                    print(line)
            # needs a checkoutline instance for .....
            elif isinstance(event, Line_close):
                " "

        return stats


# We have provided a bit of code to help test your work.
if __name__ == '__main__':
    sim = GroceryStoreSimulation('config.json')
    final_stats = sim.run('events.txt')
    print(final_stats)
