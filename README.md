## Interdisciplinary Digital Entrepreneurship

This is our group page for the course Interdisciplinary Digital Entrepreneurship at the Aarhus University (2020/21). 

### Group

- Jana Puschmann
- Filip Kubos
- Dominykas Rumsa


### Experiments


| Hypothesis        | Experiment           | Difficulty  |  Result |
| ----------------- |:--------------------|:-----------:| ------- |
| People consume more water during the weekends than during the week | Analyse data | easy | Data set with annotated weekday and week number which can be used to plot each week for a certain attribute |
| People consume more water during public holidays than during weekdays | Analyse data | easy |         |
| People consume more water during the corona-related isolation time | Analyse data | easy | Starting from week 11 to week 16 (start of the lockdown) there was a sharp increase in water flow |
| People consume more water in the summer than in the winter time | Analyse data | easy | Significant increase in water consumption during summer |
| Some data attributes are more stable than others (some attributes fluctuate more than others) | Analyse data and contact aarhusvand for more information on the data attributes | intermediate |         |
| People consume more water on hot days than cold days | Analyse data and relate to weather data | intermediate |         |
| There are certain dates that can be linked to real-world events that influenced that water consumption [1]| Analyse data and find possible real-world connection | hard |         |

[1]: https://www.dst.dk/

#### Experiment 1 - Increase of water consumption on the weekend

The first experiment was meant to try to find out whether there would be a significant difference between the water consumption on the weekends compared to regular weekdays. The thought was that people generally are at home during the weekend which could lead to a higher consumption of water. 

The given data contains logs of certain attributes over two quarters (6 months). That data is logged for every minute, each day. This is too much data too visualize in an understanding way, so the first thing we did was to compute the mean value for every attribute each day. This leaves us with only one value per day instead of several thousand.

<img src="images/experiment1/annotations_z80.png">

We visualized the given data by aarhusvand by splitting it into weeks and plotting it for the available quarters Q1 and Q2. This approach is far from perfect and unfortunately the time for fine tuning this visualization was missing. However, we can already observe that there are some interesting details in the plots. It seems that there generally can be observed an increase from Saturday to Sunday in the data in both quarters. We are still unsure what the attributes in the data actually mean and need to contact aarhusvand to get some more insights on why we might observe an increase in this particular attribute. It is also important to mention that this is only 1 of 19 of the given attributes in the data set. We can also find an interesting outlier in the first quarter (s. brown line in q1) that is deviates a lot from the other weeks and a week that suddenly starts to decrease (s. purple line in q1) as well. Once we annotate the lines with the corresponding week numbers, it will be easy to have a closer look at outlying data like this.

<img src="images/experiment1/annotations_z105.png">

Even though that was not the goal of this experiment, we can see a slight increase in the overall values in both data sets when we compare Q2 to Q1. This might be an indication that warmer months do influence the water consumption somehow. To proof this, we would need to have a look at the other available attributes and get a better understanding about what they describe.

Overall, an overview like this could make it much easier for a data scientist to understand whether the current week deviates from the norm in certain attributes. This could be one of multiple views in a data visualization dashboard.

#### Experiment 2

#### Experiment 3

This experiment tries to give insights for water flow increase during lockdown period due to Covid-19. Lockdown in Denmark started on March 13th (week 11) and lasted approximately until June 8th (week 24) when phase 3 was introduced. This graph represents water flow data grouped by week for one of the available attributes in data set DIS.01_H_B96_BF1-M_FLOW_MID. It is clearly visible that starting from week 11 there is a sharp increase in water flow amount, thus confirming the initial hypothesis that water flow increase during lockdown period. However, further research needs to be carried out on the remaining data set and consultancy with domain experiments is required to fully confirm these claims.

<img src="images/experiment3/corona.png">

### Business model canvas

## Hypothesis

COST STRUCTURE
  Value driven - We trying to create the best product that brings the most value for the customer

REVENUE STREAMS
  Asset sale - We think that customers would buy the individual product for one time fee
  Subscribtion - We think that customers would pay a subscribtion fee for maintenance of the product

CHANNELS
  Digital - User are willing to use the digital platform that we provide

CUSTOMER SEGMENTS
  Customers or individuals with large amounts of data are willing to use our product for data analysis and procession

CUSTOMER RELATIONSHIPS
  Dedicated personal assitance - Customers want a product thats tailored according to their needs
  Self-service - Customer want to be provided with a manual (how-to) that they could use the product without additional assistance
  Automated services - Customers want to get automated reports to get insights on data

KEY RESOURCES
  Intellectual - Customer knowledge (domain knowledge) and database is required in order to carryout our research and provide insights or value
  Human - In order to create the product we need skilled employess in data sience and in the area of data visualization, communication, sales, management
  Financial - To start product development we need employess
  Physical - To keep our provided services accessible we need a data server and computing power

KEY ACTIVITIES
  Problem solving - Customer needs our expertise to bring the data into readable and interpretable format
KEY PARTNERS
  Strategic alliences - to reduces the business process costs we need to collaborate with cloud computing providers
VALUE PROPOSITIONS
  Getting the job done - We help the customer getting the job done by providing the visual analytic tool for their data
  Risk assesment - Customer gets the potential to forsee upcoming risks by using our tool
  Analytical and statistical inshights - customer gets the required imputs for making decisions
  Business process optimization - Customer spends less time and money for analysing the data

