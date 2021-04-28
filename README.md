# Grocery Store Project 
 My Base Code


Grocery stores often have a difficult task: they must determine how many employees to hire to staff checkout lines during varying levels of customers throughout the day. Too few open lines means customers spend time angrily waiting; too many, and the store loses money paying its employees. It's also important to get the right mix of regular and express checkout lines, and perhaps even self-serve lines. Which combination is best depends on what kind of customers the store has.

In this assignment, you'll build an event-driven simulation for a grocery store, which will model customers using different types of checkout lines. Your finished product will be able to set up the simulation with data from file inputs, simulate a sequence of events, and report timing statistics after the simulation is complete that will help determine how successful the checkout line set-up was for that set of customer arrivals.

Simulation description
Read through the following description carefully. Your overall task for this assignment will be to create a program which fulfills the requirements here.

The grocery store
Here we describe all the things that your simulation will keep track of. There are many other things that it won't keep track of that might be important, such as which customers have children with them and how tired each cashier is, but are beyond the scope of the simulation.
Simulate only what we describe here.

A grocery store must keep track of all customers and checkout lines in the store, giving each customer a unique string identifier.

Customers go to a checkout line to pay for their items. The number of items influences how long it takes for the customer to check out, but what those items are does not, and so the simulation should only keep track of the number of items each customer has.

Every checkout line can hold some number of waiting customers. There are three different types of checkout lines:

Cashier checkout line. A customer with n items requires n + 7 seconds to checkout. Any customer can join the line, if there is room.
Express checkout line. A customer with n items requires n + 4 seconds to checkout, and customers can only enter the line if they have fewer than 8 items.
Self-serve checkout line. A customer with n items requires 2n + 1 seconds to checkout. Any customer can join the line, if there is room.
Lines are referred to by a unique index, with the following order: cashier lines, express lines, and then self-serve lines. For example, if there are 3 cashier lines, 2 express lines, and 10 self-serve lines, then:

lines 0-2 are cashier lines
lines 3-4 are express lines
lines 5-14 are self-serve lines
(This restriction is meant to make it easy to store the lines in a list.)

A grocery store starts the simulation with a fixed number of each type of checkout line, all of which are open and can serve customers. However, over the course of the simulation some checkout lines may close (see next section).

Events
We are building an event-driven simulation, a type of simulation which is governed by a set of events that must happen at particular times, each one changing the state of the simulation and possibly spawning new events. There are four different types of events which you must define:

A new customer joins a checkout line. (See below for details about which line they should join.)
A customer begins checking out (i.e., she has reached the front of the line and is the one whose items are being processed).
A customer finishes checking out (i.e., she has finished paying and leaves the store).
A line closes. All customers who were in the line must join a new line, except the first customer in the line. No new customers may join the line after it has closed.
Events all have an associated timestamp, a positive integer representing when that event occurs, in seconds. The simulation starts at time 0.

The simulation starts by reading events from a file and storing them in a container. It then repeatedly gets the next unprocessed event (the one with the smallest timestamp) and processes it, updating the state of the store.

What makes the simulation really interesting is that sometimes events spawn new events:

If a new customer joins an empty checkout line, a new "checking out" event is added with the same timestamp as the join event.
If a customer begins checking out, a new "finsh checking out" event is added with the same timestamp as the "begin" timestamp, plus the appropriate amount of time based on the type of checkout line and the number of items the customer has.
If a customer finishes checking out, the next customer in the line (if there is one) gets a "begin checking out" event with the same timestamp as the "finish" event.
If a line closes, there is one new "customer joins" event per customer in the checkout line after the first one. The new events should be spaced 1 second apart, with the last customer in the line having the earliest "new customer" event, which is the same as the "line close" event.

Example: suppose there is a checkout line with customers A, B, C, and D, with A being the first customer in the line. Suppose this line closes at time 30. Three new events are spawned: D has a new customer event at time 30, C has a new customer event at time 31, and B has a new customer event at time 32. Customer A remains in the line.

