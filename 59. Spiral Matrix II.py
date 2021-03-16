def generateMatrix(n):
    matrix = matrix = [[0 for col in range(n)] for row in range(n)]
    dim1, dim2 = n, n
    top, bot, left, right = 0, dim1, 0, dim2
    count, i, j = 0, 0, 0
    num_list = list(range(1, n**2+1))
    while True:
        i, j = top, left
        for j in range(left, right):
            matrix[i][j] = num_list[count]
            count += 1
            if count == dim1*dim2: return matrix
        i, j = top+1, right-1
        for i in range(top+1, bot):
            matrix[i][j] = num_list[count]
            count += 1
            if count == dim1*dim2: return matrix
        i, j = bot-1, right-2
        for j in range(right-2, left-1, -1):
            matrix[i][j] = num_list[count]
            count += 1
            if count == dim1*dim2: return matrix
        i, j = bot-2, left
        for i in range(bot-2, top, -1):
            matrix[i][j] = num_list[count]
            count += 1
            if count == dim1*dim2: return matrix
        top, bot, left, right = top+1, bot-1, left+1, right-1
