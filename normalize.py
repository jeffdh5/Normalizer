import sys

def normalize(string, normalized=''):
    def read_tail(string, normalized):
        if string[0] == '/':
            return normalize(string[1:], normalized + string[0])
        elif string[0] == '.':
            while string[0] == '.':
                string = string[1:]
            return normalize(string[1:], normalized)
        else:
            return normalize(string, normalized)
            
    if string == '':
        return normalized
    else:
        if string[0] == '/':
            return read_tail(string[1:], normalized + string[0])
        else:
            return normalize(string[1:], normalized + string[0])

if len(sys.argv)<2:
    print("You did not enter an directory to parse. \nIn order to use this normalizer, please enter at least one directory.\nWith multiple directories, separate the directories with a space.")
for arg in sys.argv[1:]:
    print(normalize(arg))
