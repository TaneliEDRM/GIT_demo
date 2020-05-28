def split_string(string, separator):
    l = string.split(separator)
    l = [float(i) for i in l]
    return l


s = split_string("1,3", ",")
print(s)
