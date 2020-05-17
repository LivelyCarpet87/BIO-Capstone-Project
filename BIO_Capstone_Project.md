# BIO Capstone

## Research Question

What is the effect of social distancing (average count of people met per day) on the duration of the infection (measured in days to end of epidemic) and on the total death toll?

---

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

## Data Collected

|     | 7%  | 3%  |
| --- | --- | --- |

| Avg. People Met/Day | **Days** | **Deaths** | **Days** | **Deaths** |
| ------------------- | -------- | ---------- | -------- | ---------- |
| **0.0**             | 48       | 12448.0    | 48       | 12448.0    |
| **0.5**             | 66       | 16788.0    | 54       | 13997.0    |
| **1.0**             | 103      | 25724.0    | 63       | 15990.0    |
| **1.5**             | 220      | 54389.0    | 74       | 18639.0    |
| **2.0**             | 779      | 444470.0   | 89       | 22332.0    |
| **2.5**             | 382      | 1577075.0  | 112      | 27842.0    |
| **3.0**             | 258      | 2289605.0  | 150      | 36894.0    |
| **3.5**             | 204      | 2729829.0  | 220      | 54389.0    |
| **4.0**             | 173      | 3013699.0  | 391      | 100172.0   |
| **4.5**             | 154      | 3202930.0  | 764      | 296709.0   |
| **5.0**             | 141      | 3332200.0  | 631      | 799726.0   |
| **5.5**             | 131      | 3422121.0  | 452      | 1297268.0  |
| **6.0**             | 124      | 3485471.0  | 355      | 1702279.0  |
| **6.5**             | 118      | 3530482.0  | 297      | 2027285.0  |
| **7.0**             | 114      | 3562658.0  | 258      | 2289605.0  |
| **7.5**             | 111      | 3585732.0  | 230      | 2503147.0  |
| **8.0**             | 108      | 3602288.0  | 209      | 2678455.0  |
| **8.5**             | 106      | 3614147.0  | 193      | 2823482.0  |
| **9.0**             | 104      | 3622620.0  | 180      | 2944270.0  |
| **9.5**             | 103      | 3628656.0  | 170      | 3045499.0  |
| **10.0**            | 101      | 3632923.0  | 161      | 3130766.0  |
| **10.5**            | 100      | 3635919.0  | 154      | 3202930.0  |
| **11.0**            | 99       | 3638005.0  | 148      | 3264235.0  |
| **11.5**            | 99       | 3639443.0  | 142      | 3316519.0  |
| **12.0**            | 98       | 3640423.0  | 138      | 3361238.0  |
| **12.5**            | 98       | 3641083.0  | 133      | 3399593.0  |
| **13.0**            | 97       | 3641519.0  | 130      | 3432558.0  |
| **13.5**            | 97       | 3641803.0  | 127      | 3460963.0  |
| **14.0**            | 96       | 3641985.0  | 124      | 3485471.0  |
| **14.5**            | 96       | 3642097.0  | 121      | 3506633.0  |
| **15.0**            | 96       | 3642169.0  | 119      | 3524941.0  |
| **15.5**            | 96       | 3642214.0  | 117      | 3540797.0  |
| **16.0**            | 95       | 3642233.0  | 115      | 3554535.0  |
| **16.5**            | 95       | 3642244.0  | 114      | 3566447.0  |
| **17.0**            | 95       | 3642256.0  | 112      | 3576775.0  |
| **17.5**            | 95       | 3642260.0  | 111      | 3585732.0  |
| **18.0**            | 94       | 3642257.0  | 109      | 3593501.0  |
| **18.5**            | 94       | 3642256.0  | 108      | 3600244.0  |
| **19.0**            | 94       | 3642257.0  | 107      | 3606090.0  |
| **19.5**            | 94       | 3642257.0  | 106      | 3611153.0  |
| **20.0**            | 94       | 3642257.0  | 106      | 3615536.0  |
| **20.5**            | 94       | 3642259.0  | 105      | 3619340.0  |
| **21.0**            | 94       | 3642257.0  | 104      | 3622620.0  |
| **21.5**            | 94       | 3642261.0  | 103      | 3625469.0  |
| **22.0**            | 93       | 3642257.0  | 103      | 3627914.0  |
| **22.5**            | 93       | 3642260.0  | 102      | 3630030.0  |
| **23.0**            | 93       | 3642260.0  | 102      | 3631857.0  |
| **23.5**            | 93       | 3642260.0  | 101      | 3633420.0  |
| **24.0**            | 93       | 3642255.0  | 101      | 3634761.0  |
| **24.5**            | 93       | 3642263.0  | 100      | 3635919.0  |
| **25.0**            | 93       | 3642262.0  | 100      | 3636911.0  |

---

## Graphs

![](/Users/livelycarpet87/Library/Application%20Support/marktext/images/2020-05-18-02-53-03-image.png)

![](/Users/livelycarpet87/Library/Application%20Support/marktext/images/2020-05-18-02-53-16-image.png)

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
