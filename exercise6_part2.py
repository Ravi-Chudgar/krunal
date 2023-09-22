class ProcessMethodMeta(type):
    def __init__(cls, name, bases, dct):
        if 'process' not in dct or not callable(dct['process']):
            raise TypeError(f"{name} must have a 'process' method taking 3 arguments.")
        else:
            # Ensure the 'process' method takes 3 arguments
            process_args = dct['process'].__code__.co_varnames
            if len(process_args) != 4 or process_args[0] != 'self':
                raise TypeError(f"{name}'s 'process' method must take exactly 3 arguments (including 'self').")
        super(ProcessMethodMeta, cls).__init__(name, bases, dct)

# Example usage of the metaclass
class MyClassWithProcessMethod(metaclass=ProcessMethodMeta):
    def process(self, arg1, arg2, arg3):
        # Implementation code for 'process' method
        result = arg1 + arg2 + arg3
        return result

# This class will raise a TypeError since it doesn't have a 'process' method.
class MyClassWithoutProcessMethod(metaclass=ProcessMethodMeta):
    pass

# This class will raise a TypeError since its 'process' method doesn't take 3 arguments.
class MyClassWithIncorrectProcessMethod(metaclass=ProcessMethodMeta):
    def process(self, arg1, arg2):
        pass

# Testing the metaclass
try:
    obj1 = MyClassWithProcessMethod()
    result = obj1.process(1, 2, 3)
    print("Result from MyClassWithProcessMethod:", result)
except TypeError as e:
    print(e)

try:
    obj2 = MyClassWithoutProcessMethod()
except TypeError as e:
    print(e)

try:
    obj3 = MyClassWithIncorrectProcessMethod()
except TypeError as e:
    print(e)
