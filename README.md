# LeanPlum User Purchase Prediction

Team: Xinran(Grace) Zhang, Masha Vasilenko, Nan Lin

## Objective:

The object of this project is to predict probability of user purchase in 7 days and 14 days separately. The metric we are trying to optimize is AUC score considering the purchase label is imbalanced and rare.

## Data Overview
We were given following dataset by [LeanPlum](https://www.google.com/search?q=LeanPlum&rlz=1C5CHFA_enUS812US813&oq=LeanPlum&aqs=chrome..69i57j69i61j69i60l2j0l2.1355j0j7&sourceid=chrome&ie=UTF-8) ,a leading mobile marketing company:

- Sessions

Sessions data set provides information about the past sessions from October 1, 2018 to December 14, 2018. There are 6,239,836 observations. The table contains information about the user’s location where the session was originated; duration of past sessions; the OS of device on which the session was originated; whether the session was the first for a particular user and whether the user is a developer or not.

- Events:

Events data are provided for date from October 1, 2018 to December 14, 2018. There are 111,945,519 observations with 5 columns in the Events data. Specifically, the data contains events information for 620,988 distinct users and 620,988 of them have made one or more purchases.

- Attributes:

Contains information about users’ attributes (characteristics)

- Messages:

Provides metadata about the messages that were sent to a user: the time, delivery time, that triggered the message and what was the ultimate goal of the message.

## Results

We achieved AUC score of 0.996 for new test data by iterative feature engineering, model parameter tunning and ensemble modeling

## Our approach

 1. Generate Labels at user level
 
First divide dataset into two parts to generate labels separately: 
data from Dec 1, 2018 ~ Dec 7, 2018 and Dec 1, 2018 ~ Dec 14, 2018 to get labels for training data
Later we excluded these data and used data before Dec 1, 2018 to generate features for the training data

 2. Training and validation data split
 
Split Training data into training and validation set by stratified sampling

 3. Modeling
 
We built two models for 7-day and 14-day prediction and used two different sets of features.We tried Logistic Regression(baseline model), Random Forests, and Light GBM. To tuning parameters, we applied random search for critical paramters for these models.

 4. Iterate, iterate, iterate
 
One challenge of this problem is, we don't have any extra information about relative feature importance. We tried exploring feature importance using tree based models and revisited feature engineering iteratively. Based on validation AUC, we finalized the feature sets.

 5. Ensemble to boost the result
 
A soft voting ensemble model was built to boost the result of a single model and overcome overfitting.





