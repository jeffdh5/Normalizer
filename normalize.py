def normalize(string, normalized=''):
    def read_tail(string, normalized):
        if string[0] == '/':
            return normalize(string[1:], normalized+=string[0])
        while string[0] == '.':
            string=string[1:]
            #now it should be at another '/'. You want to remove this
            #so as to not have duplicate '/'s.
            return normalize(string[1:], normalized)
        
    if string == '':
        return normalized
    else:
        if string[0] in 'abcdefghijklmnopqrstuvwxyz1234567890':
            return normalize(string[1:], normalized+=string[0])
        elif string[0] == "/":
            return read_tail(string[1:], normalized+=string[0])