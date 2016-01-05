#setting global varibles For start and finish time, these are defined
#in inport() where we find the values of Start and Finish from the text file
S = 0
F = 0

def inport ():
    programs = []
    with open ('SpacePrograms.txt') as inputfile:
        for line in inputfile:
            temp = []
            for x in line.split('\t'):
                temp.append(int(x))
            programs.append(temp)
    #use pop function to get the list that contains start and finish times
            #then pop elements from that list into S and F
    SF = programs.pop(0)
    global S
    S = SF.pop(0)
    global F
    F = SF.pop(0)
    programs.pop(0)
    return programs;

#greedy algorithm to find the optimal set in the spacePrograms.txt
def greed ():
    pro = inport()
    x = 0
    global S
    global F
    #removes all elements from the list that have a finish time less than S
    for i in pro:
        if i[2] <= S:
            del pro[x]
        x+=1
    #Finding the first program start time that starts before S and has
    #the longest run period
    selPro=[[]]
    temp = 0
    #sorts the list of lists based on the second element in each list (Strt time)
    pro = sorted(pro,key=lambda x: x[1])
    for i in pro:
        #confirms start time program to be <= S and each run stores the longsest
        #program length
        if i[1] <= S and (i[2] - i[1]) > temp:
            temp = i[2] - i[1]
            selPro[0] = [i]

 
    #Finding the rest of the programs based on when they start and checking
    #end time
    selPro = selPro.pop(0)
    n = 0
    #same concept as above, while loop confirms that the last program attached to
    #selectedPrograms(selPro) has a finish greater than F
    while selPro[n][2] < F:
        selPro.append([])
        temp = selPro[n]
        spot = 0
        n+=1
        x=0
        y=0
    #x and y are to keep index's in check so when we find a program to append to
        #selPro we know it's index, otherwise runs the same as finding the first
        #program, replace start time comparison with end time comparison of the
        #last program added to selPro
        for i in pro:
            if i[1] <= temp[2] and i[2] > temp[2] and (i[2] - i[1]) > spot:
                spot = i[2] - i[1]
                selPro[n] = i
                y = x
            x+=1
        pro.pop(y)
    return selPro

#Part 2: to partition the set so Group 1 and Group 2 have similar start times
def partition ():
    #L1 , L2 list of weights, L3 list of lists of project number and weigths
    projects = greed()
    L1 = []
    L3 = [[]]
    n=0
    #Finding the Weights,
    for i in projects:
        L3.append([])
        temp = i[2] - i[1]
        L1.append(temp)
        L3[n] = [projects[n][0],temp]
        n+=1
    L3.pop()
    L3 = sorted(L3, reverse=True, key=lambda x: x[1])

    #Algortihm to calculate the partitions only works on a list of weights
    #calculate mid value
    #sort in descending order
    #after adding largest value to L2, go through L1 and find the next largest
    #value that when added to L2 will keep total sum < mid, do this until you
    #can't find another value and that is the optimal set
    mid = sum(L1)/2
    L1 = sorted(L1, reverse=True)
    L2 = [L1.pop(0)]
    currentSum = sum(L2);
    x=0
    for i in L1: 
        if i+currentSum < mid:
            L2.append(L1.pop(x))
        currentSum = sum(L2)
        x+=1
    #record the total weights of partitioned list and attach it to
    #the return statement (a list of lists conatining optimal project numbers)
    S = [sum(L1), sum(L2)]
    x = 0
    #These next for loops convert L1 and L2 from weights to thier corresponding
    #project numbers.
    #could have partitioned with the project numbers attached but it was eaiser
    #to implement with only wieghts, I then took the brute force way to find
    #the project numbers attached to each weight in partitioned lists
    #each nest for loop tests through L1 and L2, could have combined the loops but
    #cleaner and easier to read this way
    for i in L3:
        for x,j in enumerate(L1):
            if j == i[1]:
                L1[x] = i[0]
                L3.pop(x)
                break
        x+=1
    L2 = sorted(L2)
    for i in L3:
        for x,j in enumerate(L2):
            if j == i[1]:
                L2[x] = i[0]
                break
    
    L1 = [L1]
    L1.append(L2)
    L1.append(S)
    #L1 conatins 3 lists, (2) partitioned lists with project numbers
    #(1) list of the total weigths corresponding to each partitioned list
    return L1

def main ():
    pro = greed()
    Selects = partition()
    Times = Selects.pop()
    List = sum(Selects, [])
    List = sorted(List)
    print "The selected projects : "
    print List
    print "Group 1 Projects: "
    print Selects[0]
    print "Total time: "
    print Times[0]
    print "Group 2 Projects: "
    print Selects[1]
    print "Total time: "
    print Times[1]

main ();
    
