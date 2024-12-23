# SyriaTel Customer Churn Prediction
## BUSINESS UNDERSTANDING
Syriatel is a major telecommunications company in Syria. It offers a range of services, including mobile and fixed-line telephony, internet access, and data services. The company has a significant market share in Syria and plays a vital role in connecting people and businesses across the country.


However, due to the ongoing conflict in Syria, Syriatel's operations have been significantly impacted. The company has faced challenges such as infrastructure damage, power outages, and security threats. Despite these difficulties, Syriatel has continued to provide essential communication services to the Syrian people


Customer churn is a significant concern for telecommunications companies. It refers to the loss of customers over a specific period. This can be a costly problem, as acquiring new customers is often more expensive than retaining existing one

### PROBLEM STATEMENT

SyriaTel is a telecommunications company in Syria that aims to utize customer data to uncover patterns and predict the probability of customer churn, enabling the company to take steps to retain high_value customers and minimize value losses.


### OBJECTIVES

#### Main Objective
- Find a machine learning model for correct classification of Churn and non churn customers.

#### Secondary objectives
1. To analyze customer behavior patterns and identify key factors influencing churn decisions.
2. To identify which of the key factors that affect churn need to be given more attention or priority in order to reduce customer churn as soon as Possible. 
3. To evaluate the effectiveness of retention strategies and measure the impact on customer churn rate

### Metrics of success

Based on previous studies and research, the following are the measures that evaluate the success of models.
- Accuracy:80%
        total number of True positives(correctly identified instances)
  
- Precision:50%
        measures how predictive the model is in regard s to the number of true positives against false positives
  
- REcall:75%
        The ability of the model to identify churners correctly
  
- F1-Score: between 0.55 and o.65
        measures the accuracy of the predictive model's performance
  
- Area Under the Curve (AUC): The higher the AUC the more accurate the perfomance

## DATA UNDERSTANDING
The "bigml.csv" dataset has the following attributes:
 - It has 3333 rows and 21 columns
   
Here is a further explanation of the columns that we have:
1. state: The state where the customer resides.
2. account length: The number of months the customer has been with the telecommunications company.
3. area code: The area code of the customer's phone number.
4. phone number: The customer's phone number.
5. international plan: Whether the customer has an international plan.
6. voice mail plan: Whether the customer has a voicemail plan.
7. number vmail messages: The number of voicemail messages the customer has.
8. total day minutes: The total number of minutes1 used during the day.   
9. total day calls: The total number of calls made during the day.
10. total day charge: The total charge for day time usage.
11. total eve minutes: The total number of minutes used during the evening.
12. total eve calls: The total number of calls made during the evening.
13. total eve charge: The total charge for evening time usage.
14. total night minutes: The total number of minutes used during the night.
15. total night calls: The total number of calls made during the night.
16. total night charge: The total charge for night time usage.
17. total intl minutes: The total number of minutes used for international calls.
18. total intl calls: The total number of international calls made.
19. total intl charge: The total charge for international calls.
20. customer service calls: The number of calls made to customer service.
21. churn: Whether the customer has churned (left the company) or not.

We have four data types.
- Boolean, used in one column
- Integer, use in 8 columns
- Float, used in 8 columns
- object, used in 4 columns.
  
This shows that most of the columns have numerical data.

## DATA PREPARATION - Data Cleaning
In data preparation and analysis, here is a list of what we are required to do.
1.	check for missing values.
After checking for missing values, we realized that there were no columns with missing values. Therefore, we don’t have to worry about handling any.
2.	check for duplicate values.
After checking for duplicate values, we realized that there are no rows with duplicate values. Therefore, we also don’t have to worry about handling any duplicate values
3.	check for null values.
After checking for null values, we realize that there are no null values in our data
4.	check for outliers
I checked for outliers and realized most of the columns had outliers but with very small percentages. Since the small percentages could not make very significant changes, I decided to leave them as they were.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) is an important step that helps understand the data, identify patterns, detect anomalies, and uncover relationships between variables before applying any machine learning models.
EDA can be done in 3 important steps.
1. Exploring Univariate Analysis.
 This refers to analyzing one variable at a time to understand it’s distribution or It’s Key Characteristics.

2, Exploring Bivariate analysis
Analysing the relationship between two variables to explore potential correlations or dependencies

3. Exploring Multivariate analysis
  Analyses three or more variables simuteneously to uncover deeper relationships

 ## MODELING AND EVALUATING 
 ### Data Preprocessing
Data preprocessing is a crucial step in the data analysis and machine learning pipeline. It involves preparing raw data to ensure it is clean, consistent, and suitable for analysis or modeling. High-quality data preprocessing can significantly enhance model accuracy and reliability.
Key Steps in Data Preprocessing
1. Handling Multicolinearity
From the previous subtopic, we saw that the heat map showed multicolleniarity within our dataset. 
I went ahead and dropped the minutes columns because they were more or less the same or giving the same output as the charges columns.

