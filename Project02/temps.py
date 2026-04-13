# Dean Hickman
# CS 152 Project 02
# Task 4 -- Calculate Max/ Min statistics using hightemp.py as template

# This is the main function
def main():
    """The main function opens up the .csv file GoldieMLRCJuly, and uses a for loop and if statements to search for air/water temperature to calculate their high and low values."""
    hiairtemp= -200
    hiwatertemp = -200
    loairtemp = 200
    lowatertemp= 200
    """The above lines of code are variables with intitialized values of large negative and positive integers"""
    
    hiairdate= (",")
    hiwaterdate= (",")
    loairdate = (",")
    lowaterdate = (",")
    """The line below opens up the .csv file and reads it"""
    fp =open ("GoldieMLRCJuly.csv", "r")
    """The line below assigns the function readline() to the variable line"""
    line = fp.readline()
    line = fp.readline()
    for line in fp: #every line in the file is run through
        words = line.split (",") #for each line in the file the line is split by commas and assigned to the variable words 
        print(words)
        temp3m= float(words[1]) #the second column of data is assigned to the variable temp3m and cast as a float
        airtemp= float(words[5]) #the sixth column of data is is assigned to the variable airtemp and cast as a float 
        date= str(words[0])#the first column of data is assigned to the variable date and cast as a string
        line= fp.readline()
        if airtemp> hiairtemp: #compares if airtemp is greater than hiairtemp 
            hiairtemp= airtemp #sets the current airtemp to the hiairtemp if true
            hiairdate= date #sets the date that airtemp occurred if the previous line is true
        if airtemp< loairtemp: #compares the airtemp is less than loairtemp
            loairtemp = airtemp #sets the current airtemp to the loairtemp if true
            loairdate= date #sets the date that the airtemp occured if the previous line is true
        if temp3m> hiwatertemp: #compares the water temperature is greater than hiwatertemp
            hiwatertemp= temp3m # sets the current water temperature to hiwatertemp if true
            hiwaterdate= date #sets the date that the water temperature occured if previous line is true
        if temp3m< lowatertemp: #compare water temperature is less than lowatertemp
            lowatertemp= temp3m #sets the current water temperature to lowatertemp if true
            lowaterdate= date #sets the date that the water temperature occured if previous line is true

    print("High air temperature:",hiairtemp,"degrees Celsius","On:",hiairdate) #printes the hiairtemp value with a label
    print("Low air temperature:",loairtemp,"degrees Celsius","On:",loairdate) #prints the loairtemp with a label
    print("High water temperature:",hiwatertemp,"degrees Celsius","On:",hiwaterdate) #prints the hiwatertemp with a label
    print("Low water temperature:",lowatertemp,"degrees Celsius","On:",lowaterdate) #prints the lowatertemp with a label
    fp.close()
    
#only call main if this file was executed
if __name__ == "__main__":
    main()


