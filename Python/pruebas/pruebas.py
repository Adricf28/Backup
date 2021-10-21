def array_dif(a, b):
    for i in a:

        if i not in b:
            b.append(i)
    
    print(b)
        

list1 = [1,2,2]
list2 = [1]
        
array_dif(list1, list2)