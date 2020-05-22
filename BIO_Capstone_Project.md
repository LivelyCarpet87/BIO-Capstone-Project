# BIO Capstone

## Research Question

What is the effect of social distancing (average number of people met per day) on the projected length of  (measured in days to end of epidemic) and on the total death toll?

---

## The Model

### Assumptions

1. Everyone untouched by the virus is initially susceptible.

2. People who recovered from the virus are immune to it forever. 

3. The population mixes homogeneously every day. 

4. Newborns and death from other causes can be ignored because of their relative significance. 

5. All members of the population are identical in likelihood of contracting, spreading, recovering from, or dying from the virus at any time of year. 

6. The system is assumed to be closed, meaning there is no influx or outflow of persons. 

### Mathematical Representation

The SIRD model can be represented by the following equations:

$N=S(t)+I(t)+R(t) +D(t)$

Rate of Change of S(t) = -βI

Rate of Change of I(t)$= βI - \gamma I -\mu I$

Rate of Change of R(t)$ = \gamma I$

Rate of Change of D(t)$ = \mu I$

$\beta = a \times$ <mark>$b$</mark> $\times \frac S{N - D} = \frac{abS}{N - D}$

### Independent Variables

$b$ is the number of people an infected person can contact each day. It is used to calculate $\beta$ and the other rates of change. 

### Controlled Variables

N is the total population at the beginning of the pandemic. (US Population)

