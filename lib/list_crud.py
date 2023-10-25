def create_an_empty_list():
    return []

def create_a_list():
    f = [1,2,3,4]
    return f

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    l.pop(-1)
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[len(l)-1]
