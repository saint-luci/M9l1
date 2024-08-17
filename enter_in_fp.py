def apply_all_func(int_list, *functions):
    dict = {}
    for func in functions:
        dict[func.__name__] = func(int_list)
    return dict
    
    
print(apply_all_func([6, 20, 15, 9], max, min), end="")
print(apply_all_func([6, 20, 15, 9], len, sum, sorted), end="")