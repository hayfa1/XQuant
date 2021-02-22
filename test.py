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
            if (table[i][j]==number[0] and not visited[i][j]):
                # Make the cell visited to not use it more than one in the same solution
                visited[i][j]= True
                #Put the first number indexes in variables in order to save them
                Index_i=i
                Index_j=j
                k=1
                while k<len(number):
                   
                    # handle the exception 
                    try:
                        #Search in top cell
                        if((Index_i+1<n) and (number[k]==table[Index_i+1][Index_j]) and not visited[Index_i+1][Index_j]):
                            Index_i=Index_i+1
                            path.append((Index_i,Index_j))
                            # Make the cell visited to not use it more than one in the same solution
                            visited[Index_i][Index_j]= True
                        #Search in Buttom cell
                        elif((Index_i-1>=0) and (number[k]==table[Index_i-1][Index_j]) and not visited[Index_i-1][Index_j]):
                            Index_i=Index_i-1
                            path.append((Index_i,Index_j))
                            # Make the cell visited to not use it again
                            visited[Index_i][Index_j]= True
                        #Search in right cell
                        elif((Index_j+1<n) and(number[k]==table[Index_i][Index_j+1]) and not visited[Index_i][Index_j+1]):
                            Index_j=Index_j+1
                            path.append((Index_i,Index_j))
                            # Make the cell visited to not use it again
                            visited[Index_i][Index_j]= True
                        #Search in left cell
                        elif((Index_j-1>=0) and (number[k]==table[Index_i][Index_j-1]) and not visited[Index_i][Index_j-1]):
                            Index_j=Index_j-1
                            path.append((Index_i,Index_j))
                            # Make the cell visited to not use it again
                            visited[Index_i][Index_j]= True
                        else:
                            #print("no")
                            break;
                        #continue
                        k+=1
                    except:
                        break
                #if all the input numbers were founded, their indexes will be saved in a list
                if k==len(number):
                    # Concatenate the first number indexes with the other indexes
                    L=[(i,j)]+path
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
    #Table=np.random.randint(10, size=(10,10))
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
    Table1=np.random.randint(10, size=(10,10))
    #print(Table1)
    #Number=8292
    Number=input("Please enter the number that you want to find ")
    AllSolutions=SearchNumberInTable(10,Table,Number)
    for i in range (0, len(AllSolutions)):
        print("Path number "+str(i+1)+" is "+str(AllSolutions[i]))
    
    