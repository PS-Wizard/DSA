breaksArr = [False] * 10 + [True] * 10

def TwoBalls():
    print(breaksArr)
    i = 0
    jumpThreshold = int(len(breaksArr)**0.5)
    while(not breaksArr[i] and i < len(breaksArr)):
        i += jumpThreshold
    
    for j in range(, i+1):
        if breaksArr[j]:
            return j

    return -1

print(TwoBalls())
