'''

Experiment No. 7 : Write a python program for MAGIC SQUARE.
                   A magic square is an n*n matrix of the integers 1 to (n^2) such that the sum of each row,
                   column and diagonalis the same.
                   The figure given below is an example of the magic square for case n=5. In this example
                   the common sum is 65.

                   9  |   3  |  22  |  16  |  15  |
                   2  |  21  |  20  |  14  |   8  |
                  25  |  19  |  13  |   7  |   1  |
                  18  |  12  |   6  |   5  |  24  |
                  11  |  10  |   4  |  23  |  17  |

Conditions for placing the values in the matrix in appropriate manner (CIRCULAR ARRAY) :

   1. The position of next number is calculated by decrementing row number of previous number by 1, and incrementing
      the column number of previous number by 1. At any time, if the calculated row position becomes -1, it will wrap
      around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.

   2. If the magic square already contains a number at the calculated position, calculated column position will be
      decremented by 2, and calculated row position will be incremented by 1.

   3. If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2).
'''


# A function to generate odd
# sized magic squares

def generate_Magic_Square(size):
    magicSquare=[[0 for x in range(size)] for y in range(size)]

    # Initializing first position of matrix
    i=size/2
    j=size-1

    # Fill the magic square by placing values at appropriate position
    num=1
    while num<=(size*size):
        if i==-1 and j==size:  # 3rd Condition
            j=size-2
            i=0
        else:
            # next number goes out of right side of square
            if j==size:
                j=0

            # next number goes out of upper side
            if i<0:
                i=size-1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num=num+1

        j=j+1
        i=i-1  # 1st condition

    # Printing of magic square
    sum=size*(size*size+1)/2
    print("Sum of each row or column is : ",sum)
    print("Magic Square of size",size,"*",size,"is : \n")

    for i in range(0,size):
        for j in range(0,size):
            print(' %2d ' % (magicSquare[i][j]),end=' | ')

            # To display magic square in matrix form
            if j==size-1:
                print()

#<------------------------------------------------------------------------------------------------->

#Main function

flag=1
while flag==1:
    n=int(input("\nEnter the size of the MAGIC SQUARE : "))
    if n%2==0:
        s=int(input("Please enter an ODD Number (for example - 3,5,7,9,....) : "))
        generate_Magic_Square(s)
    else:
        generate_Magic_Square(n)
    a=input("\nDo you want to print Magic Square of some other size (yes/no) : ")
    if a=='yes':
        flag=1
    else:
        flag=0
        print("\nThanks for using this program!")

#<------------------------------------------ END OF PROGRAM ----------------------------------------->


