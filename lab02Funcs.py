# lab02Funcs.py     Define a few sample functions in Python
# P. Conrad for CMPTGCS 20, Spring 2016


def perimRect(length,width):
   """
   Compute perimiter of rectangle
   >>> perimRect(2,3)
   10
   >>> perimRect(4, 2.5)
   13.0
   >>> perimRect(3, 3)
   12
   >>>
   """
   return -999.99 # stub  @@@ replace this stub with the correct code @@@


def areaRect(length,width):
   """
   compute area of rectangle
   >>> areaRect(2,3)
   6
   >>> areaRect(4, 2.5)
   10.0
   >>> areaRect(3,3)
   9
   >>>
   """
   return -999.99 # stub  @@@ replace this stub with the correct code @@@



# THIS FUNCTION IS CORRECT---it is here as an example

def isList(x):
   """
   returns True if argument is of type list, otherwise False

   >>> isList(3)
   False
   >>> isList([5,10,15,20])
   True
   """
   
   return ( type(x) == list )   # True if the type of x is a list


### @@@ NOW, write a function called isString(x)
### @@@ similar to isList() function above.
### @@@ Note that the Python pre-defined value that stands for the string type is str



def isString(x):
    """"
    return True if x is a string, otherwise False
    """
    
    return "stub" # stub  @@@ replace this stub with the correct code @@@

# The following function is provided for you as an example
# of how to write a Python function involving "or"
# This contains HINTS as to how to do the next function definition.

def isAdditivePrimaryColor(color):
    """
    return True if color is a string equal to "red", "green" or "blue", otherwise False
    >>> isAdditivePrimaryColor("blue")
    True
    >>> isAdditivePrimaryColor("black")
    False
    >>> isAdditivePrimaryColor(42)
    False
    >>>
    """
    
    return ( (color == "red" ) or (color == "green" ) or (color == "blue") )

# NOTE: the following will NOT work for isAdditivePrimaryColor:
#
# def isAdditivePrimaryColor(color):
#   return ( color == "red" or "green" or "blue" )
#
# Try it, and convince yourself that it doesn't work.
# Does it fail to compile, fail to run (python vomit), or just give the
#  wrong answer?    You may be surprised!
# Try it, then try to understand _why_ this doesn't do what you want
# Hints: 'or' is an operator, and it must take operands that are
# either True or False
# (color == "red") is either True or False.  What about the other operands?



### @@@ NOW, write a function called isSimpleNumeric(x)
### @@@ This should return true if x is either an integer (int in Python), or
### @@@   a floating point number (float in Python).  (We'll ignore the 'complex' type
### @@@   for purposes of this function.)
### @@@ Include a comment describing what the function returns 
### @@@ similar to the comments above the other function definitions in this file
### @@@ Hint: combine what you did for isString with the pattern you see
### @@@  at work in isPrimaryColor of combining boolean expressions with "or"


def isSimpleNumeric(x):
   """
   returns True if x is has type int or float; anything else, False 
   >>> isSimpleNumeric(5)
   True
   >>> isSimpleNumeric(3.5)
   True
   >>> isSimpleNumeric("5")
   False
   >>> isSimpleNumeric([5])
   False
   >>> isSimpleNumeric(6.0221415E23)
   True
   >>>
   """
   
   return "stub" # stub  @@@ replace this stub with the correct code @@@
  
