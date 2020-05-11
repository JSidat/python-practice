#Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
#without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    unique_list = []
    prev_char = None
    for char in iterable[0:]:
        if char != prev_char:
            unique_list.append(char)
            prev_char = char
    return unique_list