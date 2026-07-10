# Decorators

## Overview

![Decorators Overview](../images/dec.png)

Decorators are a powerful feature in Python that allow you to **add new functionality to an existing function without modifying its original code**.

A decorator is simply a function that takes another function as input, adds some additional behavior, and returns the modified function.

Think of a decorator as a **wrapper** around a function. The original function remains unchanged, but extra functionality is executed before, after, or around it.

---

## Understanding the Image

The image above shows a **red apple** being transformed into a **green apple**.

Similarly, a decorator transforms the behavior of a function without changing the function itself.

- 🍎 **Red Apple** → Original Function
- ➜ **Decorator** → Wraps the original function and adds extra functionality
- 🍏 **Green Apple** → Enhanced Function with additional behavior

The original function still exists, but after applying a decorator, it gains new capabilities.

For example:

- Before executing a function, a decorator can display a message.
- After executing a function, it can log the result.
- It can measure execution time.
- It can validate user input.
- It can check whether a user is authenticated.

In all these cases, **the original function remains unchanged**, while the decorator adds the required functionality.

---

## Why Use Decorators?

Decorators are widely used because they help developers avoid writing the same code repeatedly and keep programs clean and organized.

* Code Reusability
A single decorator can be applied to multiple functions, eliminating duplicate code.

* Cleaner Code
The main function contains only its core logic, while additional tasks are handled separately by decorators.

* Logging and Monitoring
Decorators can automatically record function calls, execution details, and application events.

* Authentication and Authorization
Decorators can verify whether a user has permission before allowing access to a function.

* Performance Measurement
Decorators can calculate and display how long a function takes to execute.

* Input Validation
Decorators can validate function arguments before the function is executed.

By separating these common tasks from the main business logic, decorators make Python programs more modular, reusable, and easier to maintain.

---

## Functions as First-Class Objects

In Python, functions are first-class objects. This means they can:

* Be assigned to variables
* Be passed as arguments
* Be returned from other functions
* Be stored in data structures

## Higher-Order Functions

A Higher-Order Function is a function that:

* Accepts another function as an argument
* Returns a function as a result

Decorators are built using higher-order functions.

---


## How Decorators Work

![Decorators Diagram](../images/decorators.png)

A decorator works by **wrapping an existing function** and adding extra functionality without modifying the original function's code.

Instead of changing the original function directly, Python passes the function to a decorator. The decorator creates a **wrapper function**, adds additional behavior, and then returns the wrapper as the new function.

The original function remains unchanged, but whenever it is called, the wrapper function executes first.

### Workflow

```text
Original Function
        ↓
 Passed to Decorator
        ↓
Decorator Creates Wrapper
        ↓
Adds Extra Functionality
(Before / After Execution)
        ↓
Returns Wrapped Function
        ↓
Decorated Function Executes
```

---

## Step-by-Step Explanation

### Step 1: Original Function

First, we create a normal Python function.

```python
def greet():
    print("Hello")
```

At this stage, calling `greet()` simply prints:

```text
Hello
```

---

### Step 2: Function is Passed to the Decorator

When we apply a decorator using the `@decorator` syntax, Python automatically passes the original function to the decorator.

```text
greet()
      ↓
 decorator(greet)
```

Here, `greet()` becomes the input to the `decorator()` function.

---

### Step 3: Decorator Creates a Wrapper

Inside the decorator, a new function called `wrapper()` is created.

The wrapper contains the additional functionality that should run before or after the original function.

```text
Decorator
      ↓
Creates wrapper()
```

---

### Note: Are `decorator` and `wrapper` Special Names?

No. The names `decorator` and `wrapper` are **not Python keywords**. They are simply function names chosen by the programmer.

You can replace them with any meaningful names.

For example:

```python
def logger(func):
    def execute():
        ...
    return execute
```

---


### Step 4: Wrapper Calls the Original Function

The wrapper first performs the additional task, then calls the original function.

```text
wrapper()
      ↓
Before Message
      ↓
Original Function
      ↓
After Message
```

---

### Step 5: Decorated Function Executes

