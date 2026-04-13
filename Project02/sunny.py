# Dean Hickman
# CS 152 Project 02
# Task 5 -- Calculate the number of sunny and cloudy days using hightemp.py as template


#This is the main function
def main():
    """This function opens the .csv file GoldieMLRCJuly using a for loop and if statements to read a data file. It assesses whether a day is cloudy or sunny depending on its PAR value and prints the average number of sunny/cloudy days in July"""
    numSunny= 0
    numCloudy=0
    sumSunny=0
    sumCloudy=0
    avgsunny=0
    avgcloudy=0
    """ All variables are initallized with the value of 0"""

    fp=open("GoldieMLRCJuly.csv", "r")# .csv file is opened to read
    line= fp.readline()#the readline() function is assigned to the variable line
    line= fp.readline()
    for line in fp:#every line in the file is run through
        words= line.split(",")  #for each line in the file the line is split by commas and assigned to the variable words 
        time= "12:03" #time is assigned the string of 12:03
        datetime= str(words[0])# the first column of data is assigned to the variable datetime, the cast here is redundant as the first column of data is already a string
        line= fp.readline()

        if time in datetime: # checks to see if the time, 12:03, is in the data set 
            par = float(words[4]) # the fifth column of data is assigned to the variable par and cast as a float
            if (par >800): #checks to see if par is less than 800
                numSunny= (numSunny + 1) #adds 1 to the variable numSunny then assigns that new value to the variable
                sumSunny= (sumSunny + par) #adds the value of par to sumSunny and then assigns that new value to the variable 
            else:
                numCloudy= (numCloudy + 1)#adds 1 to the variable numCloudy then assigns that new value to the variable
                sumCloudy= (sumCloudy+ par)#adds the value of par to sumCloudy and then assigns that new value to the variable 
    avgsunny= (sumSunny/numSunny) #calculates the average sunny days by division
    avgcloudy= (sumCloudy/numCloudy)#calculates the average cloudy days by division
    print("Average number of sunny days: %.3f" % (avgsunny))#prints the average number of sunny days with a label
    print("Average number of cloudy days: %.3f" % (avgcloudy))#prints the average number of cloudy days with a label

    fp.close()
# only call this function if this file is executed
if __name__ == "__main__":
    main()
