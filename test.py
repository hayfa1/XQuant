import numpy as np

def SearchNumberInTable(SizeTable,table,Number):
    n=SizeTable
    #List that will contain the indexes of all the paths found
    AllSolutions=[]
    # temp list that contains the indexes of the paths found
    path=[]
    #Split the input into a list in order to iterate over the numbers
    number=[int(x) for x in str(Number)]
    for i in range (n):
        for j in range (n):
            #Defining visited array to keep track of already visited indexes
            visited = [[False for m in range (n)] for y in range (n)]
            #Search for the first number
            if (table[i][j]==number[0]):
                #Put the first number indexes in variables in order to save them
                x=i
                y=j
                # Make the cell visited to not use it more than one in the same solution
                visited[i][j]= True
                k=1
                while k<len(number):
                    # handle the exception  where the table borders are exceeded by i and j
                    try:
                        if((number[k]==table[i+1][j]) and not visited[i+1][j]):
                            i=i+1
                            path.append((i,j))
                            # Make the cell visited to not use it again
                            visited[i][j]= True
                        elif((i-1>=0) and (number[k]==table[i-1][j]) and not visited[i-1][j]):
                            i=i-1
                            path.append((i,j))
                            # Make the cell visited to not use it again
                            visited[i][j]= True
                        elif((number[k]==table[i][j+1]) and not visited[i][j+1]):
                            j=j+1
                            path.append((i,j))
                            # Make the cell visited to not use it again
                            visited[i][j]= True
                        elif((j-1>=0) and (number[k]==table[i][j-1]) and not visited[i][j-1]):
                            j=j-1
                            path.append((i,j))
                            # Make the cell visited to not use it again
                            visited[i][j]= True
                        else:
                            break;
                        #continue
                        k+=1
                    except:
                        break
                #if all the input numbers were founded, their indexes will be saved in a list
                if k==len(number):
                    # Concatenate the first number indexes with the other indexes
                    L=[(x,y)]+path
                    # Save the indexes into a list
                    AllSolutions.append(L)
                    #Clear the list
                    path=[]
                #else the indexes will be deleted 
                elif k<len(number):
                    #Clear the list
                    path=[]
    print("The input was find "+ str(len(AllSolutions))+" time(s)")
    return AllSolutions

if __name__ == "__main__":
    Table=([[1, 5, 7, 4, 6, 2, 2, 6, 7, 2],
            [2, 8, 2, 9, 3, 9, 8, 5, 6, 2],
            [3, 4, 0, 2, 4, 3, 0, 2, 6, 7],
            [1, 5, 7, 3, 4, 5, 2, 7, 9, 7],
            [6, 2, 8, 8, 6, 7, 9, 6, 9, 7],
            [0, 2, 0, 3, 3, 5, 2, 3, 5, 5],
            [5, 5, 5, 0, 6, 6, 8, 5, 9, 0],
            [0, 5, 7, 6, 0, 6, 9, 9, 6, 7],
            [5, 5, 8, 5, 0, 8, 5, 3, 5, 5],
            [0, 0, 6, 3, 3, 3, 9, 5, 9, 9]])
    #table=np.ones((10,10))
    #Number=8292
    Number=input("Please enter the number that you want to find ")
    AllSolutions=SearchNumberInTable(10,Table,Number)
    for i in range (0, len(AllSolutions)):
        print("Path number "+str(i+1)+" is "+str(AllSolutions[i]))
    
    