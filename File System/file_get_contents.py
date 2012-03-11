def file_get_contents(url):
    import urllib
    return urllib.urlopen(url).read()