2. Data Cleaning
I'm also going to drop state and account length columns because I'll not be using them
3. Encoding Categorical Data
Next, i'm going to do label encoding on the "international plan", "voice mail plan" and "churn" columns.
The following binary categorical variables are mapped to numbers (0 and 1):
•	international plan
•	voice mail plan
•	churn
I used mapping to label encode these columns

4. Feature Scaling
I  do have a clear imbalance in my target variable churn given majority of the customers are still with Syria Tel. Therefore if we had a model that always picked customers who did not churn (majority class) then we would expect an accuracy score of around 86%. This clas imbalance issue will be looked at as part of building the model.
I did normalization to balance the target variable “churn”
5. Splitting the Dataset
I then went ahead and identified the x and y variables to be used for modelling, and I split the dataset into train and test sets.

I built two classificatiom models, logistic regression and decision Trees.

for both of the two models, I followed the following steps:
1. Building the baseline model
2. Evaluating using the metrics of success
3. Tining the model using different methods
4. Evaluating the model again  to check if it has improved.
5. Evaluating all models against each other.

#### Decision Trees
A decision tree model is evaluated using the Scikit learn library and fit into the training data.

For my decision tree, I built a baseline model, evaluated it, and then I pruned the tree model using the max_depth value and min_samples_leaf value. I then evaluated the final model and these were my final results.

Pruned model Metrics:
- Accuracy: 0.9355322338830585
- Precision: 0.8295454545454546
- recall: 0.7227722772277227
- f1_score: 0.7724867724867724
From the evaluation metrics, the decision tree has a high accuracy score  and precision This is quite evident in the confusion matrix plot above as the number of false positives is quite low at 28 customers. In terms of recall, it's 72.27% , the accuracy is at  93.55%, the precision is at 82.95% and the AUC is 84.81%


#### Logistic Regression
Logistic Regression is a supervised machine learning algorithm used for binary classification problems. It predicts the probability of a target variable belonging to a particular class, where the target is binary (e.g., 0 or 1, Yes or No, True or False).

For my logistic evaluation, I built a baseline model and evaluated it. Then I balanced the target variable and evaluated the model with the balanced target variable,and evaluated the results.
After that I did Hyperparameter tuning which is regularization by reducing C to a small number. after that I evaluated the regularised model, and these were the final results.

Regularized Model:
- Accuracy: 0.769
- Precision: 0.36163522012578614
- recall: 0.8041958041958042
- f1_score: 0.49891540130151846
After increasing regularization, we see no difference in the AUC of the model. The metrics are the same as the model_with_weights, i.e. precision, recall, accuracy and F1 score have not increased or reduced.


## EVALUATION
model	       DTbase   DTprun	LRbase	LRbal	LRreg
Precision	0.725	0.829	0.574	0.361	0.361
Recall	        0.732	0.722	0.216	0.804	0.804
Accuracy	0.917	0.935	0.865	0.769	0.769
F1 score	0.729	0.772	0.315	0.499	0.499
AUC score	0.842	0.848	0.830	0.834	0.834

If we evaluate our models using our researched metrics of success:
• Accuracy:75% - 85% : Most of the models lied between this range, while others, especially from the deision tree models, surpassed the range.
• Precision:65% - 75% : The logistic regression models did not perform well with regards to our prediction metrics. Both models from the decision trees performed well
• REcall:70% - 80% : for recall, only the liner regression baseline model did not reach our predicted metrics, The other models lied between the range of our predicted metrics.
• F1-Score: between 0.55 and o.75 : The Decision Tree models performed well with regards to our predicted metrics of succes, but the Logistic Regression models did not.
• Area Under the Curve (AUC): All models increase their AUC but the pruned model from decision trees had the highest "AUC".

## RECOMMENDATIONS
1.	I would recommend Decision Trees as the best Machine Learning model to use when trying to predict customer churn for SyriaTel Company.
2.	The key factor influencing customer churn in SyriaTel Company is Total charges for calls, which greatly impacts the total minutes taken for calls I would recommend that day Call charges and international call charges to be reduced in order to reduce customer churn in SyriaTel.
3.	I would also recommend strategies like rewarding minuites and tokens that can be redeemed to encourage or "entice" their customers to use Syriatel and inrease the number of calls.


## CONCLUSIONS
This analysis on Syriatel was better achieved using the Decision Tree model. It helped us conclude that Syriatel company should consider reducing call charges and include incentives in order to reduce customer churn and attract more customers.


## NEXT STEPS

The model can now be deployed to the end-users, and it can also be use to predict future similar cases in future.
The project only used two modelling types to achieve it's goals. Other models should be considered just incase they are able to produce better results.
