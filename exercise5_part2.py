# class MetaInherList(type):
#     def __init__(cls, name, bases, dct):
#         # Ensure that the built-in list class is one of the base classes
#         bases = (list,) + bases
#         super(MetaInherList, cls).__init__(name, bases, dct)

# # Define the class with the metaclass
# class ForceToList(metaclass=MetaInherList):
#     pass


class MetaInherList(type):
    def __getitem__(cls, item):
        return type.__getitem__(cls, item)()

class ForceToList(list, metaclass=MetaInherList):
    pass

# Example usage:
#my_list = ForceToList([1, 2, 3])
my_list = [1, 2, 3]
data=ForceToList(my_list)
print(data)  # Output: [1, 2, 3]
