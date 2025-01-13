# Welcome to "Learn Python"
# Chapter : Introduction To Python

# What is python?
Python is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python doesn't have to be your first language, but I think it's the best first language for most developers. It gets out of your way so you can focus on learning fundamental programming concepts.

Hundreds of thousands of students start their coding journey right here with [Python](https://www.python.org/ ).

But just because Python is simple doesn't mean it's not useful! Python is an [extremely popular](https://survey.stackoverflow.co/2024/technology ) language in the industry, and is well-known for:
 - Backend web servers
 - DevOps and cloud engineering
 - Machine learning
 - Scripting and automation
 - etc...

On the other hand, it's not particularly well-known for front-end development. While it's possible to do so, Python isn't typically used to build user interfaces.

## Installing Python
To get started with Python, you need to install it on your machine. You can download the latest version from the[official Python website](https://www.python.org/downloads/ ).

### Installation Steps
1. Go to the Python downloads page.
2. Select the version suitable for your operating system.
3. Follow the installation instructions.

## Use Python for…

### Web Development:
`Django`, `Pyramid`, `Bottle`, `Tornado`, `Flask`, `web2py`

### GUI Development:
`tkInter`, `PyGObject`, `PyQt`, `PySide`, `Kivy`, `wxPython`, `DearPyGui`

### Scientific and Numeric:
`SciPy`, `Pandas`, `IPython`

### Software Development:
`Buildbot`, `Trac`, `Roundup`

### System Administration:
`Ansible`, `Salt`, `OpenStack`, `xonsh`

### Building Fantasy Quest

We're going to build a text-based adventure game called "Fantasy Quest" in this course! I've written the first line of code for you, it prints a message below the editor welcoming new players to the game.

`Submit` the code to pass this assignment, then click the `-->` right arrow.

### Fix Your First Bug

The combat system in Fantasy Quest isn't working as intended! It appears that players are gaining health when attacked instead of losing it.

### Assignment
Fix the math bug on line 3.

## The Console

The "console" is a panel that displays important messages, like errors or the text output of a program. If we want to see what's happening in our code, we need to print it to the console by using the `print()` function.

We'll learn more about functions later, but for now, just know that the `print()` function will print anything you put inside its parentheses. For example:

```bash
print("this is some example text to print")
```

### Assignment
We need to tell our new players how to move! Print the following text to the console:

```
Use the arrow keys to move
```
## Your First Python Program
Once you have Python installed, you can create your first program. Open a text editor and create a file named `console.py`.

### Example Code
To run the console, execute the following command in your terminal:

```bash
python console.py
```
#### What is "Code"?
Code is just a series of instructions for a computer to follow one after another. Programs can have a lot of instructions.

Remember how we used the print() instruction to print text to the console? We can also use it to print numbers. This prints the number 42:

``` print(42) ```

Well, [addition](https://en.wikipedia.org/wiki/Addition ) is one of the most common instructions in programming. This also prints the number 42:

``` print(42 + 2) ```

It first calculates the sum inside the parentheses, and then prints the result.
### Assignment
Simple addition is used all the time in game development. In Fantasy Quest, we want weapons to deal bonus damage when they're enchanted.
Our hero's sword deals `250` damage normally, but should deal an additional `75` damage when it's enchanted.

Calculate and print the result of `250 + 75`

# Multiple Instructions
Code runs in order, starting at the top of the program. For example:

```bash 
print("this prints first")
print("this prints second")
print("this prints last") 
```
Each `print()` instruction prints on a new line.

### Assignment
The dialogue in our game should display in the correct order! In the first level, our hero encounters a talking owl named Jax.
  1. Run (not submit) the code and see that it's printed in the wrong order
  2. Rearrange the code so that it prints in the following (correct) order:

```bash
Jax: B-Kaw!
Hero: ...
Jax: Where are you off to this morning? Bkaw...
Hero: Where did an owl learn to speak??
```

# Syntax Errors

["Syntax"](https://en.wikipedia.org/wiki/Syntax_(programming_languages) ) is jargon for "valid code that the computer can understand". For example, the following code has invalid syntax:
```print("hello world')```

It has mismatched quotes around the string `hello world`. One is a single quote `'` and the other is a double quote `"`.

### Assignment
There's a bug in our game, and our players are distraught.
Find the syntax error in the code editor, and fix it.
# Syntax Errors Quiz
Syntax: The rules for how [expressions](https://en.wikipedia.org/wiki/Expression_(computer_science) ) and [statements](https://en.wikipedia.org/wiki/Statement_(computer_science) ) should be structured in a language. For example, in Python, the following is correct syntax:

```print("hello world")```
While in a different programming language, like Go, the correct syntax would be:
```fmt.Println("hello world")```
Syntax errors aren't the only kind of problems you can run into when coding, for example:
 . A bug in your logic. Your code is valid, and will run, but it does something unexpected.
 . It's too slow. Your code is valid and does what's expected, but it does it slowly

In this course, we're just concerned with syntax and logic errors. We'll cover performance issues in a later course.

# Game Statistics
Our team is asking for some stats on our Fantasy Quest game servers. They'd like to know the average number of players on the 4 servers.

### Assignment
Debug the code so that it correctly prints the solution to the math problem.

Remember, `print()` just prints the text in quotes. If you want to print the result of a mathematical expression, you can't put it in quotes.

### Key Points:
- Code can be compiled or interpreted.
- It is often organized into functions, classes, and modules.
- Comments can be included to explain the code to other developers.

##### what is Syntax Errors?
Syntax errors in programming are mistakes in the code that violate the rules of the programming language's syntax. These errors prevent the code from being parsed and executed correctly.

### Key Characteristics:
- **Detection at Compile Time**: Detected during the compilation or interpretation process.
- **Common Causes**:
  - Missing punctuation (e.g., colons, commas).
  - Mismatched parentheses or brackets.
  - Incorrect indentation (especially in Python).
  - Unclosed strings.

