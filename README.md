
Classification Project

Objectives

    Find the drivers for customer churn at Telco.

    Construct a model to predict customer churn using classifcation techniques.

    Document code, process (data acquistion, preparation, exploration and testing, modeling, and evaluating, and findings and key takeaways in a Jupyter Notebook report.

    Present a high-level notebook walkthrough targeted to your audience.

    Answer panel questions about your code, process, findings and key takeaways, and model.

Goals

    Find drivers for customer churn.

    Construct a ML classification model that accurately predicts customer churn.

    Create modules that make your process repeateable.

    Document your process well enough to be presented or read like a report.

Audience

    Your target audience for your notebook walkthrough is the Codeup Data Science team. This should guide your language and level of explanations in your walkthrough.

Project Specifications

Why are our customers churning?

Some questions to think about include but are not limited to:

    Are there clear groupings where a customer is more likely to churn?
        What if you consider contract type?
        Is there a tenure that month-to-month customers are most likely to churn? 1-year contract customers? 2-year contract customers?
        Do you have any thoughts on what could be going on? (Be sure to state these thoughts not as facts but as untested hypotheses. Unless you test them!). Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers).

    Are there features that indicate a higher propensity to churn?
        How influential are type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?

    Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point?
        If so, what is that point and for which service(s)?
        If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

Deliverables

You are expected to deliver the following:

    a Jupyter Notebook Report showing process and analysis with goal of finding drivers for customer churn. (This notebook should be commented and documented well enough to be read and walked through like a report.)

        We want to see the analysis you did to answer our questions and lead to your findings. Please clearly call out the questions and answers you are analyzing.

            For example: If you find that month-to-month customers churn more, we won't be surprised, but Telco is not getting rid of that plan. The fact that customers churn is not because they can; it's because they can and they are motivated to do so. We want your insights into why they are motivated to do so. We realize you will not be able to do a full causal experiment, but we would like to see some solid evidence of your conclusions.

    a README.md file containing project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), and key findings and takeaways from your project.

    a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn)

    individual modules, .py files, that hold your functions to acquire and prepare your data.

    a notebook walkthrough-style presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, and findings.

Detailed instructions for each stage of the pipeline are below.

In general, make sure you document your work. You don't need to explain what every line of code is doing, but you should explain what and why you are doing things.

    For example: If you drop a feature from the dataset, you should explain why you decided to do so, or why that is a reasonable thing to do. If you transform the data in a column, you should explain why you are making that transformation.

In addition, you should not present numers in isolation. If your code outputs a number, be sure you give some context to the number.
Project Planning

    Describe the project and goals.

    Task out how you will work through the pipeline in as much detail as you need to keep on track.

    Incluce a data dictionary.

    Clearly state your starting hypotheses (and add the testing of these to your task list).

Acquisition

In Your acquire.py

    Acquire data from the customers table from the telco_churn database on the codeup data science database server.

    You will want to join some tables as part of your query.

    This data should end up in a pandas data frame.

In Your Notebook - run acquire.py

    summarize data (.info(), .describe(), .value_counts(), ...)

    plot distributions of individual variables

Data Prep

In Your prepare.py

    Split your data into train/validate/test.

    Handle Missing Values.

    Handle erroneous data and/or outliers you wish to address.

    Encode variables as needed.

    Create a new feature that represents tenure in years.

    Create single variables for or find other methods to merge variables representing the information from the following columns:
        phone_service and multiple_lines
        dependents and partner
        streaming_tv & streaming_movies
        online_security & online_backup

In Your Notebook

Explore missing values and document takeaways/action plans for handling them.
- Should you remove the observations with a missing value for that variable? (remove row)

    Should you remove the variable altogether? (remove column)

    Is 'missing' equivalent to 0 (or some other constant value) in the specific case of this variable?

    Should you replace the missing values with a value it is most likely to represent, like mean/median/mode?

    Document your takeaways.

    Explore data types and adapt types or data values as needed to have numeric represenation of each attribute.

    Run prepare.py.

Data Exploration

In Your Notebook

Answer the key questions, your hypotheses, and figure out the drivers of churn. You are required to run at least 2 statistical tests in your data exploration. Make sure you document your hypotheses and set your alpha before running the tests and document your findings well.

    If a group is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts?

        Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers)

    Are there features that indicate a higher propensity to churn?

        For Example: type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.

    Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?

    If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

    Controlling for services (phone_id, internet_service_type_id, online_security_backup, device_protection, tech_support, and contract_type_id), is the mean monthly_charges of those who have churned significantly different from that of those who have not churned? (Use a t-test to answer this.)

    How much of monthly_charges can be explained by internet_service_type?
    Hint: correlation test - State your hypotheses and your conclusion clearly.

    How much of monthly_charges can be explained by internet_service_type + phone_service_type (0, 1, or multiple lines). State your hypotheses and your conclusion clearly.

    Create visualizations exploring the interactions of variables (independent with independent and independent with dependent). The goal is to identify features that are related to churn, identify any data integrity issues, understand 'how the data works'.

    For example: We may find that all who have online services also have device protection. In that case, we don't need both of those.

The visualizations done in your analysis for the questions above work toward answering the target question below.

    What can you say about each variable's relationship to churn, based on your initial exploration? If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.

Summarize your conclusions, provide clear answers to the specific questions, and summarize any takeaways/action plan from the work above.
Modeling and Evaluation

You are required to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.

In Your Notebook

    Feature Selection: Are there any variables that seem to provide limited to no additional information? If so, remove them.

    Train (fit, transform, evaluate) multiple different models, varying the model type and hyperparameters.

    Compare evaluation metrics across all the models, and select the ones you want to test using your validate dataframe.

    Based on how your evaluation of your models using the train and validate datasets, choose your best model that you will try with your test data.

    Test the final model (transform, evaluate) on your out-of-sample data (the testing data set). Summarize the performance. Interpret your results.

Draw Conclusions

    Summarize your findings.

    Key takeaways and next steps should be documented here.

