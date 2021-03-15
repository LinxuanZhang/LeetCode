def spiralOrder(matrix):
    dim1, dim2 = len(matrix), len(matrix[0])
    top, bot, left, right = 0, dim1, 0, dim2
    count, i, j = 0, 0, 0
    result = []
    while True:
        i, j = top, left
        for j in range(left, right):
            result.append(matrix[i][j])
            count += 1
            if count == dim1*dim2: return result
        i, j = top+1, right-1
        for i in range(top+1, bot):
            result.append(matrix[i][j])
            count += 1
            if count == dim1*dim2: return result
        i, j = bot-1, right-2
        for j in range(right-2, left-1, -1):
            result.append(matrix[i][j])
            count += 1
            if count == dim1*dim2: return result
        i, j = bot-2, left
        for i in range(bot-2, top, -1):
            result.append(matrix[i][j])
            count += 1
            if count == dim1*dim2: return result
        top, bot, left, right = top+1, bot-1, left+1, right-1
