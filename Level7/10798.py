# 0,0 
# 1,0 
# 2,0 
# 3,0 
# 4,0


# 0,1 
# 1,1 
# 2,1
# 3,1 
# 4,1

words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end = '')
