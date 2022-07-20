def get_middle_char(x):

    if int(len(x)) % 2:
        
        y = int(len(x)) // 2
        list(x)
        return x[y]
        
    else:
        
        y = int(len(x)) / 2
        list(x)
        return x[y]


get_middle_char('ssafy') # => a

get_middle_char('coding') # => di