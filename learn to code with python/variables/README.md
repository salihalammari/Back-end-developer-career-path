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