def ucwords(string):
    single   = string.split(' ')
    response = ''
    last = len(single)
    
    for i in range(len(single)):
        padding   = '' if i == last-1 else ' '
        response += single[i][0].upper() + single[i][1:] + padding

    return response
