#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names_defined_module = dir(hidden_4)
    print(names_defined_module)
    # filtered_names = (name for name in names_defined_module 
    #                   if not name.startswith('__'))
    # for name in filtered_names:
    #     print(name)