Finally, the decorator returns the wrapper function.

Now, whenever we call:

```python
greet()
```

Python actually executes:

```text
wrapper()
      ↓
Before
      ↓
Hello
      ↓
After
```

The original `greet()` function is never modified, but its behavior is enhanced through the decorator.

---
## Examples

| Concept                  | File                      |
| ------------------------ | ------------------------- |
| Basic Decorator          | 01_basic_decorator.py     |
| Decorator with Arguments | 02_decorator_with_args.py |
| functools.wraps Example  | 03_wraps_example.py       |
| Timer Decorator          | 04_timer_decorator.py     |
| Logging Decorator        | 05_logging_decorator.py   |

---

# 1. Basic Decorator

## Explanation

A Basic Decorator is used to add extra functionality to a function without modifying its original code.

Instead of changing the original function, a decorator wraps it and executes additional code before or after the function runs.

Decorators help keep code clean, reusable, and easier to maintain.

---

## Syntax

The general syntax of a basic decorator is:

```python
def decorator(func):

    def wrapper():
        # Code to execute before the original function

        func()

        # Code to execute after the original function

    return wrapper


@decorator
def function_name():
    # Original function
```

### Syntax Explanation

- `decorator(func)` receives the original function as an argument.
- `wrapper()` contains the additional functionality.
- `func()` calls the original function.
- `return wrapper` returns the wrapped function.
- `@decorator` applies the decorator to the function.

---

## Code Flow

The following flow shows how a decorator works internally.

```text
Define Decorator
        ↓
Define Original Function
        ↓
Apply @decorator
        ↓
Decorator Receives Function
        ↓
Creates wrapper()
        ↓
Returns wrapper()
        ↓
Call Function
        ↓
wrapper() Executes
        ↓
Before Code
        ↓
Original Function
        ↓
After Code
```

---

## How Python Executes

When Python sees the following code:

```python
@decorator
def greet():
    print("Hello, World!")
```

Python automatically converts it into:

```python
def greet():
    print("Hello, World!")

greet = decorator(greet)
```

Now, when the following statement is executed:

```python
greet()
```

Python actually executes:

```text
wrapper()
      ↓
Before calling the function
      ↓
Original greet() function
      ↓
Hello, World!
      ↓
After calling the function
```

The original function is not modified. Instead, it is replaced with the wrapped version returned by the decorator.

---

## Example

**Example:** A decorator can display a message before and after executing a function without changing the function's original implementation.

---

## Code

```python
def decorator(func):

    def wrapper():
        print("Before calling the function")

        func()

        print("After calling the function")

    return wrapper


@decorator
def greet():
    print("Hello, World!")


greet()
```

---

## Code Explanation

### Step 1

```python
def decorator(func):
```

Defines a decorator function that accepts another function as its argument.

Here, `func` refers to the original function (`greet`).

---

### Step 2

```python
def wrapper():
```

Creates an inner function called `wrapper()`.

This function is responsible for adding extra functionality.

---

### Step 3

```python
print("Before calling the function")
```

Executes before the original function.

---

### Step 4

```python
func()
```

Calls the original `greet()` function.

---

### Step 5

```python
print("After calling the function")
```

Executes after the original function finishes.

---

### Step 6

```python
return wrapper
```

Returns the wrapper function.

This replaces the original function with the wrapped version.

---

### Step 7

```python
@decorator
```

Applies the decorator to the `greet()` function.

Internally, Python performs:

```python
greet = decorator(greet)
```

---

### Step 8

```python
greet()
```

Calling `greet()` actually executes the `wrapper()` function, which then calls the original function.

---

## Output

```text
Before calling the function
Hello, World!
After calling the function
```

![Basic Decorator Output](../images/basic_decorator_output.png)

---

## Key Takeaway

A Basic Decorator wraps an existing function and adds extra functionality before or after the original function executes without modifying its original implementation. Decorators improve code reusability, readability, and maintainability by separating common tasks from the main business logic.

---

# 2. Decorator with Arguments

## Explanation

