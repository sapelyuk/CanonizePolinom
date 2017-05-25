#! Printing Polynom in canonical form

def print_polynom(dictionary, keys):
    is_first = True

    print("=====Canonized polynom=====\n")

    for key in keys:
        if is_first:
            if key == "free_digit":
                print(dictionary[key], end="")
            elif dictionary[key] == 0:
                continue
            else:
                print(dictionary[key], end="")
                print(key, end="")
            is_first = False
        else:
            if key == "free_digit":
                if dictionary[key] > 0:
                    print("+",end="")
                    print(dictionary[key], end="")
                else:
                    print(dictionary[key], end="")
            elif dictionary[key] == 0:
                continue
            else:
                if dictionary[key] > 0 and dictionary[key] != 1:
                    print("+",end="")
                    print(dictionary[key], end="")
                    print(key, end="")
                elif dictionary[key] > 0 and dictionary[key] == 1:
                    print("+",end="")
                    print(key, end="")
                elif dictionary[key] < 0 and dictionary[key] == -1:
                    print("-",end="")
                    print(key, end="")
                else:
                    print(dictionary[key], end="")
                    print(key, end="")                    

    print("=0\n")