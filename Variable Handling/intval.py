def intval(var, base=''):
    if var:
        base = 10 if not base else base
        if type(var) == list or type(var) == dict:
            return 0 if len(var) == 0 or len(var) == 0 else 1
        if type(var) == int:
            return var
        if type(var) == float:
            return int(var)
        return int(var, base)
    return None