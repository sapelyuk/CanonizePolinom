#! Reduction of a polynomial to a canonical form
import ReadPolynom
import CanonizeTerm
import Sorting
import PrintDict

def main():
    print("________________Main function________________\n")

    #Reading polynom from any source
    polynom = ReadPolynom.get_polynom()
    
    #Parsing polynom into dictionary
    dictionary = CanonizeTerm.get_term(polynom)

    #Sorting list of keys fo canonical form
    keys = Sorting.get_sorted_keys(dictionary)

    #Printing Cononical Polynom on screen
    PrintDict.print_polynom(dictionary, keys)    
    
  
if __name__ =="__main__":
    main()
