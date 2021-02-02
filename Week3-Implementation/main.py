#  Author: Marthely237 & luckyjohn-rwanda



# Initializing constructor
class Simple_array:
    def __init__(self, array=[14, 22, 41, 9, 5, 22]):
        self.array = array



# The method to print the length of our list
def length(self):
    print(len(self.array))


# The method to print a specific item in our list
def get_value(self):
    for n, i in enumerate(self.array):
        if i == 1:
            print(self.array[n])


# The method to replace an item with a new item
def replace(self):
    for n, i in enumerate(self.array):
        if i == 4:
            self.array[n] = 3
            return self.array



# Inherit Subclass
class Dynamic_array(Simple_array):
    def __init__(self, array=[14, 22, 41, 9, 5, 22]):
        super().__init__(array=[14, 22, 41, 9, 5, 22])




    # The method to add an item to our list
    def Add_list(self):
        self.array.append(5)
        print(self.array)


    # The method to delete an item from our list
    def del_list(self):
        del self.array[3]
        print(self.array)


# Space complexity: O(1)
# Time complexity: O(1)

length_array = Dynamic_array()


length_array.del_list()
