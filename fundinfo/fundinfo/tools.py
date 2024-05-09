
def strNone(str):
    if str is not None:
        return str.strip().replace(u'\xa0\n', u'')

