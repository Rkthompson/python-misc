"""
    example of a binary search in python.
    binary search will search for a value by eliminating
    the total area searched in half each iteration
"""


def binary_search(list, item):

    # high and low search values
    low = 0
    high = len(list) - 1

    while low <= high:
        # the half way point rounded down to an integer using floor division //
        mid = (low + high) // 2

        # the locaton checked for the search value
        # pulls from an array using the mid as the index value
        guess = list[mid]

        # check if the guess equals the searched for item
        if guess == item:
            return mid
        # Overwrite the high value if the guess was too high
        if guess > item:
            high = mid - 1
        # Overwrite the low value if the guess was too low
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

"""
    learning...
        1 write a function to create an array of 128 entrys
        2 search through the array
        3 pause during the search to display when the list has been cut in half
        4 answer how many times a 128 record list
             will be cut in half by a binary search
"""


def create_array(total_numbers):
    temp_list = [1]
    start = 1

    # add an item to the list until the total number requested is reached
    while(start < total_numbers):
        start = start + 1
        temp_list.append(start)

    return temp_list


def binary_search_with_callout(list, item):
    # items we need
    low = 0
    high = len(list) + 1
    # mid = (low + high) // 2

    # process
    while low <= high:
        # set the guess index
        mid = (low + high) // 2
        guess = list[mid]

        # check the guess
        # if it's a match
        if guess == item:
            # output - item found
            print("Item found")
            return mid
        # if it's too high
        if guess > item:
            print("Search too high")
            high = mid - 1
        # else it's too low
        else:
            print("Search too low")
            low = mid + 1
    # output - nothing found
    return None


my_new_lists = create_array(128)

print(binary_search_with_callout(my_new_lists, 1))
print(binary_search_with_callout(my_new_lists, 63))
print(binary_search_with_callout(my_new_lists, 64))
print(binary_search_with_callout(my_new_lists, 65))
print(binary_search_with_callout(my_new_lists, 128))

print(my_new_lists)
print(my_new_lists[0])
