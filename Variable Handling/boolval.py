def boolval(var):
    yes =  ['true', 'True', 'TRUE', 'yes', 'Yes', 'y', 'Y', '1', 'on', 'On', 'ON', 1]
    if var in yes:
        return True
    else:
        return False