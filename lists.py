def revList(listB):
    if len(listB) == 1:       
        #If there is only one value in the list, then it will just return the list the same way it started.
        return listB 
    else:
        #what this next part does is takes the list and shaves off everything but the first element (element 0) and repeatedly does this until only one value is in the list.
        #Then it basically appends the list in reverse order by calling itself multiple times.
        return revList(listB[1:]) + [listB[0]]

print(revList([8, 24, 52, 55, 61, 21]))
#prints the list [8, 24, 52, 55, 61, 21] backwards to [21, 61, 55, 52, 24, 8]
#This list is the most current Power Ball winning numbers so if you had those, send money please!