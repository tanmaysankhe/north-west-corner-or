import copy
rows = int(input("Enter number of factories"))
cols = int(input("Enter number of shops"))

#first row
given = [0 for i in range(rows+2)]
given[0] = ["Factory/Shops"]
given[0].extend(tuple(["S" + str(i) for i in range(1,cols+1)]))
given[0].append("Cap")

for i in range(rows):
    col = ["Factory " +str(i+1) + "\t"]
    #print("Enter cost of" + str(cols) + "shop for factory " + str(i+1))
    cost = list(map(int, input().strip().split()))
    col.extend(tuple(cost))
    given[i+1] = col

#last row #edit hardcode last val
col = ["Reqiurements "]
cost = list(map(int, input().strip().split()))
col.extend(tuple(cost))
given[i+2] = col


print("----------------------------GIVEN--------------------------")

for row in range(len(given)):
    for col in range(len(given[0])):
        print(given[row][col],end='\t|\t')
    print()


print("----------------------------ANSWER--------------------------")

ans = copy.deepcopy(given)

row = 1
while row < len(ans)-1:
    col = 1
    while col < len(ans[0])-1:
        ans[row][col] = 0
        col += 1
    row += 1


# for row in range(len(ans)):
#     for col in range(len(ans[0])):
#         print(ans[row][col],end='\t')
#     print()

# print("lasy reg",ans[-1][-2])
#
# print(len(given))
row, col = 1, 1
total = 0

while True:
    avail = min(ans[row][-1],ans[-1][col])
    ans[row][col] = avail
    temp = (ans[row][col] * given[row][col])
    # print("temp",row,col,"ans",ans[row][col]," x ",given[row][col]," = ",temp)
    total += temp
    # print("rowcol",row,col,avail)
    ans[row][-1] -= avail
    ans[-1][col] -= avail


    if(ans[-1][col] == 0):
        col += 1
    if(ans[row][-1] == 0):
        row += 1

    if(ans[-1][-2] == 0):
        break



for i in range(len(ans)):
    for j in range(len(ans[0])):
        print(ans[i][j],end='\t|\t')
    print()

print("--------------------------TOTAL COST--------------------------")
print("Total cost = " + str(total))