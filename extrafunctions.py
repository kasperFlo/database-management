Gspaceing = 10

def upperr(x):
    y = x.upper()
    return y
def LJspace(string):
    spaceAdd = Gspaceing - len(string)
    if (spaceAdd > 0):
        lJust = string+(" "*spaceAdd)
        return lJust 
    return string
def centerSpace(string):
    CJust = str(string).center(Gspaceing+6)
    return CJust