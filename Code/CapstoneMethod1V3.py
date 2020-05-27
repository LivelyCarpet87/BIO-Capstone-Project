import array

 #total population
N = 328200000
#initial Infectious population
initialInfectious = 1470000-260000-88199
#initial Recovered population
initialRecovered = 260000
#Probability at which people recover each day. Symptoms end on average after 7.5 days with a (1 - 5.3%) chance of recovery
gamma = 1/7.5
#Probability at which people die each day. Symptoms end on average after 7.5 days with a 5.3% chance of death
mu = 0.0599/40
#Probability person gets infected after close contact
a = 0.066

HIT=0.74

def sim(b_input,N,initialInfectious,initialRecovered,gamma,mu,a):
    Susceptible = array.array('d', [N-initialInfectious-initialRecovered]) #Initial Population of succeptible persons
    Infectious = array.array('d', [initialInfectious])
    Recovered = array.array('d', [initialRecovered])
    Deceased = array.array('d', [0])
    days=0
#    if b_input != 0:
#        R0=a*b_input*14
#        HIT=1-1/float(R0)
#    else:
#        HIT=0
    #simulate a day of interactions if the count of Infectious population >= 1
    for i in range(1,36500):
        #calculate changes in each population
        beta = float(a * b_input * Susceptible[len(Susceptible)-1]) / (N - Deceased[len(Deceased)-1])
        newSusceptible = Susceptible[len(Susceptible)-1] - round(beta * Infectious[len(Infectious)-1])
        newRemoved = round(gamma * Infectious[len(Infectious)-1]) + round(mu * Infectious[len(Infectious)-1])
        newInfectious = Infectious[len(Infectious)-1] + round(beta * Infectious[len(Infectious)-1]) - newRemoved
        newRecovered = Recovered[len(Recovered)-1] + round(gamma * Infectious[len(Infectious)-1])
        newDeceased = Deceased[len(Deceased)-1] + round(mu * Infectious[len(Infectious)-1])



        #record resulting statistic of each population of that day
        Susceptible.append(newSusceptible)
        Infectious.append(newInfectious)
        Recovered.append(newRecovered)
        Deceased.append(newDeceased)
        if(Infectious[len(Infectious)-1] > 1000):
        #if(newInfectious > 100) and (Recovered[len(Recovered)-1]<=HIT*N):
            days=days+ 1
        else:
            if (Recovered[len(Recovered)-1]<=HIT*N):
                print(","+str(b_input) + ","+ str(days) + ",Herd Immunity For Activity Without Distancing Not Achieved")
                break
            #print( str(float(b_input)) + "," + str(days) + ","+ str(round(Deceased[len(Deceased)-1],0)) )
            else:
                print(","+str(b_input) + ","+ str(days) + ",Herd Immunity For Activity Without Distancing Achieved")
                break
        #print(Susceptible[len(Susceptible)-1],Infectious[len(Infectious)-1],Recovered[len(Recovered)-1],Deceased[len(Deceased)-1])

#print the contact/day, total days until infection ends, maximum infectious population, deceased population increase in CSV format

sim(7,N,initialInfectious,initialRecovered,gamma,mu,a)
#simulate contact/day from 0 to 500 per day
for i in range(0,161):
    sim(float(i)/20,N,initialInfectious,initialRecovered,gamma,mu,a)
