def ucwords(string):
    single   = string.split(' ')
    response = ''
    
    for i in range(len(single)):
        response += single[i][0].upper() + single[i][1:] + ' '

    return response
