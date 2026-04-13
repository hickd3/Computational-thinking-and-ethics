# Dean Hickman

# CS 152 Project 04

# 18 Oct 2022

# The program models the change in penguin population in the Galapagos over time given ecological pressures, by modeling the risk of extinction over some number of years.
#In the terminal run the program by typing "python3 penguin.py"





import random                       #imports the random package

import sys                          #imports the sys package

import matplotlib.pyplot as plt            #imports the matplotlib package for use as a plot



"""The function below returns a list of a population based on the paramters: the inital population and the probabilty of a penguin being female."""

def initPop(PopSize, probFem):      #Funtion initPop is defined by its parameters, the population size and the probability of a penguin being female

    Population= []                  #Population is initialized as an empty list that will be appended later on in the funtion

    for i in range(PopSize):        #A for loop assesing the size of the population

        num= random.random()        #For i in the size of the population a number "num" will be assigned a random value using random.random()

        if num < probFem:           #Checks to see if num is less than the probability of a female penguin

            Population.append("F")  #If the above is true the list Population will be appended by adding "F" to the list

        else:                       #If the inequality is false...

            Population.append("M")  #An "M" will be appeneded to the list Population

    return Population               #The list will be returned

#test function for initPop



def test():

    PopSize = 10

    probFem = 0.5



    pop = initPop(PopSize, probFem)



    print(pop)



if __name__== "__main__":

    test()

"""This function determines if it is an El Nino year based on the following six parameters:

(Pop) the population list, (elNinoProb) the probability of an El Nino year, (stdRho) the standard growth

rate, (elNinoRho) the growth rate in an El Nino year, (probFem) the probability of a femal penguin, amd (maxCap)

the carrying capacity of the ecosystem. If it is an El Nino year append the list"""



def simulateYear(pop, elNinoProb, stdRho, elNinoRho, probFem, maxCap):      #Function defintion with arguments

    elNinoYear = False                                                      #Assigns the varible False

    if elNinoProb > random.random():                                        #Checks if the varible is greater than the random value generated

        elNinoYear = True                                                   #Reassigns the variable to True                                   

    newPop =[]                                                              #An empty list is created for the variable newPop

    for i in pop:                                                           #Runs for every penguin in the population

        if (len(newPop)) > maxCap :                                         #Checks to see if the length of the new population list is greater than the carrying capacity

            break                                                           #If true then break we dont want to add anymore penguins

        if elNinoYear == True:                                              #Checks to see if elNinoYear is equivalent to true

            if random.random() < elNinoRho:                                 #Checks to see if the random value is less than the El Nino growth rate

                newPop.append(i)                                            #If the above is true we append the new population list and return it

        else:                                                               #Otherwise we append and run through other conditionals

            newPop.append(i)

            if random.random()< (stdRho-1):                                 #Checks to see if random value is less than the standard growth rate minue 1, if it is return newPop

                if random.random() < probFem:                               #Checks to see if random value is less than the probability of a femal penguin if true append F to the list otherwise append M

                    newPop.append("F")

                else:

                    newPop.append("M")

    return newPop

    

#test function for simulateYear

def test(): 

    PopSize = 10

    probFem = 0.5



    pop = initPop(PopSize, probFem)

    

    newPop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)



    print( "El Nino year" )

    print( newPop )



    newPop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)



    print( "Standard year" )

    print( newPop )

if __name__== "__main__":

    test()



"""This function runs the simulation N number of times with eight parameters: the number of years

to run the simulation (N), the initial population size (initPopSize), the probability of a fenale penguin (probFem),

the probability of an El Nino year (elNinoProb), the growth rate in an El Nino Year (elNinoRho), the standard growth rate (stdRho),

the carrying capacity of the ecosystem (maxCap), and the minimum viable population (minViable). The function checks for the year of extinction."""

def runSimulation(N, initPopSize, probFem, elNinoProb, elNinoRho, stdRho, maxCap, minViable):       #Function definition with parameters

    PopSize = 10                                                                                    #The next 5 lines of code are varible declaraction and assignment (initialization)

    probFem = 0.5

    population = initPop(initPopSize, probFem)

    termDate = N

    pop = initPop(PopSize, probFem)

    for i in range ( 1 , N + 1):                                                                #Iterating over a set range of values from 1 up to N+1 not including N+1 so from 1 to N

        newPopulation = simulateYear(pop, elNinoProb, stdRho, elNinoRho, probFem, maxCap)

        if (len(population)> minViable) and ("F" in newPopulation) and ("M" in newPopulation):      #If the length of the population list is greater than the minimum viable population and the new population has at least one female and male, then that new population is now the population we care to work with

           population = newPopulation 

        else:                                                                                   #Otherwise we break and record the index value as the year in which the species died off

            termDate = i

            break

    return (termDate)



