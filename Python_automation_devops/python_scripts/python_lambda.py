"""
Syntax of a Lambda Function

    lambda arguments: expression
    lambda: Keyword to define a lambda function.

    arguments: Input parameters (similar to function arguments).

    expression: A single expression that is evaluated and returned.

    Key Characteristics of Lambda Functions
        Anonymous: Lambda functions don't have a name (unless assigned to a variable).

        Single Expression: They can only contain one expression, which is evaluated and returned.

        Short-lived: Typically used for short, one-time operations.

        First-class Objects: Like regular functions, lambda functions can be passed as arguments, returned from functions, or assigned to variables.

    When to Use Lambda Functions
        For simple, one-line operations.

    When passing a function as an argument to higher-order functions like map(), filter(), or sorted().

    When the function is used only once and doesn't need a name.

    Limitations of Lambda Functions
        Single Expression: Lambda functions can only contain one expression. Complex logic requires a regular function.

        Readability: Overusing lambda functions can make code harder to read and understand.

        No Statements: Lambda functions cannot include statements like if, for, or while. Use a regular function for such cases.

"""
# A lambda function to add two numbers
def test_lambda():
    add = lambda x, y: x + y
    print(add(5, 3))  # Output: 8

'''
2. Using Lambda with map()
The map() function applies a lambda function to each item in an iterable (e.g., list).
'''
def test_lambda_with_map():
    a=[1,2,3,4,5]
    b=map(lambda x:x+1,a) # it prints data in object
    print(list(b))

'''
3. Using Lambda with filter()
The filter() function filters elements based on a condition defined by a lambda function.
'''
def test_lambda_with_filter():
    a=[1,2,3,4,5]
    b=filter(lambda x:x>3,a) # stores in object
    print(list(b))

'''
4. Using Lambda with sorted()
The sorted() function can use a lambda function as the key to customize sorting.
'''
def test_lambda_with_sorted():
    students = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 30},
    ]

    # Sort by age
    sorted_students = sorted(students, key=lambda x: x["age"])
    print(sorted_students)
    # Output: [{'name': 'Bob', 'age': 22}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

'''
5. Lambda in a List of Functions
You can store multiple lambda functions in a list and call them dynamically.
'''

def test_as_list_of_functions():
    operations = [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
    ]

    print(operations[0](5, 3))  # Output: 8 (addition)
    print(operations[1](5, 3))  # Output: 2 (subtraction)
    print(operations[2](5, 3))  # Output: 15 (multiplication)

def test_lambda_with_reduce():
    import functools
    a=[1,2,3,4,5]
    b=functools.reduce(lambda a,b:a+b,a)
    print(b)


