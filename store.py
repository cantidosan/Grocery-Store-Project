"""Assignment 1 - Grocery Store Models (Task 1)

This file should contain all of the classes necessary to model the entities
in a grocery store.
"""
# This module is used to read in the data from a json configuration file.
import json


class GroceryStore:
    """A grocery store.

    A grocery store should contain customers and checkout lines.

    TODO: make sure you update the documentation for this class to include
    a list of all public and private attributes, in the style found in
    the Class Design Recipe.
    """
    def __init__(self, filename):
        """Initialize a GroceryStore from a configuration file <filename>.

        @type filename: str
            The name of the file containing the configuration for the
            grocery store.
        @rtype: None
        """
        with open(filename, 'r') as file:
            config = json.load(file)

        # <config> is now a dictionary with the keys 'cashier_count',
        # 'express_count', 'self_serve_count', and 'line_capacity'.

        self.checkout_line_list = []
        #open the different checkout counters in the store

        for element in range(config['cashier_count']):
            self.checkout_line_list.append(standard_checkout(config['line_capacity']))

        for element in range(config['express_count']):
            self.checkout_line_list.append(exp_checkout(config['line_capacity']))


        for element in range(config['self_serve_count']):
            self.checkout_line_list.append(self_checkout(config['line_capacity']))




    def  shortest_open_line(self):
        #returns the array of the shortest line in the available checkouts
        #assign shortest_line variable to NOne accounts for the [0] element being close upon
        #first iteration
        shortest_line = None
        #print(self.checkout_line_list)
        for checkout_line in self.checkout_line_list:

            if checkout_line.state != 'OPEN':
                continue
            if shortest_line == None:
                shortest_line = checkout_line
                continue
            if checkout_line.num_cust_in_line() < shortest_line.num_cust_in_line():
                shortest_line = checkout_line

        return shortest_line










class Customer(GroceryStore):
    "initializes a customer instance with three parameters"
    "time_stamp: type (int) cust_id:type (str) num_items: type (int)"

    def __init__(self, cust_id, num_items):

        self.cust_id = cust_id
        self.num_items = num_items

    def __repr__(self):

        #returns the customer unique id and items in their posession as a string

        return str(self.cust_id) + ':' + str(self.num_items)

class exp_checkout(GroceryStore):
    "initializes an express checkoutline instance"

    def __init__(self,line_capacity):

        self.cust_in_line_list = []
        self.line_capacity = line_capacity
        self.state = 'OPEN'

    def line_status(self):

        return self.state

    def num_cust_in_line(self):
        # returns the number of customers currently waiting to begin checkout

        return len(self.cust_in_line_list)

    def checkout_time(self):

       return ((self.cust_in_line_list[0].num_items) + 4)





class standard_checkout(GroceryStore):
    "initializes a standard cashier mounted checkout line"
    def __init__(self,line_capacity):

        self.line_capacity = line_capacity
        self.cust_in_line_list=[]
        self.state = 'OPEN'

    def num_cust_in_line(self):
        # returns the number of customers currently waiting to begin checkout

        return len(self.cust_in_line_list)

    def line_status(self):

        return self.state

    def checkout_time(self):

        return ((self.cust_in_line_list[0].num_items) + 7)



class self_checkout(GroceryStore):
    ""

    def __init__(self,line_capacity):

        self.line_capacity = line_capacity
        self.cust_in_line_list = []
        self.state = 'OPEN'

    def line_status(self):

        return self.state

    def num_cust_in_line(self):
        # returns the number of customers currently waiting to begin checkout

        return len(self.cust_in_line_list)

    def checkout_time(self):

        return ((self.cust_in_line_list[0].num_items)*2 + 1)




# You can run a basic test here using the default 'config.json'
# file we provided.

if __name__ == '__main__':
    store = GroceryStore('config.json')

