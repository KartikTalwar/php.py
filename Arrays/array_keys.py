def array_keys(array, search_value=''):
    if type(array) == dict:
        return array.keys()
    else:
        if type(array) == list:
            if search_value:
                keys  = []
                track = 0
                for x in array:
                    if str(x) == str(search_value):
                        keys.append(track)
                    track += 1
                return keys
        else:
            return None