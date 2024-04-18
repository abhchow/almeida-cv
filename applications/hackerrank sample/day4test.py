def truckTour(petrolpumps):
    n = len(petrolpumps)
    
    start = 0
    end = 0
    curr_petrol = 0
    curr_dist = 0
    

    while start < n:
        
        curr_petrol += petrolpumps[end][0]
        curr_dist += petrolpumps[end][1]
        if curr_petrol > curr_dist:
            end = (end + 1) % n
            
            if end == start:
                return start
            
        else:
            # start += 1
            
            curr_petrol -= petrolpumps[start][0]
            curr_dist -= petrolpumps[start][1]
            curr_petrol -= petrolpumps[end][0]
            curr_dist -= petrolpumps[end][1]

            if start == end:
                end = (end + 1) % n
            start += 1

petrolpumps = [[1, 5], [10, 3], [3,4], [0,2], [1,7], [14, 3]]

print(truckTour(petrolpumps))