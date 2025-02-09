# Variables

[Variables](https://users.cs.utah.edu/~germain/PPS/Topics/variables.html ) are how we store data as our program runs. Up 'till now we've been printing data by passing it straight into `print()`. Now we're going to save the data in variables so we can reuse it and change it before printing it.

## Creating Variables
A "variable" is just a name that we give to a value. For example, we can make a new variable named `my_height` and set its value to `100`:
```my_height = 100```

Or we can define a variable called `my_name` and set it to the text string `"Lane"`:

```my_name = "Lane"```
We have the freedom to choose any name for our variables, but they should be descriptive and consist of a single ["token"](https://en.wikipedia.org/wiki/Lexical_analysis#Token ), meaning continuous text with underscores separating the words.

## Using Variables
Once we have a variable, we can access its value by using its name. For example, this will print `100`:
```print(my_height)```
And this will print `Lane`:
```print(my_name)```

## Variables Vary
Variables are called "variables" because they can hold any value and that value can change (it varies).
For example, this code prints `20`:

```bash
acceleration = 10
acceleration = 20
print(acceleration)
```

The line `acceleration = 20` reassigns the value of `acceleration` to 20. It overwrites whatever was being held in the `acceleration` variable before (10 in this case).

# Storing Results

Now that we know how to store and change the value of variables let's do some math!

Here are some examples of common mathematical operators in Python syntax.

```bash
summation = a + b  # Addition
difference = a - b # Subtraction
product = a * b    # Multiplication
quotient = a / b   # Division
```
Parentheses can be used to order [math operations](https://www.mathsisfun.com/operation-order-pemdas.html ).

```avg = (a + b + c) / 3```
# Negative Numbers
Negative numbers in Python work the way you probably expect. Just add a minus sign:

```my_negative_num = -1```

# Comments
Comments don't do... anything. They are ignored by the Python interpreter. That said, they're good for what the name implies: adding comments to your code in plain English (or whatever language you speak).

# Single Line Comment

## Multi-Line Comments [(Aka docstrings)](https://peps.python.org/pep-0257/ )

# Variable Names
Variable names can not have spaces, they're continuous strings of characters.
The creator of the Python language himself, [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum ),[implores us](https://peps.python.org/pep-0008/#function-and-variable-names ) to use `snake_case ` for variable names. What is snake case? It's just a style for writing variable names. Here are some examples of different casing styles:
| Name	      |                    Description	                              |     Code      |	Language(s) that recommend it  |
|-------------|---------------------------------------------------------------|---------------|--------------------------------|
| Snake Case  | All words are lowercase and separated by underscores          | my_hero_health|	   Python, Ruby, Rust          |
| Camel Case  |	Capitalize the first letter of each word except the first one |	myHeroHealth  |    JavaScript, Java            |
| Pascal Case | Capitalize the first letter of each word	                  | MyHeroHealth  |    C#, C++                     |
| No Casing   |	All lowercase with no separation	                          | myherohealth  |    No one: don't do this       |

To be clear, your Python code will still work with Camel Case or Pascal Case, but can we please just have nice things? We just want some consistency in our craft.

# Basic Variable Types
Python has several basic [data types](https://en.wikipedia.org/wiki/Data_type ).

## Strings
In programming, snippets of text are called ["strings"](https://docs.python.org/3/library/stdtypes.html#textseq ). They're lists of characters strung together. We create strings by wrapping the text in single quotes or double quotes. That said, double quotes are preferred.
```bash
name_with_single_quotes = 'boot.dev' # not so good
name_with_double_quotes = "boot.dev" # so good
```
## Numbers
Numbers are not surrounded by quotes when they're declared.
An [integer](https://docs.python.org/3/c-api/long.html ) is a number without a decimal part:
```bash
x = 5 # positive integer
y = -5 # negative integer
```
A [float](https://docs.python.org/3/library/functions.html#float ) is a number with a decimal part:
```bash
x = 5.2
y = -5.2
```
## Booleans
A ["Boolean"](https://docs.python.org/3/c-api/bool.html#boolean-objects ) (or "bool") is a type that can only have one of two values: True or False. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just True/False boolean values.

```bash
is_tall = True
is_short = False
```
# F-Strings in Python
Ever played Pokemon and chosen a funny name so that the in-game messages would come out funny?
In Python we can create strings that contain dynamic values with the [f-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals ) syntax.

```bash
num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas
```
. Opening quotes must be preceded by an `f`.
. Variables within curly brackets have their values "interpolated" (injected) into the string.
. It's just a string with a special syntax.

# NoneType Variables
Not all variables have a value. We can make an "empty" variable by setting it to `[None](https://docs.python.org/3/library/constants.html#None )`. `None` is a special value in Python that represents the absence of a value. It is not the same as zero, False, or an empty string.

```my_mental_acuity = None```

The value of `my_mental_acuity` in this case is `None` until we use the assignment operator, `=`, to give it a value.

# None Is NOT a String
[NoneType](https://docs.python.org/3/library/types.html#types.NoneType ) is not the same as a string with a value of "None":

```bash
my_none = None # this is a None-type
my_none = "None" # this is a string with the value "None"
```
# NoneType Quiz
As we mentioned in the last exercise, the `None` keyword is used to define an "empty" variable.

So when would you use it? One usecase is to represent that a value hasn't been determined yet, for example, an uncaptured input. For example, maybe your program is waiting for a user to enter their name. You might start with a variable:

```username = None```

Then later in the code, once the user has entered their name, you can assign it to the `username` variable:

```username = input("What's your name? ")```

Remember, it's crucial to recognize that `None` is not the same as the string `"None"`. They look the same when printed to the console, but they are different data types. If you use `"None"` instead of `None`, you will end up with code that looks correct when it's printed but fails the tests.

# Dynamic Typing

Python is [dynamically typed](https://en.wikipedia.org/wiki/Type_system#Static_and_dynamic_type_checking_in_practice ), which means a variable can store any type, and that type can change.
For example, if I make a number variable, I can later change that variable to a string:

```bash 
speed = 5
speed = "five"
```
# But Like, Maybe Don’t 
In almost all circumstances, it’s a bad idea to change the type of a variable. The “proper” thing to do is to just create a new one. For example:
```bash
speed = 5
speed_description = "five"
```
# What Is Non-Dynamic Typing?

Languages that aren’t dynamically typed are [statically typed](mozilla), such as Go (which you’ll learn in a later course ). In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.

If Python were statically typed, the first example from before would crash on the second line, `speed = "five"`. The computer would give an error along the lines of `you can't assign a string value ("five") to a number variable (speed).`


