def is_bool(var):
    if str(var).lower() == 'false' or str(var).lower() == 'true':
        return True
    return isinstance(var, bool)