# Dean Hickman
# December 9, 2022
# CS 152 
# Project 5: Simulating Elephant Population Management
# Run the program from the Terminal by entering "python3 elephant.py + [a number for the darting probability]""
"""This is the first of a two-part project where we&#39;ll be simulating the elephant population in Kruger National Park, South Africa. The carrying capacity of the park is approximately 7000 elephants (1 elephant per
square mile of park). Previous efforts to manage the population involved culling approximately 400 animals per year. After the development of an elephant contraceptive, the current effort to
manage the population involves using a contraceptive dart on adult female elephants to limit the birth rate."""
import random       #imports the random package
import sys          #imports the sys package 
#Parameters are defined below as the IDs

IDXcalv=0   #The calving interval
IDXdarted=1 #Percentage darted
IDXjuvAge= 2 #Age of a junville 
IDXmaxAge= 3 #The maximum age
IDXcalfProb= 4     #The Probability of calf survival
IDXadultProb= 5    #The Probability of adult survival
IDXseniorProb= 6   # The Probability of senior survival
IDXcapacity= 7     #Carrying capacity
IDXyears= 7        #Number of years 
#ID for elephants
IDXGender = 0                       #Gender of an elephant
IDXAge = 1                          #Age of an elephant
IDXMonthsPregnant = 2               #Pregnacy months
IDXMonthsContraceptiveRemaining = 3 #Months of contraceptive remaining

"""This function uses the newElephant function to create elephants and therefore give a number that will be the carrying capacity parameter."""
def initPopulation(parameters):
    population = []
    for i in range(parameters[IDXcapacity]):
        population.append(newElephant(parameters, (random.randint(1,parameters[IDXmaxAge]))))
        
    return(population)
"""This function randomly creates 15 elephants of varying age and gender and prints out each elephant list, it uses the random package to do so."""
def newElephant (parameters, age):
    
    probability = (1/parameters[IDXcalv])
    elephant = [0, 0, 0, 0]
    
    g = random.randint(0,1)
    if g == 0: 
        elephant[IDXGender] = "females"
    if g == 1: 
        elephant[IDXGender] = "males"
    elephant[IDXAge] = age
    if elephant[IDXGender] == "female":
        if age>parameters[IDXjuvAge] and age <=parameters[IDXmaxAge]:
            if random.random() < probability:
                elephant[IDXMonthsPregnant] = random.randint(1,22)
    return elephant
""" This function returns the population list after it increases the age of each elephant by 1."""
def incrementAge(parameters, population):
    age = parameters[IDXAge]
    for i in population:
        age = age+1


"""The function takes the parameter list and population list as arguments. The function uses the
parameters max age and the three survival probabilities (calf, adult, senior).
The function should loop over the existing population list and add each elephant to a new
population list if it survives, using the elephant&#39;s age to determine which probability to use to
determine survival. It should return the new population list. """
def calcSurvival(parameters, population):
    new_population= []
    for elephant in population:
        if (elephant[IDXAge] <= parameters[IDXjuvAge]):
            if random.random() < parameters[IDXcalfProb]:
                new_population.append(elephant)
        elif (elephant[IDXAge] <= parameters[IDXmaxAge]):
            if random.random() < parameters[IDXadultProb]:
                new_population.append(elephant)
        elif (elephant[IDXAge] <= parameters[IDXmaxAge]):
            if random.random() < parameters[IDXseniorProb]:
                new_population.append(elephant)
    return new_population 

"""This function, dartElephants, that goes through the adult females and randomly selects
individuals for darting based on the dart probability parameter. The function takes in the
parameter list and population list as arguments. It returns the population list."""
def dartElephants(parameters, population):
        for elephant in population:
            if elephant in population:
                if elephant [IDXGender] == "female":
                    if elephant[IDXAge]>= parameters[IDXjuvAge]:
                        if elephant[IDXAge] <= parameters[IDXmaxAge]:
                            if random.random() < parameters[IDXdarted]:
                                elephant[IDXMonthsPregnant] = 0
                                elephant[IDXMonthsContraceptiveRemaining] = 22
        return population
"""This function, cullElephants checks if there are more elephants than the carrying capacity. If there are too many
elephants, it should remove enough randomly chosen elephants from the population so there are as many elephants as the carrying capacity. Parameter and population list are arguements."""
def cullElephants (parameters, population):
    total = 0
    for i in range(0, len(population)):
        total = total+i
    Carryingcapacity = parameters[IDXcapacity]
    numCulled = (total- Carryingcapacity)
    if total >Carryingcapacity:
        newPop = random.shuffle(population)
    return (newPop, numCulled)

"""The function controlPopulation will determine whether the population should be darted or culled and call the appropriate function. Then it will return
the new population list and the number culled (which will be zero, if the elephants were darted) as a tuple."""

def controlPopulation(parameters, population):
    if parameters[IDXdarted] ==0:
        (newPopulation, culled) = cullElephants(parameters, population)
    else:
        newPopulation =dartElephants(parameters, population)
        culled = 0
        return(newPopulation, culled)

    
