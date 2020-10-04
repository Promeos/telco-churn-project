# Telco™ Project
***
### Description
Accurately predict customer churn at a telecommunications company, Telco™, using a machine learning classification model.

"Churn rate is the proportion of contractual customers or subscribers who leave a supplier during a given time period. It is a possible indicator of customer dissatisfaction, cheaper and/or better offers from the competition, more successful sales and/or marketing by the competition, or reasons having to do with the customer life cycle." [source](https://en.wikipedia.org/wiki/Churn_rate)

### Data Dictionary
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|payment\_type\_id | Indicates how a customer pays their bill each month | int64 |
|contract\_type\_id| Indicates which contract type a customer has | int64 |
|internet\_service\_type_id| Indicates what type of internet service a customer has | int64 |
|customer\_id|Alpha-numeric ID that identifies each customer| object |
gender|Gender of the customer| object |
senior_citizen|Indicates if the customer is 65 or older| int64 |
partner|If a customer is married| object | 
dependents|Indicates if a customer lives with dependents| object |
tenure|The length of a customers relationship with Telco™ measured in months|  int64 |
phone_service|If a customer has phone service| object |
multiple_lines|If a customer has multiple phone lines| object |
online_security|Indicates if a customer has online security add-on| object |
online_backup|Indicates if a customer has online backups add-on| object |
device_protection|Indicates if a customer has a protection plan for Telco™ devices| object |
tech_support|Indicates whether a customer has technical support add-on| object |
streaming_tv|Indicates if a customer uses internet to stream tv| object |
streaming_movies|Indicates if a customer uses internet to stream movies| object |
paperless_billing|Indicates if a customer is enrolled in paperless billing| object |
monthly_charges|The amount a customer pays each month for services with Telco™| object |
total_charges|The total amount a customer has paid for Telco™ services| object |
|internet\_service\_type|Indicates the type of internet service a customer has| object |
|contract_type|The type of contract a customer has| object |
|payment_type|How a customer pays their bill each month| object |

| Target | Definition | Data Type |
| ----- | ----- | ----- |
|churn|Indicates whether a customer has terminated service| object |

## Setup
---
1. Download a zip file of the repository [here](https://github.com/Promeos/telco-churn-project/archive/master.zip)

2. Clone this repository using:

```
$ git clone git@github.com:Promeos/telco-churn-project.git
```

To open the file in a jupyter notebook use following code:
``` python
import pandas as pd
df = pd.read_csv('telco_data.csv')
```
<div class='alert alert-block alert-info'> 
Be sure that you are in the same directory as the csv file or use an absolute path to retrieve it
</div>

## Requirements
---
- numpy >= 1.18.1
- pandas >= 1.1.2
- scipy >= 1.4.1
- sklearn >= 0.22.1
- matplotlib >= 3.3.1
- seaborn >= 0.11.0

## Acknowledgements
---
[Codeup](https://codeup.com/)
Codeup Data Science Instructors
Darden Cohort