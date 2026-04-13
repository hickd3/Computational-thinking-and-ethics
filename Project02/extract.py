# Dean Hickman
# CS 152 Project 02
# Task 7 -- Create a .csv file with extracted data and plot it 


#This is the main function
def main():
    """The main function opens the .csv file GoldieMLRCJuly reads it and then opens and writes the .csv file ExtractData. The function makes use of a for loop, variable assignements, and an if statment to analyze air temperature data to write in the new file"""
    fp = open("GoldieMLRCJuly.csv","r")# opens up the .csv file GoldieMLRCJuly and reads it
    fp2= open("ExtractData.csv", "w") # opens up the .csv file ExtractData and writes in it
    fp2.write("Date/Time" + "," + "Air Temperature" + "\n") #writes the headers into the file and starts a new line

    #main code
    """The line below assigns the function readline() to the variable line"""
    line= fp.readline()
    line=fp.readline()
    for line in fp: #every line in the file is run through
        words = line.split(",")#for each line in the file the line is split by commas and assigned to the variable words 
        time ="3:03:00 PM"#time is assigned the string of 15:03
        datetime= str(words[0])# the first column of data is assigned to the variable datetime, the cast here is redundant as the first column of data is already a string
        airtemp =float (words[5])#the sixth column of data is is assigned to the variable airtemp and cast as a float 
        line = fp.readline()
        if time in datetime:# checks to see if the time, 15:03, is in the data set 
            fp2.write(datetime+ "," + airtemp + "\n") #writes in the file the extracted data
              
    
    fp.close() #closes the .csv file GoldieMLRCJuly
    fp2.close()# closes the .csv file ExtractData

    # only call this function if this file is executed
if __name__=="__main__":
    main()