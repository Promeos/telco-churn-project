# Telco™ Project
***
### Project Description
Accurately predict customer churn at a telecommunications company, Telco™, using a machine learning classification model.

Background
Telco™ is a telecommunications company that provides competitive internet and phone service packages. Customers have the option of signing a month-to-month, one-year, or two-year contract.

Business Problem
Telco™ wants to know why customers are churning.

Data Dictionary
|Attribute|Definition|
|:--|:---|
|payment\_type\_id|Numeric value (1-4)|
|contract\_type\_id|Numeric value (1-3|
|internet\_service\_type_id|Numeric value (1-3)|
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

### Table of Contents:
1. [Planning](#Planning)
2. [Acquisition](#Acquisition)
3. [Preparation](#Preparation)
4. [Exploration](#Exploration)
5. [Modeling](#Modeling)
6. [Evaluation](#Evaluation)

## Planning
---
 Goal(s)
 1. Find drivers of customer churn
 2. Accurately predict customer churn at Telco™
 
 Measure(s) of success
1. Hypothesis testing using statistical measures
    - Determine relationships of attributes
    - Test Hypothises
2. Establish Baseline accuracy
3. Create 3 classification models
    - Model performance: train, validate
        - Have at least 1 model that performs better than the baseline model 
    - Hyperparameter tuning
        - Use sklearns built in attributes to tune models
        - Select the best performing model to use on the test set
    - Model performance: test

Hypothesis Tests
1. Chi2 Test
Does a customer churn independent of whether they have dependents or a partner?
Does a customer churn independent of whether they have a month-to-month contract or other types of contracts
Does a customer churn independent of whether they have dsl or fiber optic internet?
Does a customer churn independent of whether they have streaming services?
Does a customer churn independent of whether they make automatic or manual payments?

2. T-Test - Two Sample, One-Tailed
Do customers who churn have a higher monthly charge than those who don't churn?
Do customers who churn pay more for phone services than those who don't churn?


 ## Acquisition
---
To analyze this data on your local machine you have several methods:

> Download a zip file of the repository [here](https://github.com/Promeos/telecom-churn-project/archive/master.zip)

> Clone this repository using:
>`git clone git@github.com:Promeos/telecom-churn-project.git`

To open the file in a jupyter notebook use following code:

>import pandas as pd
df = pd.read_csv('telco_data.csv')

Note: Be sure that you are in the same directory as the file or use an absolute path to retrieve the file

## Preparation and Processing
---
- [ ] Document process
- [ ] Create `prepare.py` file
    - [ ] Create functions to clean data
    - [ ] Store functions in a separate file, `prepare.py`
- [ ] Clean data
    - [ ] __tidy-data__ mindset
    - [ ] Change datatypes
        - [ ] Create encoded variables from categorical variables
    - [ ] Round numeric floating-point values
    
## Exploration
---
- [ ] Statistical Analysis
    - [ ] Restate hypothesis here
    - [ ] Test hypotheses
    - [ ] Plot distributions
- [ ] Create visuals
- [ ] Summarize key findings

Hypotheses

## Modeling
---
- [ ] Create 3 classification models

## Evaluation
---

- [ ] Summarize/Recap key findings
    - [ ] Drivers
    - [ ]