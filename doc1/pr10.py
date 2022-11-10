def mirror(arr): 
    arr2 = list(reversed(arr))
    for x in arr2 : arr.append(x)
# ссоздала список перевернутых и добавила элементы этого списка в исходный список

##arr = [1, 2]
##mirror(arr)
##print(*arr)
##
##arr = [1]
##mirror(arr)
##print(*arr)
