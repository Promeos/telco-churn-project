# Telco™ Project
***
### Project Description
---
Accurately predict customer churn at a telecommunications company, Telco™, using a machine learning classification model.

Telco™ is a telecommunications company that provides competitive internet and phone service packages. Telco™ wants to know why customers are terminating service.

### Data Dictionary
---
| Attribute | Definition | Data Types|
| ----- | ----- | ----- |
|payment\_type\_id | Numeric value (1-4) |
|contract\_type\_id|Numeric value (1-3 |
|internet\_service\_type_id|Numeric value (1-3) |
|customer\_id|Alpha-numeric ID that identifies each customer
gender|Gender of the customer|
senior_citizen|Indicates if the customer is 65 or older|
partner|If a customer is married|
dependents|Indicates if a customer lives with dependents|
tenure|The length of a customers relationship with Telco™ measured in months|
phone_service|If a customer has phone service|
multiple_lines|If a customer has multiple phone lines|
online_security|Indicates if a customer has online security add-on|
online_backup|Indicates if a customer has online backups add-on|
device_protection|Indicates if a customer has a protection plan for Telco™ devices|
tech_support|Indicates whether a customer has technical support add-on|
streaming_tv|Indicates if a customer uses internet to stream tv|
streaming_movies|Indicates if a customer uses internet to stream movies|
paperless_billing|Indicates if a customer is enrolled in paperless billing|
monthly_charges|The amount a customer pays each month for services with Telco™|
total_charges|The total amount a customer has paid for Telco™ services|
|churn|Indicates whether a customer has terminated service|
|internet\_service\_type|Indicates the type of internet service a customer has|
|contract_type|The type of contract a customer has|
|payment_type|How a customer pays their bill each month|
---

## Setup
---
1. Download a zip file of the repository [here](https://github.com/Promeos/telco-churn-project/archive/master.zip)

2. Clone this repository using:
`git clone git@github.com:Promeos/telco-churn-project.git`

To open the file in a jupyter notebook use following code:
``` python
import pandas as pd
df = pd.read_csv('telco_data.csv')
```
<div class='alert alert-box alert-info'> 
Be sure that you are in the same directory as the csv file or use an absolute path to retrieve it
</div>

## Requirements
---
- 
- 
- 

## Usage
---
```
$ git clone git@github.com:Promeos/telco-churn-project.git
```
## Acknowledgements
---
```
- Codeup Data Science Team
- Darden Cohort
```