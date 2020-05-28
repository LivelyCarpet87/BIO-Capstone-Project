## Research Question

What is the effect of social distancing (**average** number of people met per day, incrementing from 0.0 to 10.0 by 0.05) on the projected length of COVID-19 epidemic according to the SIRD model (measured in days to end of epidemic)? The end of the epidemic is defined as when the infectious population size is below 1000 persons. 

## Hypothesis

The **projected length of the COVID-19 epidemic** according to the SIRD model increases with the **average number of people met per day**. 

## Background

### How COVID-19 Spreads

The COVID-19 infectious disease is caused by the SARS-CoV-2, spread primarily between close contact through droplets carrying the virus, produced when coughing, sneezing, or talking. Less frequently, the virus is spread by touching contaminated objects then touching one's face. 

### Goal

Currently, the projected length of the pandemic is uncertain:

> "Its going to be a matter of several weeks to a few months for sure. ... The duration depends on the effectiveness of the controls"
> 
> -- Dr. Anthony Fauci (ABC News on March 15^th^)

Because of the dynamic nature of the social distancing policies compounded with incomplete information, it is difficult to project the exact duration of the pandemic. This lab aims to explore one of the controls, social distancing, and its impact on the projected length using the SIRD model and real world values. 

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

### Mathematical Functions Explained

S(t) is the population size susceptible to the new disease at given time t measured in persons. The initial starting value is the current estimate of susceptible population. It changes each day according to the equations given above: each day, a certain percentage of the susceptible population gets infected by a member of the infectious population.

I(t) is the population infectious with the new disease at given time t. This initial value is based on current extrapolation of the population that has been tested. Each day, it increases by the new susceptible people infected by the infectious population and decreases by the population that just died or got better that day.

