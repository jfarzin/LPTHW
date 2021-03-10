# create a class called Parent
class Parent(object):

    # class Parent has a function called override that calls the self parameter
    def override(self):
        # this function prints PARENT override
        print("PARENT override()")

    # class has a function implicit that calls the self parameter
    def implicit(self):
        # function prints PARENT implicit
        print("PARENT implicit()")
    
    # class has a function called altered that calls the self parameter
    def altered(self):
        # function prints PARENT altered
        print("PARENT altered()")

# create a class called Child that is a Parent
class Child(Parent):

    # class has a function override that calls self parameter
    def override(self):
        # function prints CHILD override
        print("CHILD override()")

    # class has a function called altered that calls self param
    def altered(self):
        # function prints CHILD, BEFORE PARENT altered
        print("CHILD, BEFORE PARENT altered()")
        # call the higher class (Parent) using super with CHild and self params
        # from super (the higher Parent class) call the function altered
        super(Child, self).altered()
        # print CHILD AFTER PARENT altered
        print("CHILD, AFTER PARENT altered()")

# assign dad to the class Parent
dad = Parent()
# assign son to the class Child
son = Child()

# with dad, call the implicit function with self param
dad.implicit()
# with son, call the implicity function with self param
son.implicit()

# with dad, call the override function with self param
dad.override()
# with son, call the override function with self param
son.override()

# with dad, call the altered function with self param
dad.altered()
#with son, call the altered function with self param
son.altered()
