def modulateInputs(string):
     
    try:
        string = str(string)

# if the input can't be converted in a string (the input is an object without __str__ method) return an error 
    except:
        return "Error: Input must be in 4 bit binary"

# if the execpt is not triggered we remove special character to accept different input
    string = string.replace(" ", "")
    string = string.replace("-", "")

# verify that the input in a 4 bit binary
    if len(string) % 4 != 0:
        return "Error: Input must be in 4 bit binary"

        # return an error if there is anaything else than 0 and 1
    for c in string:
        if (c != "0") and (c != "1"):
            return "Error: Input must be in 4 bit binary"

# the input is suitable to be converted so I convert the string
    return convert4B5B(string)

def convert4B5B(string):
    # make a dictionary with all the possible 4 bit binary and there transposition in 5 bit
    encodingTable = {
	"0000":	"11110",
	"0001":	"01001",
	"0010":	"10100",
	"0011":	"10101",
	"0100":	"01010",
	"0101":	"01011",
	"0110":	"01110",
	"0111":	"01111",
    "1000":	"10010",
	"1001":	"10011",
	"1010":	"10110",
	"1011":	"10111",
	"1100":	"11010",
	"1101":	"11011",
	"1110":	"11100",
	"1111":	"11101"
    }

#  make an empty string that will be populated by the 5 bit conversion
    newString = ""

    # iterate to every 4 postion of the string 
    for i in range(0,len(string)-3,4):
        # add the 5bit translation to the new string
        newString += encodingTable[string[i:i+4]]
    return newString



