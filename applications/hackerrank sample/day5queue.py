# Enter your code here. Read input from STDIN. Print output to STDOUT

q = int(input("")) #Enter number of queries:

s1 = []
s2 = []
n = 0

for i in range(q):
    query = input("")
    
    # enqueue
    if query[0] == '1':
        value = query[2:]
        
        for j in range(n):
            s2.append(s1.pop())
            
        s1.append(value)
            
        for j in range(n):
            s1.append(s2.pop())
            
        n += 1
        
    # dequeue front
    elif query[0] == '2':
        s1.pop()
        n -= 1
    
    # print front
    elif query[0] == '3': #else
        print(s1[-1])
        
