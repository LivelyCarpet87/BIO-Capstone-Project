## Research Question

What is the effect of social distancing (**average** number of people met per day, incrementing from 0.0 to 8.0 by 0.05) on the projected length of COVID-19 epidemic according to the SIRD model (measured in days to end of epidemic)? The end of the epidemic is defined as when the infectious population size is below 1000 persons. 

## Hypothesis

The **projected length of the COVID-19 epidemic** according to the SIRD model increases with the **average number of people met per day**. 

## Background

The purpose of this lab is to use the SIRD model to model the current epidemic and its spread. The lab investigates how the spread of the virus is impacted by the average number of people each person meets each day. 

### The SIRD Model Explained

#### Assumptions

1. Everyone untouched by the virus is initially susceptible.

2. People who recovered from the virus are immune to it forever. 

3. The population mixes homogeneously every day. 

4. Newborns and death from other causes can be ignored because of their relative significance. 

5. All members of the population are identical in likelihood of contracting, spreading, recovering from, or dying from the virus at any time of year. 

6. The system is assumed to be closed, meaning there is no influx or outflow of persons. 

#### Mathematical Representation

The SIRD model can be represented by the following equations:

N=S(t)+I(t)+R(t) +D(t)

Rate of Change of S(t) = -$\beta$I

Rate of Change of I(t) = $\beta$I - $\gamma$I -$\mu$I

Rate of Change of R(t) = $\gamma$ I

Rate of Change of D(t) = $\mu$I

$\beta$ = abS / (N - D) = (abS) / (N - D)

## Controlled Variables

N is the total population at the beginning of the pandemic. US Population=328.2 million people

