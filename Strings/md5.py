def md5(string):
    from hashlib import md5
    return md5(str(string)).hexdigest()