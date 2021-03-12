def isValidSerialization(preorder):
    preorder = preorder.split(',')
    diff = 0 # difference of indegree and outdegree
    for node in preorder:
        if diff < 0:
            return False
        diff += 1 if node != "#" else -1
    if diff == -1:
        return True
    else:
        return False
