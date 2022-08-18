# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""
5 4 3 2 1            
  4 3 2 1               
    3 2 1                   
      2 1                     
        1
"""

#i = 
max = 5
"""
def printpattern():
    count = 0
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        #print('\r')
        count += 1
        print() # new line
"""  
def printpattern():
    max_num = 5
    for i in range(5, 0, -1):
        num = max_num
        for j in range(5, 0, -1):
            if j > i:
                print(" ", end=' ')
            else:
                print(num, end=' ')
                num -= 1
        print("")
        max_num -= 1

if __name__ == "__main__":
    printpattern()
   
