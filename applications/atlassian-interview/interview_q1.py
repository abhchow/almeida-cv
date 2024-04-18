#problem is about a hackathon
#implement a function to determine the winner of the hackathon

# output: list of winners
    #with their names

def findWinner(listVotes):
    """
    n is the number of ballots
    v is the maximum number of votes on a single ballot

    Args:
        listVotes (tuple list): a list of 3ples with 3 ordered names (strings)

    Returns:
        List of candidates ranked in descending order
    """

    candidates = dict()
    max_points = 3

    # counter = 0 # the total number of votes that have already been cast across all ballots
    for ballot in listVotes:                                        # O(n)
        for i in range(len(ballot)):                                # O(v)
            if ballot[i] not in candidates:
                # candidates[ballot[i]] = [0, counter]
                candidates[ballot[i]] = [0] + [0]*max_points
            candidates[ballot[i]][0] += max_points - i

            candidates[ballot[i]][i+1] += 1

            # candidates[ballot[i]][1] = counter
            # counter += 1

    candidatesList = list(candidates.items())                       # O(n)

    #loop
    for i in range(3,0,-1):
        candidatesList.sort(key=lambda tup: tup[1][i], reverse=True)    # O(vnlogn)

    candidatesList.sort(key=lambda tup: tup[1][0], reverse=True)    # O(nlogn)
                                                                    # O(vnlogn)
                                                                    # O(nv+nlogn)
    return [candidate[0] for candidate in candidatesList]


testCandidates = [("Albert", "Nick", "Hillary"), ("Nick", "Scott", "Mike"), ("Scott", "Albert", "Hillary"), ("Nick", "Albert", "Scott"), ("Mike","Scott","Albert"),("Nick","Scott","Albert"),("Raymond", "Chris", "Scott"), ("Chris", "Raymond", "Albert"), ("Rowan", "Daniel", "Albert")]#, ("Raymond", "Chris", "Nick"), ("Nick", "Scott", "Hillary"), ("Nick",), ("Nick", "Scott")]
# testCandidates = [("Nick",)]
print(findWinner(testCandidates))

"""
Albert  5,7
Nick    5,3
Hillary 2,8
Scott   5,6
Mike    1,5
"""

