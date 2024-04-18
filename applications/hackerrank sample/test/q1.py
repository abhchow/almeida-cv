def countTeams(rating, queries):
    ratingSorted = [0]*len(rating)
    for i in range(len(rating)):
        ratingSorted[i] = [rating[i], i]
        
    takeFirst = lambda x: x[0]
    ratingSorted.sort(key=takeFirst)
    pass

rating = [4,2,1,6,2,1,6,21]

countTeams(rating, 1)

def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)