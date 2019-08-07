'''
The idea with DNA logic is explained further in
"Artificial Life" by Steven Levy, on page 63. 

"...instead of computer bits, there's a four-state
code [the four base chemicals that make up DNA and 
whose sequencing forms the genetic code] [sic]" (63)
'''

def validInputs(DNA):
    new_DNA = ""
    for i in range(0, len(DNA), 2):
        first = convertDNA(DNA[i])
        second = convertDNA(DNA[i+1])
        if (DNA[i] + DNA[i+1]) % 2 != 0:
            print(first + " and " + second + " do not belong together.")
            return "ERROR IN CODE"
        else:
            new_DNA += first
            new_DNA += second
    return new_DNA

def convertDNA(num_input):
    # Adenine
    if num_input == 0:
        return "A"
    # Thymine
    elif num_input == 2:
        return "T"
    # Guanine
    elif num_input == 1:
        return "G"
    # Cytosine
    elif num_input == 3:
        return "C"




if __name__ == "__main__":
    DNA_sequence = [1, 3, 3, 1, 0, 2, 2, 0, 1, 3]
    converted_string = validInputs(DNA_sequence)
    print(converted_string)