def str_split(string, length):
    return [ string[i:i+length] for i in range(0, len(string), length) ]