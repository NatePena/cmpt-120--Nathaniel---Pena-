'''
Assignment #4:
    Tests the different primitive data types and if the student has assigned the proper type.
@author Kevin Hayden
@date 2023-02-04
@org Marist College - Department of Computing Science
'''

# define a variable called my_int and assign it an integer value.
my_int = 3
# define a variable called my_float and assign it a float value.
my_float = 3.14
# define a variable called my_bool and assign it a boolean value.
my_bool = True 
# define a variable called my_str and assign it a str value.
my_str = "Spam Eggs"
# define a variable called my_list and assign it a list value.
my_list = [1, 2, 3]
# define a variable called my_dict and assign it a dict value.
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_bool = True

print("Value of my_dict:", my_dict)
print("Data type of my_dict:", type(my_dict))

print("Value of my_bool:", my_bool)
print("Data type of my_bool:", type(my_bool))

class TestTyping:

    def test_00(self):
        assert type(my_int).__name__ == "int"

    def test_01(self):
        assert type(my_float).__name__ == "float"

    def test_02(self):
        assert type(my_bool).__name__ == "bool"

    def test_04(self):
        assert type(my_str).__name__ == "str"

    def test_05(self):
        assert type(my_list).__name__ == "list"

    def test_06(self):
        assert type(my_dict).__name__ == "dict"
        