#test function for runSimulation

def test():

    PopSize = 10

    probFem = 0.5



    pop = initPop(PopSize, probFem)

    

    newPop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)



    print( "El Nino year" )

    print( newPop )



    newPop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)



    print( "Standard year" )

    print( newPop )

    for i in range (10):

        runSimulation(201,500,0.5, (1/7), 0.41, 1.188,2000,10)

    return (newPop)

if __name__== "__main__":

    test()



"""This top level code is the main function with one parameter argv. It tests if there are at least three arguments on the command line if there aren't

a usage statement is printed and the function is exited. With this we can also extract values from the command line and assign them meaning,

like the second argument will be cast as integer telling us the years between an El Nino event."""

def main(argv):

    if (len(sys.argv) < 3): 

        print ("Enter: " ,[1], "program name", [2], "number of simulations to run", [3], "the number of years between an El Nino event")      #In the command line fill in the arguments to run 

        return

    numSimulations= int(sys.argv[1])                                                                                                            #For the next two lines we declare a variable to be cast as an integer from a list

    extYears= int(sys.argv[2])

    simResults = []                                                                                                                                #The next two lines are variables set to empty lists so they can be appended as we iterate over them 

    CEPD = []

    N = 201                                                                                                                                            #The next 9 lines of code are default parameters being initialized

    initPopSize = 500

    probFem = 0.5

    elNinoProb= (1 / extYears)

    elNinoRho= 0.41

    stdRho= 1.188

    maxCap= 2000

    minViable= 10

    extinct = 0

    

    for i in range (numSimulations):                                                                        #Iteration over the range that the user inputs

        Results= runSimulation(N, initPopSize, probFem, elNinoProb, elNinoRho, stdRho, maxCap, minViable)

        simResults.append(Results)                                                                          #The results of the simulation are appended to a new list

        if simResults[i] < N:

            extinct= extinct+1

    end =( extinct / numSimulations)

    print("The overall possibility that penguins will go extinct in the next" , N, "years:  ", (end *100), "%")

    

    """This function takes the results and turns it into a Cumulative Extinction Probability Distribution (CEPD)

    The CEPD will go up to N and display Y, the number of simulations where the population has gone extinct."""

    def computeCEPD(simResults, N):
        CEPD= []                                    #CEPD is an empty list

        for i in range(N):

            CEPD.append(0)                          #Create the list CEPD with N zeros

        for i in simResults:

            if i < N:

                while i < N:                        #Loop from i to N

                    CEPD[i] = CEPD[i] +1            #Add  entry into  CEPD list

                    i = i+1 

        for i in range (len(CEPD)):                  #Loop over the CEPD list

            CEPD[i] =(CEPD[i]/len(simResults))         #Divide each entry by the length of the extinction year results list, which is also the number of simulations

        return CEPD                                 #Return the list

    CEPD= computeCEPD(simResults, N)

    year = []

    probability = []

    

    for i in range (0, N, 10):                                              #Every 10th entry in the CEPD list will be printed and plotted

        print("In the year: ", i, "the probability of extinction is: " , CEPD[i]*100, "%")
        

    

    plt.plot( year, probability, "bo--")

    plt.title("CEPD run #1 of 1000 simulations for 201 years with default parameters")
if extYears == 3:

            for i in range (0, N, 10):

                year = i
            year.append(i)
            probability= (CEPD[i]*100)
        probability.append((CEPD[i]*100))

        plt.plot( year, probability, "ro--")

        plt.title("CEPD vs. Year, 3 Year El Nino Cycle")

        plt.xlabel("Year")

        plt.ylabel("CEPD")

        plt.show()

        if extYears == 5:

            for i in range (0, N, 10):

                year = i
            year.append(i)

            probability= (CEPD[i]*100)
        probability.append((CEPD[i]*100))

        plt.plot( year, probability, "ro--")

        plt.title("CEPD vs. Year, 5 Year El Nino Cycle")

        plt.xlabel("Year")

        plt.ylabel("CEPD")

        plt.show()

        if extYears == 7:

            for i in range (0, N, 10):

                year = i
        year.append(i)

        probability= (CEPD[i]*100)
    probability.append((CEPD[i]*100))


    plt.plot( year, probability, "ro--")

    plt.title("CEPD vs. Year, 7 Year El Nino Cycle")

    plt.xlabel("Year")

    plt.ylabel("CEPD")

    plt.show()

    

    for i in range (0, N, 10):

        year.append(i)

        probability.append((CEPD[i]*100))
    plt.xlabel("Year")

    plt.ylabel("CEPD")

    plt.show()


if __name__ =="__main__":

    main(sys.argv)       