Sometimes, the function being decorated accepts one or more arguments. In such cases, the decorator must also be able to receive and pass those arguments to the original function.

Python provides `*args` and `**kwargs` to make decorators flexible enough to work with functions that accept any number of positional and keyword arguments.

Without `*args` and `**kwargs`, the decorator would only work with functions that have no parameters.

---

## Why Use Decorators with Arguments?

A basic decorator works well for functions that do not require parameters.

However, many real-world functions accept arguments.

For example:

```python
add(5, 3)
login(username, password)
send_email(receiver, subject)
```

To decorate these functions without knowing how many arguments they receive, we use:

- `*args` → Accepts any number of positional arguments.
- `**kwargs` → Accepts any number of keyword arguments.

This makes the decorator reusable for different types of functions.

---

## Syntax

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        # Code before function execution

        result = func(*args, **kwargs)

        # Code after function execution

        return result

    return wrapper


@decorator
def function_name(arguments):
    ...
```

### Syntax Explanation

- `decorator(func)` receives the original function.
- `wrapper(*args, **kwargs)` accepts all arguments passed to the function.
- `func(*args, **kwargs)` forwards those arguments to the original function.
- `return result` returns the value produced by the original function.
- `@decorator` applies the decorator to the function.

---

## Code Flow

The following flow shows how a decorator works with function arguments.

```text
Define Decorator
        ↓
Define Function with Arguments
        ↓
Apply @decorator
        ↓
Decorator Receives Function
        ↓
Creates wrapper(*args, **kwargs)
        ↓
Call Function with Arguments
        ↓
wrapper Receives Arguments
        ↓
Execute Code Before Function
        ↓
Original Function Executes
        ↓
Execute Code After Function
        ↓
Return Result
```

---

## How Python Executes

When Python sees:

```python
@decorator
def add(a, b):
    return a + b
```

Python automatically converts it into:

```python
def add(a, b):
    return a + b

add = decorator(add)
```

Now, when the following statement is executed:

```python
add(5, 3)
```

Python actually executes:

```text
wrapper(5, 3)
        ↓
Before execution
        ↓
func(5, 3)
        ↓
Returns 8
        ↓
After execution
        ↓
Returns 8
```

The original `add()` function is not modified. Instead, it is replaced with the wrapped version returned by the decorator.

---

## Example

**Example:** A decorator can display messages before and after executing a function that accepts arguments, such as an addition function.

---

## Code

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print("Result:", add(5, 3))
```

---

## Code Explanation

### Step 1

```python
def decorator(func):
```

Defines a decorator function that accepts another function as its argument.

Here, `func` refers to the original `add()` function.

---

### Step 2

```python
def wrapper(*args, **kwargs):
```

Creates a wrapper function that can accept any number of positional and keyword arguments.

- `*args` stores positional arguments.
- `**kwargs` stores keyword arguments.

---

### Step 3

```python
print("Before execution")
```

Executes before calling the original function.

---

### Step 4

```python
result = func(*args, **kwargs)
```

Calls the original function and forwards all received arguments.

In this example:

```python
add(5, 3)
```

becomes:

```python
func(5, 3)
```

The original function performs:

```text
5 + 3 = 8
```

The returned value is stored in `result`.

---

### Step 5

```python
print("After execution")
```

Executes after the original function finishes.

---

### Step 6

```python
return result
```

Returns the value produced by the original function.

Without this statement, the decorated function would return `None`.

---

### Step 7

```python
@decorator
```

Applies the decorator to the `add()` function.

Internally, Python performs:

```python
add = decorator(add)
```

---

### Step 8

```python
add(5, 3)
```

Calling `add(5, 3)` actually executes the `wrapper()` function.

The wrapper:

1. Prints the message before execution.
2. Calls the original `add()` function.
3. Receives the result (`8`).
4. Prints the message after execution.
5. Returns the result.

---

## Output

```text
Before execution
After execution
Result: 8
```

![Decorator with Arguments Output](../images/args_output.png)

---

## Key Takeaway

