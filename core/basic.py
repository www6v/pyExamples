def all_unique(lst):
        return len(lst) == len(set(lst))

def listAndTuple():
    ##
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))
    print(all_unique(y))

    ## list vs. tup
    l = [3, 2, 3, 7, 8, 1]
    print(l[1:2])
    l.count(3)
    l.index(7)
    l.reverse()
    l.sort()

    tup = (3, 2, 3, 7, 8, 1)
    tup.count(3)
    tup.index(7)
    list(reversed(tup))
    sorted(tup)


def dictAndSet():
    d = {'name': 'jason', 'age': 20}

    d['gender'] = 'male'
    d['dob'] = '1999-02-01'
    d['dob'] = '1998-01-01'
    d.pop('dob')
    print(d)

    s = {1, 2, 3}
    s.add(4)
    s.remove(4)
    print(s)
