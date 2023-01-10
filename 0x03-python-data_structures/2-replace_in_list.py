def element_at(my_list, idx, new_element):
    if idx < 0:
       return ("none")
    elif idx > len(my_list) - 1:
        return ("none")
    else:
	my_list[idx] = new_element
	return my_list