Decorators with `*args` and `**kwargs` are more flexible than basic decorators because they can work with functions that accept any number of positional and keyword arguments. This makes them suitable for real-world applications where functions often require different types of input parameters.

---

# 4. Timer Decorator

## Explanation

A Timer Decorator is used to measure how long a function takes to execute.

Instead of modifying the original function, the decorator records the start time before the function runs and the end time after it finishes. The difference between these two times gives the total execution time.

This technique is commonly used to analyze and improve application performance.

![Timer Decorator](../images/time.png)

---

## Why Use a Timer Decorator?

A Timer Decorator helps developers understand how efficiently a function executes.

It is commonly used for:

- Performance monitoring
- Application optimization
- Benchmarking code
- Measuring API response times
- Comparing different algorithms

---

## Syntax

```python
import time

def timer(func):

    def wrapper():

        start_time = time.time()

        func()

        end_time = time.time()

        print(end_time - start_time)

    return wrapper


@timer
def function_name():
    ...
```

### Syntax Explanation

- `time.time()` records the current system time.
- `start_time` stores the time before the function executes.
- `func()` calls the original function.
- `end_time` stores the time after execution.
- `end_time - start_time` calculates the execution time.
- `@timer` applies the timer decorator.

---

## Code Flow

```text
Define Timer Decorator
        ↓
Define Original Function
        ↓
Apply @timer
        ↓
Call Function
        ↓
Record Start Time
        ↓
Execute Original Function
        ↓
Record End Time
        ↓
Calculate Execution Time
        ↓
Display Execution Time
```

---

## How Python Executes

When Python sees:

```python
@timer
def process_data():
    ...
```

Python internally converts it into:

```python
def process_data():
    ...

process_data = timer(process_data)
```

Now, when:

```python
process_data()
```

is executed, Python actually runs:

```text
wrapper()
      ↓
Record Start Time
      ↓
Original Function Executes
      ↓
Record End Time
      ↓
Calculate Time Difference
      ↓
Display Execution Time
```

The original function is never modified. The timer decorator simply measures how long it takes to execute.

---

## Example

**Example:** Measure the execution time of a function that processes data.

---

## Code

```python
import time

def timer(func):

    def wrapper():

        start_time = time.time()

        func()

        end_time = time.time()

        print(
            "Execution Time:",
            round(end_time - start_time, 2),
            "seconds"
        )

    return wrapper


@timer
def process_data():

    time.sleep(2)

    print("Processing completed")


process_data()
```

---

## Code Explanation

### Step 1

```python
import time
```

Imports Python's built-in `time` module to measure execution time.

---

### Step 2

```python
def timer(func):
```

Defines the timer decorator.

The parameter `func` represents the original function.

---

### Step 3

```python
def wrapper():
```

Creates a wrapper function that contains the timing logic.

---

### Step 4

```python
start_time = time.time()
```

Records the current time before executing the original function.

---

### Step 5

```python
func()
```

Executes the original function.

In this example, it calls:

```python
process_data()
```

---

### Step 6

```python
end_time = time.time()
```

Records the current time immediately after the function finishes.

---

### Step 7

```python
round(end_time - start_time, 2)
```

Calculates the total execution time and rounds it to two decimal places.

---

### Step 8

```python
@timer
```

Applies the timer decorator to the `process_data()` function.

Internally, Python performs:

```python
process_data = timer(process_data)
```

---

### Step 9

```python
process_data()
```

Calling `process_data()` actually executes the wrapper function, which:

1. Records the start time.
2. Executes the original function.
3. Records the end time.
4. Calculates the execution time.
5. Displays the result.

---

## Output

```text
Processing completed
Execution Time: 2.0 seconds
```

![Timer Decorator Output](../images/time_output.png)

---

## Key Takeaway

A Timer Decorator measures how long a function takes to execute without modifying the original function. It is widely used to monitor performance, compare algorithms, identify slow functions, and optimize applications.

---
# 5. Logging Decorator

## Explanation

A Logging Decorator is used to record information whenever a function is executed.

