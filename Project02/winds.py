# Dean Hickman
# CS 152 Project 02
# Task 6 -- Calculate Max wind speed using hightemp.py as template

# This is the main function
def main():
    """The main function opens up the .csv file GoldieMLRCJuly, and uses a for loop and if statements to search for wind speed to calculate their high and low values."""
hiWind=-10
loWind= 10
hidate = (",")
lodate = (",")

fp =open ("GoldieMLRCJuly.csv", "r")
line = fp.readline()
line = fp.readline()
for line in fp: #every line in the file is run through
        words = line.split (",") #for each line in the file the line is split by commas and assigned to the variable words 
        print(words)
        windSpeed= float(words[6]) #the seventh column of data is is assigned to the variable airtemp and cast as a float 
        date= str(words[0])#the first column of data is assigned to the variable date and cast as a string
        line= fp.readline()
        if hiWind> windSpeed: #compares if hiWind is greater than windSpeed 
            windSpeed= hiWind #sets the current hiWind to the windspeed if true
            hidate= date #sets the date that hiWind occurred if the previous line is true
        if windSpeed< loWind: #compares the windSpeed is less than loWind
            windSpeed= loWind #sets the current windSpeed to the loWind if true
            lodate= date #sets the date that the lodate occured if the previous line is true
print("High wind speed:",hiWind,"kilometers per hour","On:",hidate) #printes the hiWind value with a label
print("Low wind speed:",loWind,"kilometers per hour","On:",lodate) #prints the loWind with a label

if __name__== "__main__":
    main()
