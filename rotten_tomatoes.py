def _isvalid(i,j,r,c):
    if i>=0 and i<r:
        if j>=0 and j<c:
            return True
    return False


a= [[2, 1, 0, 2, 1],[1, 0, 1, 2, 1],[1, 0, 0, 2, 1]]
c = len(a[0])
r = len(a)   

que = []
for i in range(r):
    for j in range(c):
        # print(i,j, a[i][j])
        if a[i][j] == 2:
            que.append((i,j))
delimiter = (-1,-1)
que.append(delimiter)
ans = 0
# print(que)
while que:
    current = que.pop(0)
    if current[0] == -1 and current[1] == -1:
        if que:
            current = que.pop(0)
            que.append((-1,-1))
            ans += 1
        else:
            print(ans)
            break
    # print(current)
    if _isvalid(current[0]+1, current[1], r, c) and a[current[0]+1][current[1]] == 1:
        que.append((current[0]+1, current[1]))
        a[current[0]+1][current[1]] = 2
    if _isvalid(current[0], current[1]+1, r, c) and a[current[0]][current[1]+1] == 1:
        que.append((current[0], current[1]+1))
        a[current[0]][current[1]+1] = 2
    if _isvalid(current[0]-1, current[1], r, c) and a[current[0]-1][current[1]] == 1:
        que.append((current[0]-1, current[1]))
        a[current[0]-1][current[1]] = 2
    if _isvalid(current[0], current[1]-1, r, c) and a[current[0]][current[1]-1] == 1:
        que.append((current[0], current[1]-1))
        a[current[0]][current[1]-1] = 2 
    if ans <= 1:
        print(que)
    