"""This function simulateMoth moves the simulation foward by one month. It modifies only the adult females in the population, and it adds a new calf to the population if one
should be born. The function takes in the parameter list and population list. It returns the population list."""
def simulateMonth(parameters, population):
    for elephant in population:
        gender = elephant[IDXGender]
        age = elephant[IDXAge]
        monthsPregnant = elephant[IDXMonthsPregnant]
        monthsContraceptive = elephant[IDXMonthsContraceptiveRemaining]
        if gender == "f" and (age > parameters[IDXjuvAge]) and (age < parameters[IDXmaxAge]):
            if monthsContraceptive > 0:
                elephant[IDXMonthsContraceptiveRemaining]= (elephant[IDXMonthsContraceptiveRemaining]-1)
            elif monthsPregnant > 0:
                if monthsPregnant >= 22:
                    age = 1
                    population.append(elephant)
                    elephant[IDXMonthsPregnant] = 0
                else:
                    elephant[IDXMonthsPregnant] = (elephant[IDXMonthsPregnant]+1)
            else:
                if parameters[IDXcalv] > (1.0 / (3.1*12 - 22)):
                    elephant[IDXMonthsPregnant] = 1 
"""The simulateYear function takes in the parameter list and population list. It calls calcSurvival, then it calss incrementAge, then it loops twelve times calling simulateMonth. Finally, it returns the population list."""
def  simulateYear(parameters, population):
    calcSurvival(parameters, population)
    incrementAge(parameters, population)
    for i in range(12):
        simulateMonth(parameters, population)

""" This function calculates the number of calves, juveniles, adult males, adult females, and seniors are in the population.
It returns a list with those values, the total, and the number culled. """
def calcResults(parameters, population, culled):
    calves = 0
    juveniles = 0
    adultmales = 0
    adultfemales = 0
    seniors = 0
    
    test=[]
    
    for elephant in population:
        if (elephant[IDXAge] <= parameters[IDXjuvAge]):
            calves = calves + 1
        if (elephant[IDXAge]==parameters[IDXjuvAge]):
            juveniles = juveniles + 1
        if (elephant[IDXAge]>parameters[IDXjuvAge]) and (elephant[IDXAge]<parameters[IDXmaxAge]):
            if elephant[IDXGender] == "males":
                adultfemales = adultmales+1
            if elephant[IDXGender] == "females":
                adultfemales = adultfemales+1
        if (elephant[IDXAge] >= parameters[IDXmaxAge]):
            seniors = seniors + 1
        
        total = calves+juveniles+adultfemales+adultmales+seniors
        
        test.append(total)
        test.append(calves)
        test.append(juveniles)
        test.append(adultmales)
        test.append(adultfemales)
        test.append(seniors)
        test.append(culled)
    return(test)
"""This function takes the parameter list and the number of year to run the simulation.  Then it creates the new population, applies controls,
loops of the number of years, simulatesthe year, and keeps track of the demographics for each year by appending them to a results list. """
def runSimulation(parameters, years):
    popsize = parameters[IDXcapacity]
    population = initPopulation( parameters )
    [population,culled] = controlPopulation( parameters, population )
    results = []
    for i in range(parameters[IDXyears]):
        population = simulateYear( parameters, population )
        [population,culled] = controlPopulation( parameters, population )
        results.append( calcResults( parameters, population, culled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 :
            print( 'Terminating early' )
            break
        
    return results 

def test():
    calv = 3.1
    darted = 0.0
    juvage = 12
    maxage = 60
    calfprob = 0.850
    adultprob = 0.996
    seniorprob = 0.200
    capacity = 10000
    years = 200
  
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity, years]
    print(parameters[IDXmaxAge])
   
    print(parameters)

    population = []
    for i in range(15):
        population.append( newElephant( parameters, random.randint(1, parameters[IDXmaxAge]) ) )

    for e in population:
        print(e)
    
    initPopulation(parameters)
    population = incrementAge(parameters, population)
    print(population)
"""This is the main function."""    
def main(argv):
    if (len(sys.argv)<1):
        print("enter the probability of darting")
    darted = int(sys.argv[1])
    calv = 3.1
    darted = 0.0
    juvAge = 12
    maxAge = 60
    calfProb = 0.850
    adultProb = 0.996
    seniorProb = 0.200
    capacity = 10000
    years = 200
    # make the parameter list out of the variables
    parameters = [calv, darted, juvAge, maxAge, calfProb, adultProb, seniorProb, capacity, years]
    results = []    
    results = runSimulation(parameters, years)
    print(results[-1])
   
    for i in range(years):
        for x in population:
            total = x+1
        print("Total population value in year ", i, ": total")
    
    avgtotal = (total/years)
    avgcalves = (calves/years)
    avgjuveniles = (juveniles/years)
    avgadultmales = (adultmales/years)
    avgadultfemales = (adultfemales/years)
    avgseniors = (seniors/years)
    
    print("Average total population value: ", avgtotal)
    print("Average number of calves: ", avgcalves)
    print("Average number of juveniles: ", avgjuveniles)
    print("Average number of adult males: ", avgadultmales)
    print("Average number of adult females: ", avgadultfemales)
    print("Average number of seniors: ", avgseniors)
    
if __name__ == "__main__":
    main(sys.argv)