#! Writing term into dictionary, where key - x^n... ; value - a

# Parsing polynom on terms
def get_term(poly):
    term = list()
    dictionary = dict()
    flag = 1 # for "=" detection and reverse sign if we`re on right side of polynom
    start = 0
    end = len(poly)
    sign = "+"
    if poly[0] == "-":
        sign = "-"
        start = 1
    for i in range(start, end):
        if poly[i-1] == "=" and poly[i] == "-":
            sign = "-"
        elif poly[i] == "-" or poly[i] == "+":
            key, value = read_term(term, sign, flag)
            if key in dictionary:
                dictionary[key] += value
            else:
                dictionary[key] = value
            term.clear()
            sign = poly[i]
        elif poly[i] == "=":
            key, value = read_term(term, sign, flag)
            if key in dictionary:
                dictionary[key] += value
            else:
                dictionary[key] = value
            term.clear()
            flag = -1
            sign = "+"
        else:
            term += poly[i]
    key, value = read_term(term, sign, flag)
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value
    term.clear()

    return dictionary

# Adding terms into dictionary
def read_term(term, sign, flag): 
    dictionary = dict()
    temp_value = ""
    temp_key = ""
    multiplier_flag = True # to detect end of multiplier for not confuse with degree

    for char in term:
        if multiplier_flag and ((char > "0" and char <= "9") or char == "."):
            temp_value = temp_value + char
        else:
            multiplier_flag = False
            temp_key = temp_key + char
    try:
        if temp_value == "":
            value = 1
        else:
            try:
                value = int(temp_value)
            except:
                value = float(temp_value)
        if temp_key == "":
            key = "free_digit"
        else:
            key = str(temp_key)
    except Exception as exp:
        print("Somethink wrong", exp)

    #adding right sign to value
    if flag == 1:
        if sign == "-":
            value = value*(-1)
    elif flag == -1:
        if sign == "+":
            value = value*(-1)

    return key, value