###3
##            *
##            * *
##            * * *
##            * * * *
##            * * * * *
##
def pattern(n):
    for i in range(n):
        for j in range(n):
            if  i+j<=2*i:#i-j<=0
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern(5)
