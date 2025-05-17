
def add_item(my_list, num):
    """Adds a int item to the list.
    
    This one is very simple. You simply need to add num to the end of my_list.
    """
    # code starts here


def remove_item(my_list, num):
    """Removes a int item from the list if it exists.
    
    This one is also simple with a caveat. You are to remove the first instance
    of `num` from `my_list`. However, if `num` doesn't exist in `my_list`, then
    you should print (EXACTLY) "{num} is not in the list." (of course replacing
    {num} with the value of the `num` parameter).
    """
    # code starts here


def modify_item(my_list, num):
    """Modifies an existing item in the list by replacing it with a new value.
    
    This is a bit more challenging. There are multiple steps.

    1. Determine if `num` is in `my_list`. If not as above print "{num} is not
       in the list." and return.

    2. Find the location (index) of `num` in `my_list`.

    3. Ask the user for a new number (the text of the prompt is up to you) and
       convert it to an int. If the user enters a value that cannot be
       converted, then print (EXACTLY) "Not a number." and return.

    4. Set the value of the element at the location you found in step 2 to the
       value the user entered in step 3.
    """
    # code starts here


def main():
    """Main function to run the list manager"""
    my_list = []
    print("The list is now", my_list)

    while True:
        action = input("(a)dd, (r)emove, (m)odify or (e)xit: ").strip().lower()
        if action == "e":
            print("Bye!")
            break

        try:
            value = int(input("Value: "))
        except ValueError:
            print("Not a number.")
            return

        match action:
            case 'a':
                add_item(my_list, value)
            case 'r':
                remove_item(my_list, value)
            case 'm':
                modify_item(my_list, value)
            case _:
                print("Invalid option. Please choose 'a', 'r', 'm', or 'e'.")

        print("The list is now", my_list)

if __name__ == "__main__":
    main()
