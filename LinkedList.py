# Linked List.

"""------------------------------------------------------------
The Item class will contain the value of the item and the index
of the Item which follows.
------------------------------------------------------------"""
class Item():

    def __init__ (self, value, to):

        self.value = value # Stores the value.
        self.to = to # Stores the index of the next value.




"""------------------------------------------------------------
# The class which contains the linked list. This is where
items will be added and removed from the list. There is also a
search function which returns a boolean value based on whether
the list contains the value or not.

Parameters: data_type - the type which the array will hold.
            length - how many slots in the array.
            values_to_add - values to add to the array on
                            creation.
------------------------------------------------------------"""
class LinkedList():

    # Constructor.
    def __init__(self, data_type, length, values_to_add = None):

        # The linked list.
        self.__size = length
        self.__values = [None] * length
        self.__type = data_type
        self.__setup()


        # Adding values if there are any to add.
        if values_to_add != None:
            self.add(values_to_add)


    """------------------------------------------------------------
    Sets up the start pointer and the free pointer. Start pointer
    starts at 1 so that the program knows to stop when the pointer
    is equal to 0.
    ------------------------------------------------------------"""
    def __setup(self):
        
        # Default values.
        self.__start = 1
        self.__free = 0


    """------------------------------------------------------------
    Public method for adding to the list. Checks to see if the list
    is full before inserting the value.
    
    Paramater 'value', can either be a list or a single value.
    ------------------------------------------------------------"""
    def add(self, value):
        
        # Checking to see if the List is full before adding.
        if self.isFull():
            raise Exception("Error: Tried adding to Linked List but List was full.")

        # Checking to see if it is a list to add.
        if type(value) == list:
            for each_item in value:
                self.__insert(each_item)

        # Adding individual item to the list.
        else:
            self.__insert(value)


    """------------------------------------------------------------
    Private method for inserting the item. It checks to see if the
    value is of the correct type before adding. It also checks to
    see if the list is empty so that it can just add the value to
    the start. It then checks to see if the value should go BEFORE
    the start so the start pointer can be updated correctly.
    Afterwards it traverses the linked list until the value to
    add is less than or equal or 
    ------------------------------------------------------------"""  
    def __insert(self, item):
                
        # Making sure they're adding a value which is of equal type to the linked list.
        if type(item) is not self.__type:
            raise Exception("Error: Expected '" + self.__type.__name__ +"': got '" + type(item).__name__ + "'.")
        
        if self.isEmpty():
            self.__values[self.__free] = Item(item, 0)
            self.updateFreePointer()

        else:

            # If the item should go before the item at the start.
            if item <= self.__values[self.__start - 1].value:

                self.__values[self.__free] = Item(item, self.__start)
                self.__start = self.__free + 1
                self.updateFreePointer()

    
            else:
                current = self.__start
                lastItemIndex = current - 1

                
                while True:
                    
                    if item <= self.__values[current - 1].value:

                        self.__values[self.__free] = Item(item, current)
                        self.__values[lastItemIndex].to = self.__free + 1
                        self.updateFreePointer()
                        break

                    else:

                        lastItemIndex = current - 1
                        current = self.__values[current - 1].to

                        if current == 0:

                            self.__values[self.__free] = Item(item, 0)
                            self.__values[lastItemIndex].to = self.__free + 1
                            self.updateFreePointer()
                            break


    """------------------------------------------------------------
    Public method for removing values from the list. Only removes
    one occurance of each value.
    Parameter 'target', can be a list or a value.
    ------------------------------------------------------------"""
    def remove(self, target):
        
        # Checking to see if it is a list to add.
        if type(target) == list:
            for each_item in target:
                # Checking to see if the List is Empty.
                if self.isEmpty():
                    raise Exception("Error: Cannot remove from empty list.")
                
                self.__delete(each_item)

        else:
            # Checking to see if the List is Empty.
            if self.isEmpty():
                raise Exception("Error: Cannot remove from empty list.")
            
            self.__delete(target)


    """------------------------------------------------------------
    Deletes a single item from the array. Checks to see if the
    start value is the target to be removed. If yes, resets the
    array. If not it traverses the list until the value is found.
    Makes sure to check to see if the list is empty before trying
    to remove another value.
    ------------------------------------------------------------"""
    def __delete(self, target):

        # Making sure they're removing a value which is of equal type to the linked list.
        if type(target) is not self.__type:
            raise Exception("Error: Expected '" + self.__type.__name__ + "': got '" + type(item).__name__ + "'.")


        if self.__values[self.__start - 1].value == target:
            self.clear()
                
        else:
            current = self.__start
            lastItemIndex = current - 1

            while current != 0:
                if self.__values[current - 1].value == target:

                    self.__values[lastItemIndex].to = self.__values[current - 1].to
                    self.__values[current - 1] == None
                    break
                    
                else:

                    lastItemIndex = current - 1
                    current = self.__values[current - 1].to


    """------------------------------------------------------------
    Public method for removing all the items in the list.
    Parameter 'target', can either be a list or a value. Makes
    sure to check to see if the list is empty before trying to
    remove another value.
    ------------------------------------------------------------"""
    def removeAll(self, target):

        # Checking to see if it is a list to add.
        if type(target) == list:
            for each_item in target:

                # Checking to see if the List is Empty.
                if self.isEmpty():
                    raise Exception("Error: Cannot remove from empty list.")
                
                self.__deleteAll(each_item)

        # Adding individual item to the list.
        else:
            # Checking to see if the List is Empty.
            if self.isEmpty():
                raise Exception("Error: Cannot remove from empty list.")
        
            self.__deleteAll(target)


    """------------------------------------------------------------
    Removes every occurance of the value the user wants to delete.
    Checks every value in the array and if it is a target value it
    removes it and updates the 'to', value of the previous Item.
    ------------------------------------------------------------"""  
    def __deleteAll(self, target):
        
        # Checking to see if the List is Empty.
        if self.isEmpty():
            raise Exception("Error: Cannot remove from empty list.")

        # Making sure they're removing a value which is of equal type to the linked list.
        if type(target) is not self.__type:
            raise Exception("Error: Expected '" + self.__type.__name__ +"': got '" + type(item).__name__ + "'.")


        if self.__values[self.__start - 1].value == target:

            current = self.__start

            while self.__values[current - 1].value == target:

                self.__start = self.__values[current - 1].to
                self.__values[current - 1] = None
                current = self.__start

        else:

            current = self.__start
            lastItemIndex = current - 1

            while current != 0:

                if self.__values[current - 1].value == target:
                    
                    beginning = lastItemIndex
                    while self.__values[current - 1].value == target:
                        
                        self.__values[beginning].to = self.__values[current - 1].to
                        lastItemIndex = current - 1
                        current = self.__values[current - 1].to
                        self.__values[lastItemIndex] = None


                else:

                    lastItemIndex = current - 1
                    current = self.__values[current - 1].to
                    

    """------------------------------------------------------------
    Finds the next None value and sets the free pointer to the
    index of that None.
    ------------------------------------------------------------"""
    def updateFreePointer(self):

        if self.isFull() is False:
            self.__free = self.__values.index(None)
            
        else:
            self.__free = None
    

    """------------------------------------------------------------
    Returns false if there is a None somewhere in the list because
    that means the list is not full.
    ------------------------------------------------------------"""
    def isFull(self):
        
        if None in self.__values:
            return False

        return True


    """------------------------------------------------------------
    Returns true if there are no values in the list. Returns false
    if there are.
    ------------------------------------------------------------"""
    def isEmpty(self):

        if self.__values[self.__start - 1] == None:
            return True

        return False



    """------------------------------------------------------------
    Appends values to an array so that the values are in ascending
    order. Useful for binary searching the list multiple times so
    long as the list does not change between searches.
    ------------------------------------------------------------"""
    def getValuesAscending(self):

        
        current = self.__start
        ordered = []
            
        if (not self.isEmpty()):
            while current != 0:

                ordered.append(self.__values[current - 1].value)
                current = self.__values[current - 1].to


        return ordered



    """------------------------------------------------------------
    Inserts each value to the beginning of the array so it is in
    order of highest to lowest. Useful for binary searching the
    list multiple times so long as the list does not change between
    searches.
    ------------------------------------------------------------"""
    def getValuesDecending(self):

        current = self.__start
        ordered = []
            
        if (not self.isEmpty()):
            while current != 0:

                ordered.insert(0, self.__values[current - 1].value)
                current = self.__values[current - 1].to

        return ordered



    """------------------------------------------------------------
    Fetches the values as they lie but removes None types.
    ------------------------------------------------------------"""
    def getValues(self):

        if (not self.isEmpty()):
            unordered = []
            for item in self.__values:

                try:
                    unordered.append(item.value)
                except:
                    pass

            return unordered



    """------------------------------------------------------------
    Returns the index of the target in the unordered array. Returns
    None if not found.
    ------------------------------------------------------------"""
    def search(self, target):

        if (not self.isEmpty()):
            current = self.__start

            while current != 0:
                if self.__values[current - 1].value == target:
                    return current - 1

                current = self.__values[current - 1].to
                
            
        return None


    """------------------------------------------------------------
    Sets every value in the array to None.
    ------------------------------------------------------------"""
    def clear(self):
        self.__values = [None] * self.__size
        self.__setup()



    """------------------------------------------------------------
    Gets the size of the array.
    ------------------------------------------------------------"""
    def getSize(self):
        return self.__size
