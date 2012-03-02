# Two elements are considered equal
# if and only if (string) $elem1 === (string) $elem2.

def array_unique(array, stringComparison=True):
    def preserve(n, stringComparison):
        if stringComparison:
            return str(n)
        else:
            return n
    if type(array) == dict:
        check = []
        final = {}
        for key,val in array.iteritems():
            rem = preserve(val, stringComparison)
            if rem in check:
               continue
            final[key] = val
            check.append(val)
        return final
    else:
        check = {}
        final = []
        for element in array:
            rem = preserve(element, stringComparison)
            if rem in check:
                continue
            check[rem] = 1
            final.append(element)
        return final

