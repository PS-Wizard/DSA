def linearSearch(somearr,somevalue):
    for i,v in enumerate(somearr):
        print(i)
        if v == somevalue:
            return i
    return None
