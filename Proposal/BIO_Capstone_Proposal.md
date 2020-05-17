# BIO Capstone

Effects of different degrees of social distancing on the peak value of the I(t) curve in the SIRD model. 

## The Model

### Mathematical Representation

The SIRD model can be represented by the following equations:

$N=S(t)+I(t)+R(t) +D(t)$

$\frac{dS}{dt} = -βI$

$\frac{dI}{dt} = βI - \gamma I -\mu I$

$\frac{dR}{dt} = \gamma I$

$\frac{dD}{dt} = \mu I$

$\beta = a \times b \times \frac S{N - D} = \frac{abS}{N - D}$

### Independent Variables

$b$ is the number of people an infected person can contact each day. 

### Controlled Variables

N is the total population at the beginning of the pandemic. (World population)

$\gamma$ is the recovery rate of this disease. $\gamma = 1/D = 1/7.5$ [Source of 7.5 day recovery](https://www.who.int/bulletin/online_first/20-255695.pdf)

$\mu$ is the mortality rate of this disease.  [5.3%](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7074479/)

$a$ represents the probability a susceptible person is infected after close contact. [on average 7% of close contacts becoming infected](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30287-5/fulltext)

### Dependent Variable

The dependent variable is the peak of I(t).

### Mathematical Functions Explained

S(t) is the population susceptible to the new disease at given time t. The initial value is the current estimates of susceptible population. 

I(t) is the population infectious with the new disease at given time t. This initial value is based on current extrapolation of the population that has been tested. 

R(t) is the population no longer susceptible to the new disease at given time t due to immunity.  [154000 recovered](https://www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide)

D(t) is the population no longer susceptible to the new disease at given time t due to death. This is the current reported death toll.  

---

## Methodology

The methodology is to use the constants and the independent variable to estimate the separate functions. The functions will be estimated using Euler's method with an interval of 1 (day). The resulting function graph will be used to find the dependent variable. 

A python script written in Python 3.8 would be used to do the calculations above for different values of the independent variable and print the output in CSV format. A copy of the script can be found in the [Appendix 1](#appendix-1)



---



## Appendix 1

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
        beta = (a * b_input * Susceptible[len(Susceptible)-1] / (N - Deceased[len(Deceased)-1]) )
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
            print( str(b_input) + "," + str(days) + ","+ str(round(Deceased[len(Deceased)-1],0)) )
            break
        #print(Susceptible[len(Susceptible)-1],Infectious[len(Infectious)-1],Recovered[len(Recovered)-1],Deceased[len(Deceased)-1])

#print the contact/day, total days until infection ends, maximum infectious population, deceased population increase in CSV format


#simulate contact/day from 0 to 500 per day

for i in range(0,51):
    sim(i,N,initialInfectious,initialRecovered,gamma,mu,a)

```
