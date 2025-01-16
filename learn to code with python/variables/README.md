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

