def strip_tags(html):
    import re
    return re.sub(r'<[^>]*?>', '', html)