Instead of modifying the original function, the decorator logs important details such as when the function starts and when it finishes. This helps developers monitor application behavior, debug issues, and keep track of function execution.

Logging decorators are widely used in production applications to improve monitoring and troubleshooting.

---

## Why Use a Logging Decorator?

A Logging Decorator automatically records function execution without changing the original function.

It is commonly used for:

- Application monitoring
- Debugging issues
- Tracking user actions
- API request logging
- System auditing

---

## Syntax

```python
def logger(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Completed")

    return wrapper


@logger
def function_name():
    ...
```

### Syntax Explanation

- `logger(func)` receives the original function.
- `wrapper()` contains the logging logic.
- The first `print()` logs when the function starts.
- `func()` executes the original function.
- The second `print()` logs when the function completes.
- `@logger` applies the logging decorator.

---

## Code Flow

```text
Define Logger Decorator
        ↓
Define Original Function
        ↓
Apply @logger
        ↓
Call Function
        ↓
Log Function Started
        ↓
Execute Original Function
        ↓
Log Function Completed
```

---

## How Python Executes

When Python sees:

```python
@logger
def process_order():
    ...
```

Python automatically converts it into:

```python
def process_order():
    ...

process_order = logger(process_order)
```

Now, when:

```python
process_order()
```

is executed, Python actually runs:

```text
wrapper()
      ↓
Log Function Started
      ↓
Original Function Executes
      ↓
Log Function Completed
```

The original function remains unchanged while the decorator records its execution.

---

## Example

**Example:** Log a message whenever a function starts and completes execution.

---

## Code

```python
def logger(func):

    def wrapper():

        print(f"[LOG] Function '{func.__name__}' started")

        func()

        print(f"[LOG] Function '{func.__name__}' completed")

    return wrapper


@logger
def process_order():

    print("Processing customer order...")


process_order()
```

---

## Code Explanation

### Step 1

```python
def logger(func):
```

Defines the logging decorator.

The parameter `func` refers to the original function.

---

### Step 2

```python
def wrapper():
```

Creates the wrapper function that adds logging before and after the original function executes.

---

### Step 3

```python
print(f"[LOG] Function '{func.__name__}' started")
```

Displays a log message before executing the original function.

`func.__name__` returns the name of the function being decorated.

For this example, it returns:

```text
process_order
```

---

### Step 4

```python
func()
```

Calls the original function.

Here it executes:

```python
process_order()
```

---

### Step 5

```python
print(f"[LOG] Function '{func.__name__}' completed")
```

Displays a log message after the original function finishes.

---

### Step 6

```python
return wrapper
```

Returns the wrapper function.

The original function is replaced with the wrapped version.

---

### Step 7

```python
@logger
```

Applies the logging decorator.

Internally, Python performs:

```python
process_order = logger(process_order)
```

---

### Step 8

```python
process_order()
```

Calling `process_order()` actually executes the wrapper function, which:

1. Logs that the function has started.
2. Executes the original function.
3. Logs that the function has completed.

---

## Output

```text
[LOG] Function 'process_order' started
Processing customer order...
[LOG] Function 'process_order' completed
```

![Logging Decorator Output](../images/login_output.png)

---

## Key Takeaway

A Logging Decorator records information before and after a function executes without modifying the original function. It is widely used for debugging, monitoring, auditing, and tracking application behavior in real-world software systems.

---

# Summary

Decorators are a powerful Python feature that allows developers to extend the behavior of functions without modifying their original implementation.

In this module, we learned that decorators work by wrapping an existing function inside another function and executing additional functionality before or after the original function.

The concepts covered in this module are:

- Basic Decorator
- Decorator with Arguments
- `functools.wraps` Example
- Timer Decorator
- Logging Decorator

Through these examples, we learned how decorators preserve function metadata, work with functions that accept arguments, measure execution time, and record function execution for debugging and monitoring.

Decorators promote cleaner, reusable, and maintainable code by separating common functionality from business logic. They are widely used in Python frameworks and real-world applications for logging, authentication, authorization, performance monitoring, input validation, caching, and many other cross-cutting concerns.
---