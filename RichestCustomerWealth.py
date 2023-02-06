def maximize_wealth(accounts):
    r=0
    for i in range(len(accounts)):
        p =sum([x for x in accounts[i]])
        if p>=r:
            r=p
    return r
print(maximize_wealth([[1,5],[7,3],[3,5]]))