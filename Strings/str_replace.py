def str_replace(search, replace, subject):
    if type(search) == list:
        if len(search) == len(replace):
            for i in range(len(search)):
                if search[i] != '':
                    subject = subject.replace(str(search[i]), str(replace[i]))
            return subject
        else:
            return "search and replace lengths are not the same"
    else:
        return subject.replace(search, replace)
