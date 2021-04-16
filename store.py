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

class Customer(GroceryStore):
    ""
    def __init__(self):

        pass

class exp_checkout(GroceryStore):
    ""
    def __init__(self,config):
        self.line_cap =config['line_capacity']

        pass

class standard_checkout(GroceryStore):
    ""
    def __init__(self,config):
        self.line_capacity=config['line_capacity']
        pass

class self_checkout(GroceryStore):
    ""
    def __init__(self,config):
        self.line_cap=config['line_capacity']
        pass



# You can run a basic test here using the default 'config.json'
# file we provided.
if __name__ == '__main__':
    store = GroceryStore('config.json')
    # Execute some methods here
