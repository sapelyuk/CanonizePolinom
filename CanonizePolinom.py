#! Reduction of a polynomial to a canonical form
import ReadPolynom
import CanonizeTerm

def main():
    print("________________Main function________________")
    #Reading polynom from any source
    polynom = ReadPolynom.get_polynom()
    
    #Parsing polynom into dictionary
    dictionary = CanonizeTerm.get_term(polynom)

    print("DICTIONARY IN MAIN")
    for key in dictionary:
        if key == "free_digit":
            print(dictionary[key], end="")
        else:
            print(dictionary[key], end="")
            print(key, end="")

    print("=0\nEND...")


if __name__ =="__main__":
    main()