Algorithm for assigning customers to lines
As you might expect, the algorithmically interesting part of this simulation is deciding how to assign new customers to lines. For the purpose of this assignment, we will use one simple algorithm. When a new customer joins, he or she always joins the open line with the fewest number of customers that he or she is allowed to join, choosing the one with the lowest index (as represented by the grocery store) if there is a tie.

You can assume there is always at least one open line that has space for the customer.

Statistics
When the simulation is over, it should report three statistics: the total number of customers who checked out, the timestamp of the final event, and the maximum time a customer spent waiting in line.

(Of course, there are many more interesting statistics you could report, but we had to stop somewhere!)

Starter code
Download this tar file containing a bunch of starter files for this assignment, and extract its contents into assignments/a1. We will guide you through them as you work on the different parts of this assignment.

Task 1: Modelling a Grocery Store
Your first task is to enable the creation of a grocery store model based on a configuration file. This part will get you designing and implementing your own classes (for the store, customers, and different kinds of checkout lines).

The simulation program uses two input files: config.json and store.py. The former stores the configuration of a grocery store as a set of key-value pairs:

cashier_count: the number of standard cashier checkout lines
express_count: the number of express checkout lines
self_serve_count: the number of self-serve checkout lines
line_capacity: the maximum number of customers allowed in each line (all lines have the same capacity)
In store.py, we have provided a skeleton class GroceryStore, and put starter code into the constructor to read in data from a configuration file into a dictionary.

Your task is to complete the implementation of GroceryStore, and design and implement classes for customers and the different kinds of checkout lines in the store. Note that you may create some methods now, but add or remove methods later as you work through the assignment - this is perfectly fine.

Task 2: Events
We have provided an Event API for you in event.py. Read through the abstract class documentation carefully. Your first job is to use inheritance to create subclasses for specific types of events which follow the API.

In the course of implementing the events, you might find that you need to add or modify code you've written in Part 1 - again, that's totally fine!

At the bottom of the file, you must also implement the function create_event_list, which reads in events from a file. It must handle files that have the following format:

there is one event per line
only "new customer" and "line close" events appear
the "new customer" event has the following format:

<timestamp> Arrive <cid> <num_items>
the "line close" event has the following format:

<timestamp> Close <line_index>
You can see an example of a valid file format in events.txt. You do not need to do error-checking for this function: you may assume (as a precondition) that this file is in a valid format.

Task 3: Simulation
Take a look now at the simulation.py file, which contains a class skeleton for the simulation. Your main job will be to implement the run method.

The main structure of the run method should look like:

add events to self._events

while not self._events.is_empty():
    event = remove event from self._events
    process event
    add new events to self._events
While we could use a Python list to keep track of the events, that's too powerful for our purposes. What we really need is a simple data type which allows us only to insert objects and remove them one at a time.

This should remind you of our Container ADT; however, neither the Stack nor Queue ADTs we cover in the course work, because we don't want to remove events based on when we inserted them, but rather based on their timestamp.

This leads us to a new ADT: the PriorityQueue, which supports the following actions:

determine whether the priority queue is empty
insert an item with a given priority
remove the item with the highest priority
Look at container.py, which contains the Container abstract class we covered in lecture, as well as a new, partially-complete PriorityQueue class. You must complete the add implementation according to its docstring. (Notice that we're essentially using a sorted list to implement this class; in later courses, you'll learn about a much more efficient implementation called heaps.)

Once this is done, turn your attention to the GroceryStoreSimulation class and implement its two methods. Note that you should have an _events attribute which stores a priority queue containing all of the unprocessed events.

We strongly recommend that you start by making sure you can process all the events - perhaps implement a __str__ for each of the events and print out events as they're being processed.

Statistics
Your run method must return a dictionary of statistics, with the following keys:

'num_customers': the total number of customers in the simulation.
'total_time': the timestamp of the last event (which should usually be a "finish checkout" event).
'max_wait: the maximum amount of time a customer waited. Customer wait time is defined as the difference in times between when the customer first joined a line and when the customer finished checking out. (Note: if a customer joins and line and the line closes, and then joins another line, wait time is calculated based on the customer joining the first line, not the second one.)
You can assume there is always at least one customer in the simulation.
