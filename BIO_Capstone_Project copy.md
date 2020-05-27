## Research Question

What is the effect of social distancing (**average** number of people met per day, incrementing from 0.0 to 8.0 by 0.05) on the projected length of COVID-19 epidemic according to the SIRD model (measured in days to end of epidemic)?

## Hypothesis

The projected length of the COVID-19 epidemic according to the SIRD model increases with the average number of people met per day. 

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

N=S(t)+I(t)+R(t) +D(t)

Rate of Change of S(t) = -¦ÂI

Rate of Change of I(t) = ¦ÂI - ¦ÃI -¦ÌI

Rate of Change of R(t) = ¦Ã I

Rate of Change of D(t) = ¦ÌI

¦Â = abS / (N - D) = (abS) / (N - D)

### Controlled Variables

N is the total population at the beginning of the pandemic. (US Population)

¦Ã is the recovery rate of this disease. ¦Ã = 1/D = 1/7.5 [Source of 7.5 day recovery](https://www.who.int/bulletin/online_first/20-255695.pdf)

¦Ì is the mortality rate of this disease. 0.0599 (mortality rate in all cases) / 40 (the data was collected over 40 days) = 0.0014975

a represents the probability a susceptible person is infected after close contact. [On average 6.6% of close contacts become infected](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30287-5/fulltext)

### Dependent Variable

The dependent variable is the projected length of the epidemic, measured in days. The epidemic is considered to be over when the Infectious population drops below 1000 persons. 1000 persons was chosen because of its relative insignificance to the US population.

### Mathematical Functions Explained

S(t) is the population size susceptible to the new disease at given time t measured in persons. The initial starting value is the current estimate of susceptible population. It changes each day according to the equations given above: each day, a certain percentage of the susceptible population gets infected by a member of the infectious population. 

I(t) is the population infectious with the new disease at given time t. This initial value is based on current extrapolation of the population that has been tested. Each day, it increases by the new susceptible people infected by the infectious population and decreases by the population that just died or got better that day. 

R(t) is the population recovered (and no longer susceptible) to the new disease at the given time t due to immunity.  [154000 recovered](https://www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide) Each day it increases by the new amount of newly recovered members of the infectious population. 

D(t) is the population no longer susceptible to the new disease at given time t due to death. This is the current reported death toll. Each day it increases by the new amount of newly deceased members of the infectious population.

## Methodology

The methodology is to use the constants and the independent variable to create estimations of the values for each day for each function. The resulting function values will be parsed for the dependent variable, the day the infectious population decreases below 1000 persons. 

A python script written in Python 3.8 using built-in libraries would be used to do the calculations stated above for different values of the independent variable and print the output in CSV format. A copy of the script can be found in the [Appendix 1](#appendix-1)



## Data Collected

#### Projected Length of Epidemic VS Average Number of People Met (Partial)

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | Avg. People Met/Day [Continued] | Predicted Length of Epidemic (Days) [Continued] |
| ----------------------- | --------------------------------------- | ------------------------------- | ----------------------------------------------- |
| 0.0                     | 48                                      | 0.15                            | 52                                              |
| 0.05                    | 49                                      | 0.2                             | 54                                              |
| 0.1                     | 51                                      |                                 |                                                 |

**\* The full data table can be found below in [Appendix 2](#appendix-2)**

## Graphs

<img title="" src="https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/Images/GraphedData.png" alt="" width="743">

## CER

**Claim 1:**

The length of the epidemic initially increases when the average number of persons met per day increases because it increases the chances for the virus to spread but not quickly enough to increase the immune population to slow its spread. 

**Evidence 1:**

The projected length of the pandemic is lowest when each member of the population meet less than 1 person on average per day. The projected length of the pandemic is the highest when each member of the population meet about 2.1 persons on average per day. 

**Reasoning 1:**

When people interact very little, the virus has very little chance to spread, thereby the infectious population quickly decreases below 1000 persons because little to no people are infected as the infectious recover. This matches with the data showing that the pandemic is projected to be over the quickest if everyone isolated themselves completely. However, as people meet about 2 other people per day, the virus is able to sustain the infectious population the longest as the newly infectious per day is closest to the number of people deceased or recovered per day initially. This allows the virus to last longer as it delays herd immunity in the country by the longest possible while maintaining a steady number of infectious people.  

**Claim 2:**

The projected length of the epidemic decreases when the avg. amount of people met per day increases above 2.1 persons because herd immunity occurs sooner. 

**Evidence 2:**

The projected length of the pandemic decreases as the amount of people met per day increase above 2.1 persons per day. 

**Reasoning 2:**

Because the increased contact between persons spreads the virus easier, a greater number of people become infected initially but recover and remain immune to the disease. Because of the initial outbreak infects more people, more people are rendered immune to the disease. This slows and eventually halts the spread of the virus, preventing the epidemic from lasting too long. However, this causes a sudden surge in projected infectious population and risks overwhelming hospitals, as well as exposing more people to the virus, increasing total projected deaths. 

## Strengths & Limitations

### Strength

1. It is a simplified model, allow users to make good projections without having to simulate the complex behaviors of a society. This allows the model to be faster and more lightweight. 

2. It can accurately predict effects of a new infectious disease in a large population. 

### Limitations

1. It doesn't account for births or deaths from other causes. 

2. It does not account for susceptibility differences in different age groups

3. It cannot model the unique behaviors of a community, which is an issue since the population does not mix homogeneously. 

4. It does not account for self-isolation and contact tracing. 

## Appendix 1

**Projected Length of Epidemic VS Average Number of People Met (Full)**

| **Avg. People Met/Day** | **Projected Length of Epidemic (Days)** | **Avg. People Met/Day** | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) |
| ----------------------- | --------------------------------------- | ----------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- |
| 0.0                     | 48                                      | 1.35                    | 147                     | 2.7                 | 364                     | 4.05                | 183                     | 5.4                 | 139                     | 6.75                | 120                     |
| 0.05                    | 49                                      | 1.4                     | 158                     | 2.75                | 348                     | 4.1                 | 180                     | 5.45                | 138                     | 6.8                 | 119                     |
| 0.1                     | 51                                      | 1.45                    | 171                     | 2.8                 | 334                     | 4.15                | 177                     | 5.5                 | 137                     | 6.85                | 119                     |
| 0.15                    | 52                                      | 1.5                     | 186                     | 2.85                | 320                     | 4.2                 | 175                     | 5.55                | 136                     | 6.9                 | 118                     |
| 0.2                     | 54                                      | 1.55                    | 203                     | 2.9                 | 309                     | 4.25                | 173                     | 5.6                 | 135                     | 6.95                | 118                     |
| 0.25                    | 55                                      | 1.6                     | 224                     | 2.95                | 298                     | 4.3                 | 171                     | 5.65                | 134                     | 7.0                 | 117                     |
| 0.3                     | 57                                      | 1.65                    | 250                     | 3.0                 | 288                     | 4.35                | 169                     | 5.7                 | 133                     | 7.05                | 117                     |
| 0.35                    | 59                                      | 1.7                     | 281                     | 3.05                | 279                     | 4.4                 | 167                     | 5.75                | 132                     | 7.1                 | 117                     |
| 0.4                     | 61                                      | 1.75                    | 320                     | 3.1                 | 270                     | 4.45                | 165                     | 5.8                 | 132                     | 7.15                | 116                     |
| 0.45                    | 63                                      | 1.8                     | 370                     | 3.15                | 262                     | 4.5                 | 163                     | 5.85                | 131                     | 7.2                 | 116                     |
| 0.5                     | 65                                      | 1.85                    | 432                     | 3.2                 | 255                     | 4.55                | 161                     | 5.9                 | 130                     | 7.25                | 115                     |
| 0.55                    | 67                                      | 1.9                     | 511                     | 3.25                | 249                     | 4.6                 | 159                     | 5.95                | 129                     | 7.3                 | 115                     |
| 0.6                     | 70                                      | 1.95                    | 604                     | 3.3                 | 242                     | 4.65                | 158                     | 6.0                 | 129                     | 7.35                | 115                     |
| 0.65                    | 72                                      | 2.0                     | 699                     | 3.35                | 237                     | 4.7                 | 156                     | 6.05                | 128                     | 7.4                 | 114                     |
| 0.7                     | 75                                      | 2.05                    | 767                     | 3.4                 | 231                     | 4.75                | 154                     | 6.1                 | 127                     | 7.45                | 114                     |
| 0.75                    | 78                                      | 2.1                     | 786                     | 3.45                | 226                     | 4.8                 | 153                     | 6.15                | 126                     | 7.5                 | 114                     |
| 0.8                     | 81                                      | 2.15                    | 759                     | 3.5                 | 221                     | 4.85                | 152                     | 6.2                 | 126                     | 7.55                | 113                     |
| 0.85                    | 85                                      | 2.2                     | 710                     | 3.55                | 217                     | 4.9                 | 150                     | 6.25                | 125                     | 7.6                 | 113                     |
| 0.9                     | 89                                      | 2.25                    | 655                     | 3.6                 | 212                     | 4.95                | 149                     | 6.3                 | 125                     | 7.65                | 113                     |
| 0.95                    | 93                                      | 2.3                     | 604                     | 3.65                | 208                     | 5.0                 | 148                     | 6.35                | 124                     | 7.7                 | 112                     |

| **Avg. People Met/Day** | Projected Length of Epidemic (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) | Avg. People Met/Day | Projected Length (Days) |
| ----------------------- | ----------------------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- | ------------------- | ----------------------- |
| 1.0                     | 97                                  | 2.35                | 557                     | 3.7                 | 204                     | 5.05                | 146                     | 6.4                 | 123                     | 7.75                | 112                     |
| 1.05                    | 102                                 | 2.4                 | 517                     | 3.75                | 201                     | 5.1                 | 145                     | 6.45                | 123                     | 7.8                 | 112                     |
| 1.1                     | 108                                 | 2.45                | 482                     | 3.8                 | 197                     | 5.15                | 144                     | 6.5                 | 122                     | 7.85                | 111                     |
| 1.15                    | 114                                 | 2.5                 | 452                     | 3.85                | 194                     | 5.2                 | 143                     | 6.55                | 122                     | 7.9                 | 111                     |
| 1.2                     | 121                                 | 2.55                | 426                     | 3.9                 | 191                     | 5.25                | 142                     | 6.6                 | 121                     | 7.95                | 111                     |
| 1.25                    | 128                                 | 2.6                 | 403                     | 3.95                | 188                     | 5.3                 | 141                     | 6.65                | 121                     | 8.0                 | 110                     |
| 1.3                     | 137                                 | 2.65                | 382                     | 4.0                 | 185                     | 5.35                | 140                     | 6.7                 | 120                     |                     |                         |
