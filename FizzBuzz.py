def fizzbuzz(n):
    res=[]
    for i in range(n):
        s=""
        if i%3==0:
            s+="Fizz"
        if i%5==0:
            s+="Buzz"
        if not(s):
            s=str(i)
        res.append(s)
    return res
