list = ['GUVI', 'learning', 'is', 'awesome', 'always'] 
def foo(x):
     print x * 3

 
def my_map_simple(fun, list):
     for item in list:
         fun(item)

 
my_map_simple(foo, list)

 