R(t) is the population recovered (and no longer susceptible) to the new disease at the given time t due to immunity. [154000 recovered](https://www.npr.org/sections/coronavirus-live-updates/2020/05/01/849065983/more-than-1-million-people-have-recovered-from-covid-19-worldwide) Each day it increases by the new amount of newly recovered members of the infectious population.

D(t) is the population no longer susceptible to the new disease at given time t due to death. Each day it increases by the new amount of newly deceased members of the infectious population.

## Controlled Variables

N is the total population at the beginning of the pandemic. US Population=328.2 million people

$\gamma$ is the recovery rate of this disease. ¦Ã = 1/D = 1/7.5 This is because the length of recovery is 7.5 days, so each day there is a 1/7.5 chance of recovery. [Source](https://www.who.int/bulletin/online_first/20-255695.pdf)

$\mu$ is the mortality rate of this disease. 0.0599 (mortality rate in all cases) / 40 (days) = 0.0014975 chance of dying per day. (Sourced from [Google COVID-19 data](https://www.google.com/search?q=covid+19+cases+usa) on May 3rd)

a represents the probability a susceptible person is infected after close contact. On average, 6.6% of close contacts are infected. [Source](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30287-5/fulltext)

## Dependent Variable

The dependent variable is the projected length of the epidemic, measured in days. The epidemic is considered to be over when the Infectious population drops below 1000 persons. 1000 persons was chosen because of its relative insignificance to the US population. 

## Independent Variable

b is the average number of people an infected person can contact each day. It is used to calculate $\beta$ and the other rates of change. For the experiment, the average number of people met per day incremented from 0.00 to 10.00 by increments of 0.05. On average, we meet about 22 persons per day (Meier), but because many guidelines prohibit gatherings of more than 10 people, the study only explores meeting to up to 10 people on average per day. 

## Methodology

The methodology is to use the constants and the independent variable to create estimations of the values for each day for each function. The resulting function values will be parsed for the dependent variable, the day the infectious population decreases below 1000 persons. The independent variable, **average number** of people met per day, increments from 0.00 (persons/day) to 10.00 (persons/day) by increments of 0.05 (persons/day). 

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

The projected length of the pandemic is lowest when each member of the population meet on average less than 1 person per day, at about 60 days. The projected length of the pandemic is the highest when each member of the population meet about 2.1 persons on average per day, with a peak of 780 days. 

**Reasoning 1:**

When people interact very little, the virus has very little chance to spread, thereby the infectious population quickly decreases below 1000 persons because little to no people are infected as the infectious recover. This matches with the data showing that the pandemic is projected to be over the quickest if everyone isolated themselves completely. However, as people meet about 2 other people per day, the virus is able to sustain the infectious population the longest as the newly infectious per day is closest to the number of people deceased or recovered per day initially. This allows the virus to last longer as it delays herd immunity in the country by the longest possible while maintaining a steady number of infectious people.  

**Evidence 2:**

The projected length of the pandemic decreases as the amount of people met per day increase above 2.1 persons per day, tending to about 110 days. 

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

Meier, Robert J. ¡°A Critical Analysis of Corona Related Data: What the More Reliable Data Can Imply for Western-Europe.¡± *Applied Sciences*, vol. 10, no. 10, 2020, p. 3398., doi:10.3390/app10103398.

"'Things will get worse before they get better': Dr. Anthony Fauci | ABC News" *YouTube,* uploaded by ABC News, 15 March 2020, https://www.youtube.com/watch?v=zkH2rLIeU7A

¡§U.S. and World Population Clock.¡¨ *Population Clock*, 3 May 2020, www.census.gov/popclock/.

## Appendix 1

**Projected Length of Epidemic VS Average Number of People Met (Full)**

| **Avg. People Met/Day** | **Predicted Length of Epidemic (Days)** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** | **Avg. People Met/Day [Continued]** | **Predicted Length of Epidemic (Days) [Continued]** |
| ----------------------- | --------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- |
| 0.0                     | 48                                      | 2.55                                | 426                                                 | 5.1                                 | 145                                                 | 7.65                                | 113                                                 |
| 0.05                    | 49                                      | 2.6                                 | 403                                                 | 5.15                                | 144                                                 | 7.7                                 | 112                                                 |
| 0.1                     | 51                                      | 2.65                                | 382                                                 | 5.2                                 | 143                                                 | 7.75                                | 112                                                 |
| 0.15                    | 52                                      | 2.7                                 | 364                                                 | 5.25                                | 142                                                 | 7.8                                 | 112                                                 |
| 0.2                     | 54                                      | 2.75                                | 348                                                 | 5.3                                 | 141                                                 | 7.85                                | 111                                                 |
| 0.25                    | 55                                      | 2.8                                 | 334                                                 | 5.35                                | 140                                                 | 7.9                                 | 111                                                 |
| 0.3                     | 57                                      | 2.85                                | 320                                                 | 5.4                                 | 139                                                 | 7.95                                | 111                                                 |
| 0.35                    | 59                                      | 2.9                                 | 309                                                 | 5.45                                | 138                                                 | 8.0                                 | 110                                                 |
| 0.4                     | 61                                      | 2.95                                | 298                                                 | 5.5                                 | 137                                                 | 8.05                                | 110                                                 |
| 0.45                    | 63                                      | 3.0                                 | 288                                                 | 5.55                                | 136                                                 | 8.1                                 | 110                                                 |
| 0.5                     | 65                                      | 3.05                                | 279                                                 | 5.6                                 | 135                                                 | 8.15                                | 110                                                 |
| 0.55                    | 67                                      | 3.1                                 | 270                                                 | 5.65                                | 134                                                 | 8.2                                 | 109                                                 |
| 0.6                     | 70                                      | 3.15                                | 262                                                 | 5.7                                 | 133                                                 | 8.25                                | 109                                                 |
| 0.65                    | 72                                      | 3.2                                 | 255                                                 | 5.75                                | 132                                                 | 8.3                                 | 109                                                 |
| 0.7                     | 75                                      | 3.25                                | 249                                                 | 5.8                                 | 132                                                 | 8.35                                | 109                                                 |
| 0.75                    | 78                                      | 3.3                                 | 242                                                 | 5.85                                | 131                                                 | 8.4                                 | 108                                                 |
| 0.8                     | 81                                      | 3.35                                | 237                                                 | 5.9                                 | 130                                                 | 8.45                                | 108                                                 |
| 0.85                    | 85                                      | 3.4                                 | 231                                                 | 5.95                                | 129                                                 | 8.5                                 | 108                                                 |
| 0.9                     | 89                                      | 3.45                                | 226                                                 | 6.0                                 | 129                                                 | 8.55                                | 108                                                 |
| 0.95                    | 93                                      | 3.5                                 | 221                                                 | 6.05                                | 128                                                 | 8.6                                 | 107                                                 |
| 1.0                     | 97                                      | 3.55                                | 217                                                 | 6.1                                 | 127                                                 | 8.65                                | 107                                                 |
| 1.05                    | 102                                     | 3.6                                 | 212                                                 | 6.15                                | 126                                                 | 8.7                                 | 107                                                 |
| 1.1                     | 108                                     | 3.65                                | 208                                                 | 6.2                                 | 126                                                 | 8.75                                | 107                                                 |
| 1.15                    | 114                                     | 3.7                                 | 204                                                 | 6.25                                | 125                                                 | 8.8                                 | 107                                                 |
| 1.2                     | 121                                     | 3.75                                | 201                                                 | 6.3                                 | 125                                                 | 8.85                                | 106                                                 |
| 1.25                    | 128                                     | 3.8                                 | 197                                                 | 6.35                                | 124                                                 | 8.9                                 | 106                                                 |
| 1.3                     | 137                                     | 3.85                                | 194                                                 | 6.4                                 | 123                                                 | 8.95                                | 106                                                 |
| 1.35                    | 147                                     | 3.9                                 | 191                                                 | 6.45                                | 123                                                 | 9.0                                 | 106                                                 |
| 1.4                     | 158                                     | 3.95                                | 188                                                 | 6.5                                 | 122                                                 | 9.05                                | 106                                                 |
| 1.45                    | 171                                     | 4.0                                 | 185                                                 | 6.55                                | 122                                                 | 9.1                                 | 106                                                 |
| 1.5                     | 186                                     | 4.05                                | 183                                                 | 6.6                                 | 121                                                 | 9.15                                | 105                                                 |
| 1.55                    | 203                                     | 4.1                                 | 180                                                 | 6.65                                | 121                                                 | 9.2                                 | 105                                                 |
| 1.6                     | 224                                     | 4.15                                | 177                                                 | 6.7                                 | 120                                                 | 9.25                                | 105                                                 |
| 1.65                    | 250                                     | 4.2                                 | 175                                                 | 6.75                                | 120                                                 | 9.3                                 | 105                                                 |
| 1.7                     | 281                                     | 4.25                                | 173                                                 | 6.8                                 | 119                                                 | 9.35                                | 105                                                 |
| 1.75                    | 320                                     | 4.3                                 | 171                                                 | 6.85                                | 119                                                 | 9.4                                 | 104                                                 |
| 1.8                     | 370                                     | 4.35                                | 169                                                 | 6.9                                 | 118                                                 | 9.45                                | 104                                                 |
| 1.85                    | 432                                     | 4.4                                 | 167                                                 | 6.95                                | 118                                                 | 9.5                                 | 104                                                 |
| 1.9                     | 511                                     | 4.45                                | 165                                                 | 7.0                                 | 117                                                 | 9.55                                | 104                                                 |
| 1.95                    | 604                                     | 4.5                                 | 163                                                 | 7.05                                | 117                                                 | 9.6                                 | 104                                                 |
| 2.0                     | 699                                     | 4.55                                | 161                                                 | 7.1                                 | 117                                                 | 9.65                                | 104                                                 |
| 2.05                    | 767                                     | 4.6                                 | 159                                                 | 7.15                                | 116                                                 | 9.7                                 | 104                                                 |
| 2.1                     | 786                                     | 4.65                                | 158                                                 | 7.2                                 | 116                                                 | 9.75                                | 103                                                 |
| 2.15                    | 759                                     | 4.7                                 | 156                                                 | 7.25                                | 115                                                 | 9.8                                 | 103                                                 |
| 2.2                     | 710                                     | 4.75                                | 154                                                 | 7.3                                 | 115                                                 | 9.85                                | 103                                                 |
| 2.25                    | 655                                     | 4.8                                 | 153                                                 | 7.35                                | 115                                                 | 9.9                                 | 103                                                 |
| 2.3                     | 604                                     | 4.85                                | 152                                                 | 7.4                                 | 114                                                 | 9.95                                | 103                                                 |
| 2.35                    | 557                                     | 4.9                                 | 150                                                 | 7.45                                | 114                                                 | 10.0                                | 103                                                 |
| 2.4                     | 517                                     | 4.95                                | 149                                                 | 7.5                                 | 114                                                 | <br>                                | <br>                                                |
| 2.45                    | 482                                     | 5.0                                 | 148                                                 | 7.55                                | 113                                                 | <br>                                | <br>                                                |
| 2.5                     | 452                                     | 5.05                                | 146                                                 | 7.6                                 | 113                                                 | <br>                                | <br>                                                |

**Qualitative Data: Reaching Herd Immunity Threshold (HIT) to End Social Distancing**

| HIT not reached                              | HIT reached                                   |
| -------------------------------------------- | --------------------------------------------- |
| Meeting on average 0.00-3.70 persons per day | Meeting on average 3.75-10.00 persons per day |