$\gamma$ is the recovery rate of this disease. ¦Ã = 1/D = 1/7.5 This is because the length of recovery is 7.5 days, so each day there is a 1/7.5 chance of recovery. [Source](https://www.who.int/bulletin/online_first/20-255695.pdf)

$\mu$ is the mortality rate of this disease. 0.0599 (mortality rate in all cases) / 40 (days) = 0.0014975 chance of dying per day. (Sourced from [Google COVID-19 data](https://www.google.com/search?q=covid+19+cases+usa) on May 3rd)

a represents the probability a susceptible person is infected after close contact. On average, 6.6% of close contacts are infected. [Source](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30287-5/fulltext)

## Dependent Variable

The dependent variable is the projected length of the epidemic, measured in days. The epidemic is considered to be over when the Infectious population drops below 1000 persons. 1000 persons was chosen because of its relative insignificance to the US population.

## Independent Variable

b is the average number of people an infected person can contact each day. It is used to calculate $\beta$ and the other rates of change. For the experiment, the average number of people met per day incremented from 0.00 to 8.00 by increments of 0.05.

### Mathematical Functions Explained

S(t) is the population size susceptible to the new disease at given time t measured in persons. The initial starting value is the current estimate of susceptible population. It changes each day according to the equations given above: each day, a certain percentage of the susceptible population gets infected by a member of the infectious population. 

I(t) is the population infectious with the new disease at given time t. This initial value is based on current extrapolation of the population that has been tested. Each day, it increases by the new susceptible people infected by the infectious population and decreases by the population that just died or got better that day. 

R(t) is the population recovered (and no longer susceptible) to the new disease at the given time t due to immunity.  [154000 recovered](https://www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide) Each day it increases by the new amount of newly recovered members of the infectious population. 

D(t) is the population no longer susceptible to the new disease at given time t due to death.  Each day it increases by the new amount of newly deceased members of the infectious population.

## Methodology

The methodology is to use the constants and the independent variable to create estimations of the values for each day for each function. The resulting function values will be parsed for the dependent variable, the day the infectious population decreases below 1000 persons. The independent variable, **average number** of people met per day, increments from 0.00 (persons/day) to 8.00 (persons/day) by increments of 0.05 (persons/day). 

A python script written in Python 3.8 using built-in libraries would be used to do the calculations stated above for different values of the independent variable and print the output in CSV format. A copy of the script can b~~e~~ found in the the repository. 

Steps to reproduce data:

1. Open the terminal app (to execute the following commands, paste them and hit enter)
   
   <img title="" src="https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/Images/Open%20Terminal.png" alt="" width="353">

2. Clone the repository `git clone https://github.com/LivelyCarpet87/BIO-Capstone-Project`

3. change directory to the Code folder `cd ./BIO-Capstone-Project/Code`

4. execute `python3 ./CapstoneMethod1V3.py` and the output should be similar to ([Link to code](https://github.com/LivelyCarpet87/BIO-Capstone-Project/blob/master/Code/CapstoneMethod1V3.py)):

<img title="" src="https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/Images/TerminalScreenshot.png" alt="" width="801">

## Data Collected

#### Projected Length of Epidemic VS Average Number of People Met (Partial)

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | Avg. People Met/Day [Continued] | Predicted Length of Epidemic (Days) [Continued] |
| ----------------------- | --------------------------------------- | ------------------------------- | ----------------------------------------------- |
| 0.0                     | 48                                      | 0.15                            | 52                                              |
| 0.05                    | 49                                      | 0.2                             | 54                                              |
| 0.1                     | 51                                      |                                 |                                                 |

**\* The full data table can be found below in [Appendix 1](#appendix-1)**

## Graphs

<img title="" src="https://raw.githubusercontent.com/LivelyCarpet87/BIO-Capstone-Project/master/Images/GraphedData.png" alt="" width="636">

## CER

**Claim:**

The length of the epidemic initially increases when the average number of persons met per day increases because it increases the chances for the virus to spread but not quickly enough to increase the immune population to slow its spread. The projected length of the epidemic decreases when the avg. amount of people met per day increases above 2.1 persons because herd immunity occurs sooner.

**Evidence 1:**

The projected length of the pandemic is lowest when each member of the population meet on average less than 1 person per day. The projected length of the pandemic is the highest when each member of the population meet about 2.1 persons on average per day. 

**Reasoning 1:**

When people interact very little, the virus has very little chance to spread, thereby the infectious population quickly decreases below 1000 persons because little to no people are infected as the infectious recover. This matches with the data showing that the pandemic is projected to be over the quickest if everyone isolated themselves completely. However, as people meet about 2 other people per day, the virus is able to sustain the infectious population the longest as the newly infectious per day is closest to the number of people deceased or recovered per day initially. This allows the virus to last longer as it delays herd immunity in the country by the longest possible while maintaining a steady number of infectious people.  

**Evidence 2:**

The projected length of the pandemic decreases as the amount of people met per day increase above 2.1 persons per day. 

**Reasoning 2:**

Because the increased contact between persons spreads the virus easier, a greater number of people become infected initially but recover and remain immune to the disease. Because of the initial outbreak infects more people, more people are rendered immune to the disease. This slows and eventually halts the spread of the virus, preventing the epidemic from lasting too long. However, this causes a sudden surge in projected infectious population and risks overwhelming hospitals, as well as exposing more people to the virus, increasing total projected deaths. 

## Strengths & Limitations

### Strength

1. It is a simplified model, allow users to make good projections without having to simulate the complex behaviors of a society. This allows the model to be faster and more lightweight. 

2. It can accurately predict effects of a new infectious disease in a large population. 

### Limitations

1. It doesn't account for births or deaths from causes other than COVID-19. Because of this, the susceptible population will always slowly increase, the real-world result should be longer than the projected length by the SIRD model. A possible improvement would be to change the model add new births to the susceptible population at a steady rate and remove those deceased (due to other causes) from the susceptible (${- \frac{S(t)}{N-D(t)}\times Deaths}$), infectious ($-\frac{I(t)}{N-D(t)}\times Deaths$), and recovered population ($-\frac{I(t)}{N-D(t)}\times Deaths$), and  add the deceased from other causes to the Deceased population. 

2. It cannot model the unique behaviors of a community, which is an issue since the population does not mix homogeneously as according to the assumptions. Because of this, the model likely predicts a value that would be greater than real life if different communities avoid other communities or its members during the epidemic. A possible improvement would be to create a rule based simulation of actual persons in a mock community. That way, population members can behave differently and better model the country. 

3. It does not account for self-isolation. Because of the model assumes every infectious person is infecting people and the population is mixing homogeneously, this causes the model's projected length of the epidemic to be longer than the real world value. A possible improvement would be to have an Infectious population that is quarantined as well as a infectious population. Thus, there is a chance the person gets quarantined and cannot infect others.

4. This model assumes permanent immunity from COVID-19 after recovery, which does not consider the possibility of reinfection after a longer period of time. Because of this, the projected length is shorter than the real-world value should epidemics last long enough for reinfection. A possible solution would be to model the population as individual persons rather than numbers, so that they could become reinfected after some time. 

5. It cannot account for multiple strains for the same virus. This limitation causes the predicted length to be shorter than the actual length of the epidemic if the virus overall becomes more infectious, or the predicted length could be longer than real life if the virus overall becomes less infectious. A possible solution is to rerun the model with different values of infectiousness. 

## Works Cited

Bi, Qifang, et al. ¡§Epidemiology and Transmission of COVID-19 in 391 Cases and 1286 of Their Close Contacts in Shenzhen, China: a Retrospective Cohort Study.¡¨ *The Lancet*, The Lancet, 2020, www.thelancet.com/pdfs/journals/laninf/PIIS1473-3099(20)30287-5.pdf.

¡§Cases Overview.¡¨ *Google Search*, Google, 3 May 2020, www.google.com/search?q=covid%2B19%2Bcases%2Busa.

Hamzah, Fairoza Amira Binti, et al. ¡§CoronaTracker: World-Wide COVID-19 Outbreak Data Analysis and Prediction Fairoza Amira Binti Hamzaha.¡¨ *CoronaTracker: World-Wide COVID-19 Outbreak Data Analysis and Prediction*, World Health Organization, 2020, www.who.int/bulletin/online_first/20-255695.pdf.

Horn, Austin. ¡§More Than 1 Million People Have Recovered From COVID-19 Worldwide.¡¨ *NPR*, NPR, 1 May 2020, www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide.

¡§U.S. and World Population Clock.¡¨ *Population Clock*, 3 May 2020, www.census.gov/popclock/.

## Appendix 1

**Projected Length of Epidemic VS Average Number of People Met (Full)**

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** |
| ----------------------- | --------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- |
| 0.0                     | 48                                      | 2.05                                | 767                                                 | 4.1                                 | 180                                                 | 6.15                                | 126                                                 |
| 0.05                    | 49                                      | 2.1                                 | 786                                                 | 4.15                                | 177                                                 | 6.2                                 | 126                                                 |
| 0.1                     | 51                                      | 2.15                                | 759                                                 | 4.2                                 | 175                                                 | 6.25                                | 125                                                 |
| 0.15                    | 52                                      | 2.2                                 | 710                                                 | 4.25                                | 173                                                 | 6.3                                 | 125                                                 |
| 0.2                     | 54                                      | 2.25                                | 655                                                 | 4.3                                 | 171                                                 | 6.35                                | 124                                                 |
| 0.25                    | 55                                      | 2.3                                 | 604                                                 | 4.35                                | 169                                                 | 6.4                                 | 123                                                 |
| 0.3                     | 57                                      | 2.35                                | 557                                                 | 4.4                                 | 167                                                 | 6.45                                | 123                                                 |
| 0.35                    | 59                                      | 2.4                                 | 517                                                 | 4.45                                | 165                                                 | 6.5                                 | 122                                                 |
| 0.4                     | 61                                      | 2.45                                | 482                                                 | 4.5                                 | 163                                                 | 6.55                                | 122                                                 |
| 0.45                    | 63                                      | 2.5                                 | 452                                                 | 4.55                                | 161                                                 | 6.6                                 | 121                                                 |
| 0.5                     | 65                                      | 2.55                                | 426                                                 | 4.6                                 | 159                                                 | 6.65                                | 121                                                 |
| 0.55                    | 67                                      | 2.6                                 | 403                                                 | 4.65                                | 158                                                 | 6.7                                 | 120                                                 |
| 0.6                     | 70                                      | 2.65                                | 382                                                 | 4.7                                 | 156                                                 | 6.75                                | 120                                                 |

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** |
| ----------------------- | --------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- |
| 0.65                    | 72                                      | 2.7                                 | 364                                                 | 4.75                                | 154                                                 | 6.8                                 | 119                                                 |
| 0.7                     | 75                                      | 2.75                                | 348                                                 | 4.8                                 | 153                                                 | 6.85                                | 119                                                 |
| 0.75                    | 78                                      | 2.8                                 | 334                                                 | 4.85                                | 152                                                 | 6.9                                 | 118                                                 |
| 0.8                     | 81                                      | 2.85                                | 320                                                 | 4.9                                 | 150                                                 | 6.95                                | 118                                                 |
| 0.85                    | 85                                      | 2.9                                 | 309                                                 | 4.95                                | 149                                                 | 7.0                                 | 117                                                 |
| 0.9                     | 89                                      | 2.95                                | 298                                                 | 5.0                                 | 148                                                 | 7.05                                | 117                                                 |
| 0.95                    | 93                                      | 3.0                                 | 288                                                 | 5.05                                | 146                                                 | 7.1                                 | 117                                                 |
| 1.0                     | 97                                      | 3.05                                | 279                                                 | 5.1                                 | 145                                                 | 7.15                                | 116                                                 |
| 1.05                    | 102                                     | 3.1                                 | 270                                                 | 5.15                                | 144                                                 | 7.2                                 | 116                                                 |
| 1.1                     | 108                                     | 3.15                                | 262                                                 | 5.2                                 | 143                                                 | 7.25                                | 115                                                 |
| 1.15                    | 114                                     | 3.2                                 | 255                                                 | 5.25                                | 142                                                 | 7.3                                 | 115                                                 |
| 1.2                     | 121                                     | 3.25                                | 249                                                 | 5.3                                 | 141                                                 | 7.35                                | 115                                                 |
| 1.25                    | 128                                     | 3.3                                 | 242                                                 | 5.35                                | 140                                                 | 7.4                                 | 114                                                 |
| 1.3                     | 137                                     | 3.35                                | 237                                                 | 5.4                                 | 139                                                 | 7.45                                | 114                                                 |
| 1.35                    | 147                                     | 3.4                                 | 231                                                 | 5.45                                | 138                                                 | 7.5                                 | 114                                                 |
| 1.4                     | 158                                     | 3.45                                | 226                                                 | 5.5                                 | 137                                                 | 7.55                                | 113                                                 |
| 1.45                    | 171                                     | 3.5                                 | 221                                                 | 5.55                                | 136                                                 | 7.6                                 | 113                                                 |
| 1.5                     | 186                                     | 3.55                                | 217                                                 | 5.6                                 | 135                                                 | 7.65                                | 113                                                 |
| 1.55                    | 203                                     | 3.6                                 | 212                                                 | 5.65                                | 134                                                 | 7.7                                 | 112                                                 |
| 1.6                     | 224                                     | 3.65                                | 208                                                 | 5.7                                 | 133                                                 | 7.75                                | 112                                                 |
| 1.65                    | 250                                     | 3.7                                 | 204                                                 | 5.75                                | 132                                                 | 7.8                                 | 112                                                 |
| 1.7                     | 281                                     | 3.75                                | 201                                                 | 5.8                                 | 132                                                 | 7.85                                | 111                                                 |
| 1.75                    | 320                                     | 3.8                                 | 197                                                 | 5.85                                | 131                                                 | 7.9                                 | 111                                                 |
| 1.8                     | 370                                     | 3.85                                | 194                                                 | 5.9                                 | 130                                                 | 7.95                                | 111                                                 |
| 1.85                    | 432                                     | 3.9                                 | 191                                                 | 5.95                                | 129                                                 | 8.0                                 | 110                                                 |
| 1.9                     | 511                                     | 3.95                                | 188                                                 | 6.0                                 | 129                                                 |                                     |                                                     |
| 1.95                    | 604                                     | 4.0                                 | 185                                                 | 6.05                                | 128                                                 |                                     |                                                     |
| 2.0                     | 699                                     | 4.05                                | 183                                                 | 6.1                                 | 127                                                 |                                     |                                                     |







**Qualitative Data: Reaching Herd Immunity Threshold (HIT) to End Social Distancing**

| HIT not reached                              | HIT reached                                  |
| -------------------------------------------- | -------------------------------------------- |
| Meeting on average 0.00-3.70 persons per day | Meeting on average 3.75-8.00 persons per day |
