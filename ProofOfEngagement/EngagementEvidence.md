# Github Commit History

<img src="https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/ProofOfEngagement/CommitHistory1.png" title="" alt="" width="728">

For reference, my account username is LivelyCarpet87 and I am the sole contributor to this repository. This is my repository and not a fork of other's work. 

# Versions of Code (Major)

Before you read the code, you can see minor changes and tests commented out in gray. The code takes in the hard coded input and calculates the results using the SIRD model. The result is printed out as Comma Separated Values, which can be pasted into Numbers or Excel. Alternatively, they can be saved into a .csv file by piping output, like this: `python3 capstoneV3.py > newData.csv`

## V1

It was unfortunately completely riddled with bugs and errors, so V2 was recreated from scratch and V1 deleted. 

## V2

```python
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
a = 0.03

def sim(b_input,N,initialInfectious,initialRecovered,gamma,mu,a):
    Susceptible = array.array('d', [N-initialInfectious-initialRecovered]) #Initial Population of succeptible persons
    Infectious = array.array('d', [initialInfectious])
    Recovered = array.array('d', [initialRecovered])
    Deceased = array.array('d', [0])
    days=0
    #simulate a day of interactions if the count of Infectious population >= 1
    for i in range (1,1460):
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
        if(Infectious[len(Infectious)-1]>1000):
            days=days+ 1
        else:
            #print( str(float(b_input)) + "," + str(days) + ","+ str(round(Deceased[len(Deceased)-1],0)) )
            print(str(days) + ","+ str(round(Deceased[len(Deceased)-1],0)) )
            break
        #print(Susceptible[len(Susceptible)-1],Infectious[len(Infectious)-1],Recovered[len(Recovered)-1],Deceased[len(Deceased)-1])

#print the contact/day, total days until infection ends, maximum infectious population, deceased population increase in CSV format


#simulate contact/day from 0 to 500 per day

for i in range(0,101):
    sim(float(i)/2,N,initialInfectious,initialRecovered,gamma,mu,a)

```

## V3

```python
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
```

# Screenshots of Execution

![](https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/ProofOfEngagement/TerminalOutput1.png)

![](https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/ProofOfEngagement/TerminalOutput2.png)

# Screenshots of errors

![](https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/ProofOfEngagement/PythonError.png)
