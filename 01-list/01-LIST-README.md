# List Manager Exercise

Create a program that allows users to manage a list by adding, removing, or
modifying integer values. The program will repeatedly ask the user for an action
until they choose to exit.

## Inputs

The program should handle the following inputs from the user:

  - `(a)dd`: Adds an integer to the list.
  - `(r)emove`: Removes an integer from the list if it exists.
  - `(m)odify`: Modifies an existing integer in the list by replacing it with a
    new value.
  - `(e)xit`: Exits the program.

Each time an action is requested, the user should be prompted for an integer
`Value`, which will be processed according to the selected action.

## Expected Output

When you run your program, it should display the list status after each action.
Below is an example session:

```plaintext
The list is now []
(a)dd, (r)emove, (m)odify or (e)xit: a
Value: 5
The list is now [5]
(a)dd, (r)emove, (m)odify or (e)xit: a
Value: 10
The list is now [5, 10]
(a)dd, (r)emove, (m)odify or (e)xit: r
Value: 5
The list is now [10]
(a)dd, (r)emove, (m)odify or (e)xit: m
Value: 10
New Value: 20
The list is now [20]
(a)dd, (r)emove, (m)odify or (e)xit: e
Bye!
```

## Tasks

The main program loop that presents the menu, asks for a value, and calls an
appropriate function is already done for you. You are to implement the
functions:

- add_item()
- remove_item()
- modify_item()

All of the functions modify the list passed in as the parameter `my_list`, and
none of them return any values. More explicit instructions for each are provided
in the docstring. Remember that your code is written BELOW the closing """ of
the docstring.


## Hints
- Remember to validate user input when expecting an integer with `input()`.
- The `in` keyword can be helpful to check if an item exists in the list.
- To avoid runtime errors when converting user input to an integer, use
  try-except.
