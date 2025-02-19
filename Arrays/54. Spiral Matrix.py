def spiralOrder(matrix):
    toReturn = matrix.pop(0)
    while (matrix):
        for i,v in enumerate(matrix):
            if v:
                toReturn.append(v.pop())
            if i + 1 == len(matrix):
                toReturn.extend(matrix.pop(i)[::-1]) 
                print(f'First Loop: {toReturn}')
                break

        for i in range(len(matrix)-1,-1,-1):
            if (matrix[i]):
                toReturn.append(matrix[i].pop(0))
            if i-1 == -1:
                toReturn.extend(matrix.pop(i))
                print(f'Second Loop: {toReturn}')
                break;
    return toReturn

spiralOrder([[7],[9],[6]])
