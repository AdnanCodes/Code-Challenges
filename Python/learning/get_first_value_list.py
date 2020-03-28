def get_first_value(number_list):
    # Several ways to acquire first value in the list
    # you can return first value by simply indexing at '0'
    # return number_list[0]
    return number_list[0]
    # Alternative crazy way of thinking
    # Iterate through the list and immediately return first element
    # For loop will go through the entire list but we can stop with either
    # return or break

    for item in number_list:
        return item
