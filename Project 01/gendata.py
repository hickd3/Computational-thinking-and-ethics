"""Dean Hickman
9/20/22
CS152
Task 3
Project 01"""
"""Begin Task 3d, statement, variable assignment, and test"""
pi=1   
vi=11    
t=0.5
a=-10 
pf= pi+ ((vi*t)+ (0.5*a*t**2))
print(pf)
""" Begin Task 3e, function definition and test"""
def ballistic1(t):
   """Returns the final position of an object given specified parameters""" 
   pi=1   
   vi=11    
   a=-10 
   pf= pi+ ((vi*t)+ (0.5*a*t**2))
   return(pf)
y= ballistic1(0.5)
y= ballistic1(1.0)

print ("f(1.0) is",y)
"""End of Task 3. Begin Task 4 a more general ballistic trajectory"""
def ballistic2(pi,vi,a, t):
    """ Returns the ballistic trajectory for any object"""
    pf= pi+ ((vi*t)+ (0.5*a*t**2))
    return(pf)
test= ballistic2(2,11,-10,0.5)
y=ballistic2(pi,vi,a,t)
print('', y)
"""End Task 4. Begin Task 5 to find a point"""
def computeAndOutput(pi, vi, a, t):
    """Computes a point and print it out"""
    y= ballistic2(pi,vi,a,t) 
    """This line is Task 9 it opens a file and assigns it a refernce variable"""
    fp = open (' hickdata.csv' , 'a')
    fp.write ( str(t) + "," + str(y)+ "\n")
    fp.close()
    print( t, ',', y )
"""End Task 5. Begin Task 6 compute ten points"""
def trajectory10(pi,vi,a,t):
    """Computes ten points of trajectory"""
    computeAndOutput(pi,vi,a,(t+(0* 0.1)))
    computeAndOutput(pi,vi,a,(t+(1* 0.1)))
    computeAndOutput(pi,vi,a,(t+(2* 0.1)))
    computeAndOutput(pi,vi,a,(t+(3* 0.1)))
    computeAndOutput(pi,vi,a,(t+(4* 0.1)))
    computeAndOutput(pi,vi,a,(t+(5* 0.1)))
    computeAndOutput(pi,vi,a,(t+(6* 0.1)))
    computeAndOutput(pi,vi,a,(t+(7* 0.1)))
    computeAndOutput(pi,vi,a,(t+(8* 0.1)))
    computeAndOutput(pi,vi,a,(t+(9* 0.1)))

y= trajectory10(1,11,-10,0)
y= trajectory10(1,11,-10,1)
    """ Task 11 Extension"""
    # the addition of + x to the parameter t will allow the user to control the step size by any integer it is the same process for the other function trajectory100()
 # def trajectory10(pi,vi,a,t):
    #x
    #computeAndOutput(pi,vi,a,t+ (x*0.1))
"""End of Task 6. Being Task 7 compute 100 points"""
def trajectory100( pi, vi, a, t):
    """Computes 100 points of trajectory with only ten interations of code"""
    trajectory10(pi,vi,a,(t+0))
    trajectory10(pi,vi,a,(t+1))
    trajectory10(pi,vi,a,(t+2))
    trajectory10(pi,vi,a,(t+3))
    trajectory10(pi,vi,a,(t+4))
    trajectory10(pi,vi,a,(t+5))
    trajectory10(pi,vi,a,(t+6))
    trajectory10(pi,vi,a,(t+7))
    trajectory10(pi,vi,a,(t+8))
    trajectory10(pi,vi,a,(t+9))
    
y=trajectory100(1,50,-10,0)
""" End of Task 8. Continutation of Task 9 managing the file"""
fp = open (' hickdata.csv' , 'a')
fp .write( str(t) + "," + str(pf)+ "\n")
fp.close()
"""Task 11 Extenstion"""
#The patttern thus far is that you will only have to write at most ten lines of code per function to create that amount of point, i.e. I would only need to copy my trajectory100() ten times to get 1000 points of code.
# Creating a loop:
#tvalue=0
#tnewValue
#while tvalue<= 10:
    #trajectory10(pi,vi,a,t)
    #tvalue + 1 = tnewValue
def clearfile():
    """Clearfile clears the file of the previous materials before calling trajectory100()"""
    fp = open( 'data.csv','w' )
    fp.close()
clearfile()