$\gamma$ is the recovery rate of this disease. $\gamma = 1/D = 1/7.5$ [Source of 7.5 day recovery](https://www.who.int/bulletin/online_first/20-255695.pdf)

$\mu$ is the mortality rate of this disease.  0.0599 (mortality rate in all cases) / 40 (the data was collected over 40 days) = 0.0014975

$a$ represents the probability a susceptible person is infected after close contact. [On average 6.6% of close contacts become infected](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30287-5/fulltext)

### Dependent Variable

The dependent variable is length of time, measured in days, until the projected Infectious population drops below 1000 persons. 

### Mathematical Functions Explained

S(t) is the population size susceptible to the new disease at given time t measured in persons. The initial starting value is the current estimate of susceptible population. It changes each day according to the equations given above: each day, a certain percentage of the susceptible population gets infected by a member of the infectious population. 

I(t) is the population infectious with the new disease at given time t. This initial value is based on current extrapolation of the population that has been tested. Each day, it increases by the new susceptible people infected by the infectious population and decreases by the population that just died or got better that day. 

R(t) is the population recovered (and no longer susceptible) to the new disease at the given time t due to immunity.  [154000 recovered](https://www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide) Each day it increases by the new amount of newly recovered members of the infectious population. 

D(t) is the population no longer susceptible to the new disease at given time t due to death. This is the current reported death toll. Each day it increases by the new amount of newly deceased members of the infectious population.

---

## Methodology

The methodology is to use the constants and the independent variable to create estimations of the values for each day for each function. The resulting function values will be parsed for the dependent variable, the day the infectious population decreases below 1000 persons. 

A python script written in Python 3.8 using built-in libraries would be used to do the calculations stated above for different values of the independent variable and print the output in CSV format. A copy of the script can be found in the [Appendix 1](#appendix-1)

---

## Data Collected

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | **Observations**           |
| ----------------------- | --------------------------------------- | -------------------------- |
| 0.0                     | 48                                      | Herd Immunity Not Achieved |
| 0.05                    | 49                                      | Herd Immunity Not Achieved |
| 0.1                     | 51                                      | Herd Immunity Not Achieved |
| 0.15                    | 52                                      | Herd Immunity Not Achieved |
| 0.2                     | 54                                      | Herd Immunity Not Achieved |
| 0.25                    | 55                                      | Herd Immunity Not Achieved |
| 0.3                     | 57                                      | Herd Immunity Not Achieved |
| 0.35                    | 59                                      | Herd Immunity Not Achieved |
| 0.4                     | 61                                      | Herd Immunity Not Achieved |
| 0.45                    | 63                                      | Herd Immunity Not Achieved |
| 0.5                     | 65                                      | Herd Immunity Not Achieved |
| 0.55                    | 67                                      | Herd Immunity Not Achieved |
| 0.6                     | 70                                      | Herd Immunity Not Achieved |
| 0.65                    | 72                                      | Herd Immunity Not Achieved |
| 0.7                     | 75                                      | Herd Immunity Not Achieved |
| 0.75                    | 78                                      | Herd Immunity Not Achieved |
| 0.8                     | 81                                      | Herd Immunity Not Achieved |
| 0.85                    | 85                                      | Herd Immunity Not Achieved |
| 0.9                     | 89                                      | Herd Immunity Not Achieved |
| 0.95                    | 93                                      | Herd Immunity Not Achieved |
| 1.0                     | 97                                      | Herd Immunity Not Achieved |
| 1.05                    | 102                                     | Herd Immunity Not Achieved |
| 1.1                     | 108                                     | Herd Immunity Not Achieved |
| 1.15                    | 114                                     | Herd Immunity Not Achieved |
| 1.2                     | 121                                     | Herd Immunity Not Achieved |
| 1.25                    | 128                                     | Herd Immunity Not Achieved |
| 1.3                     | 137                                     | Herd Immunity Not Achieved |
| 1.35                    | 147                                     | Herd Immunity Not Achieved |
| 1.4                     | 158                                     | Herd Immunity Not Achieved |
| 1.45                    | 171                                     | Herd Immunity Not Achieved |
| 1.5                     | 186                                     | Herd Immunity Not Achieved |
| 1.55                    | 203                                     | Herd Immunity Not Achieved |
| 1.6                     | 224                                     | Herd Immunity Not Achieved |
| 1.65                    | 250                                     | Herd Immunity Not Achieved |
| 1.7                     | 281                                     | Herd Immunity Not Achieved |
| 1.75                    | 320                                     | Herd Immunity Not Achieved |
| 1.8                     | 370                                     | Herd Immunity Not Achieved |
| 1.85                    | 432                                     | Herd Immunity Not Achieved |
| 1.9                     | 511                                     | Herd Immunity Not Achieved |
| 1.95                    | 604                                     | Herd Immunity Not Achieved |
| 2.0                     | 699                                     | Herd Immunity Not Achieved |
| 2.05                    | 767                                     | Herd Immunity Not Achieved |
| 2.1                     | 786                                     | Herd Immunity Not Achieved |
| 2.15                    | 759                                     | Herd Immunity Not Achieved |
| 2.2                     | 710                                     | Herd Immunity Not Achieved |
| 2.25                    | 655                                     | Herd Immunity Not Achieved |
| 2.3                     | 604                                     | Herd Immunity Not Achieved |
| 2.35                    | 557                                     | Herd Immunity Not Achieved |
| 2.4                     | 517                                     | Herd Immunity Not Achieved |
| 2.45                    | 482                                     | Herd Immunity Not Achieved |
| 2.5                     | 452                                     | Herd Immunity Not Achieved |
| 2.55                    | 426                                     | Herd Immunity Not Achieved |
| 2.6                     | 403                                     | Herd Immunity Not Achieved |
| 2.65                    | 382                                     | Herd Immunity Not Achieved |
| 2.7                     | 364                                     | Herd Immunity Not Achieved |
| 2.75                    | 348                                     | Herd Immunity Not Achieved |
| 2.8                     | 334                                     | Herd Immunity Not Achieved |
| 2.85                    | 320                                     | Herd Immunity Not Achieved |
| 2.9                     | 309                                     | Herd Immunity Not Achieved |
| 2.95                    | 298                                     | Herd Immunity Not Achieved |
| 3.0                     | 288                                     | Herd Immunity Not Achieved |
| 3.05                    | 279                                     | Herd Immunity Not Achieved |
| 3.1                     | 270                                     | Herd Immunity Not Achieved |
| 3.15                    | 262                                     | Herd Immunity Not Achieved |
| 3.2                     | 255                                     | Herd Immunity Not Achieved |
| 3.25                    | 249                                     | Herd Immunity Not Achieved |
| 3.3                     | 242                                     | Herd Immunity Not Achieved |
| 3.35                    | 237                                     | Herd Immunity Not Achieved |
| 3.4                     | 231                                     | Herd Immunity Not Achieved |
| 3.45                    | 226                                     | Herd Immunity Not Achieved |
| 3.5                     | 221                                     | Herd Immunity Not Achieved |
| 3.55                    | 217                                     | Herd Immunity Not Achieved |
| 3.6                     | 212                                     | Herd Immunity Not Achieved |
| 3.65                    | 208                                     | Herd Immunity Not Achieved |
| 3.7                     | 204                                     | Herd Immunity Not Achieved |
| 3.75                    | 201                                     | Herd Immunity Achieved     |
| 3.8                     | 197                                     | Herd Immunity Achieved     |
| 3.85                    | 194                                     | Herd Immunity Achieved     |
| 3.9                     | 191                                     | Herd Immunity Achieved     |
| 3.95                    | 188                                     | Herd Immunity Achieved     |
| 4.0                     | 185                                     | Herd Immunity Achieved     |
| 4.05                    | 183                                     | Herd Immunity Achieved     |
| 4.1                     | 180                                     | Herd Immunity Achieved     |
| 4.15                    | 177                                     | Herd Immunity Achieved     |
| 4.2                     | 175                                     | Herd Immunity Achieved     |
| 4.25                    | 173                                     | Herd Immunity Achieved     |
| 4.3                     | 171                                     | Herd Immunity Achieved     |
| 4.35                    | 169                                     | Herd Immunity Achieved     |
| 4.4                     | 167                                     | Herd Immunity Achieved     |
| 4.45                    | 165                                     | Herd Immunity Achieved     |
| 4.5                     | 163                                     | Herd Immunity Achieved     |
| 4.55                    | 161                                     | Herd Immunity Achieved     |
| 4.6                     | 159                                     | Herd Immunity Achieved     |
| 4.65                    | 158                                     | Herd Immunity Achieved     |
| 4.7                     | 156                                     | Herd Immunity Achieved     |
| 4.75                    | 154                                     | Herd Immunity Achieved     |
| 4.8                     | 153                                     | Herd Immunity Achieved     |
| 4.85                    | 152                                     | Herd Immunity Achieved     |
| 4.9                     | 150                                     | Herd Immunity Achieved     |
| 4.95                    | 149                                     | Herd Immunity Achieved     |
| 5.0                     | 148                                     | Herd Immunity Achieved     |
| 5.05                    | 146                                     | Herd Immunity Achieved     |
| 5.1                     | 145                                     | Herd Immunity Achieved     |
| 5.15                    | 144                                     | Herd Immunity Achieved     |
| 5.2                     | 143                                     | Herd Immunity Achieved     |
| 5.25                    | 142                                     | Herd Immunity Achieved     |
| 5.3                     | 141                                     | Herd Immunity Achieved     |
| 5.35                    | 140                                     | Herd Immunity Achieved     |
| 5.4                     | 139                                     | Herd Immunity Achieved     |
| 5.45                    | 138                                     | Herd Immunity Achieved     |
| 5.5                     | 137                                     | Herd Immunity Achieved     |
| 5.55                    | 136                                     | Herd Immunity Achieved     |
| 5.6                     | 135                                     | Herd Immunity Achieved     |
| 5.65                    | 134                                     | Herd Immunity Achieved     |
| 5.7                     | 133                                     | Herd Immunity Achieved     |
| 5.75                    | 132                                     | Herd Immunity Achieved     |
| 5.8                     | 132                                     | Herd Immunity Achieved     |
| 5.85                    | 131                                     | Herd Immunity Achieved     |
| 5.9                     | 130                                     | Herd Immunity Achieved     |
| 5.95                    | 129                                     | Herd Immunity Achieved     |
| 6.0                     | 129                                     | Herd Immunity Achieved     |
| 6.05                    | 128                                     | Herd Immunity Achieved     |
| 6.1                     | 127                                     | Herd Immunity Achieved     |
| 6.15                    | 126                                     | Herd Immunity Achieved     |
| 6.2                     | 126                                     | Herd Immunity Achieved     |
| 6.25                    | 125                                     | Herd Immunity Achieved     |
| 6.3                     | 125                                     | Herd Immunity Achieved     |
| 6.35                    | 124                                     | Herd Immunity Achieved     |
| 6.4                     | 123                                     | Herd Immunity Achieved     |
| 6.45                    | 123                                     | Herd Immunity Achieved     |
| 6.5                     | 122                                     | Herd Immunity Achieved     |
| 6.55                    | 122                                     | Herd Immunity Achieved     |
| 6.6                     | 121                                     | Herd Immunity Achieved     |
| 6.65                    | 121                                     | Herd Immunity Achieved     |
| 6.7                     | 120                                     | Herd Immunity Achieved     |
| 6.75                    | 120                                     | Herd Immunity Achieved     |
| 6.8                     | 119                                     | Herd Immunity Achieved     |
| 6.85                    | 119                                     | Herd Immunity Achieved     |
| 6.9                     | 118                                     | Herd Immunity Achieved     |
| 6.95                    | 118                                     | Herd Immunity Achieved     |
| 7.0                     | 117                                     | Herd Immunity Achieved     |
| 7.05                    | 117                                     | Herd Immunity Achieved     |
| 7.1                     | 117                                     | Herd Immunity Achieved     |
| 7.15                    | 116                                     | Herd Immunity Achieved     |
| 7.2                     | 116                                     | Herd Immunity Achieved     |
| 7.25                    | 115                                     | Herd Immunity Achieved     |
| 7.3                     | 115                                     | Herd Immunity Achieved     |
| 7.35                    | 115                                     | Herd Immunity Achieved     |
| 7.4                     | 114                                     | Herd Immunity Achieved     |
| 7.45                    | 114                                     | Herd Immunity Achieved     |
| 7.5                     | 114                                     | Herd Immunity Achieved     |
| 7.55                    | 113                                     | Herd Immunity Achieved     |
| 7.6                     | 113                                     | Herd Immunity Achieved     |
| 7.65                    | 113                                     | Herd Immunity Achieved     |
| 7.7                     | 112                                     | Herd Immunity Achieved     |
| 7.75                    | 112                                     | Herd Immunity Achieved     |
| 7.8                     | 112                                     | Herd Immunity Achieved     |
| 7.85                    | 111                                     | Herd Immunity Achieved     |
| 7.9                     | 111                                     | Herd Immunity Achieved     |
| 7.95                    | 111                                     | Herd Immunity Achieved     |
| 8.0                     | 110                                     | Herd Immunity Achieved     |

---

## Graphs

![](https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/Images/GraphedData.png)



---

## CER

**Claim 1:**

The length of the epidemic initially increases when the average number of persons met per day increases because it increases the chances for the virus to spread but not enough quickly enough to increase the immune population to to slow its spread. 

**Evidence 1:**

The projected length of the pandemic is lowest when we meet less than 1 person on average per day. The projected length of the pandemic is the highest when we meet about 2.1 persons on average per day. 

**Reasoning 1:**

When people interact very little, the virus has very little chance to spread, thereby the infectious population quickly decreases below 1000 persons because little to no people are infected as the infectious recover. This matches with the data showing that the pandemic is projected to be over the quickest if everyone isolated themselves completely. However, as people meet about 2 other people per day, the virus is able to sustain the infectious population the longest as the newly infectious per day is closest to the number of people deceased or recovered per day initially. This allows the virus to last longer as it delays herd immunity in the country by the longest possible while maintaining a steady number of infectious people.  



**Claim 2:**

The projected length of the epidemic decreases when the avg. amount of people met per day increases above 2.1 persons because herd immunity occurs sooner. 

**Evidence 2:**

The projected length of the pandemic decreases as the amount of people met per day increase above 2.1 persons per day. 

**Reasoning 2:**

Because the increased contact between persons spreads the virus easier, a greater number of people become infected initially but recover and remain immune to the disease. Because of the initial outbreak infects more people, more people are rendered immune to the disease. This slows and eventually halts the spread of the virus, preventing the epidemic from lasting too long. However, this causes a sudden surge in projected infectious population and risks overwhelming hospitals, as well as exposing more people to the virus, increasing total projected deaths. 

---

## Strengths & Limitations

### Strength

1. It is a simplified model, allow users to make good projections without having to simulate the complex behaviors of a society. This allows the model to be faster and more lightweight. 

2. It can accurately predict effects of a new infectious disease in a large population. 

### Limitations

1. It doesn't account for births or deaths from other causes. 

2. It does not account for susceptibility differences in different age groups

3. It cannot model the unique behaviors of a community, which is an issue since the population does not mix homogeneously. 

4. It does not account for self-isolation and contact tracing. 

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
                print(","+str(b_input) + ","+ str(days) + ",Herd Immunity Not Achieved" + 
+", about "+str(round(Deceased[len(Deceased)-1]/float(24280000)*100,4)) + "% the Shanghai population died")
                break
            #print( str(float(b_input)) + "," + str(days) + ","+ str(round(Deceased[len(Deceased)-1],0)) )
            else:
                print(","+str(b_input) + ","+ str(days) + ",Herd Immunity Achieved"  
+", about "+str(round(Deceased[len(Deceased)-1]/float(24280000)*100,4)) + "% the Shanghai population died")
                break

#print the contact/day, total days until infection ends, maximum infectious population, deceased population increase in CSV format

#simulate contact/day from 0 to 500 per day
for i in range(0,161):
    sim(float(i)/20,N,initialInfectious,initialRecovered,gamma,mu,a)
```
