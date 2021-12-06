# Final Project Data Mining CMPE255 : RealEstate Investment Prediction 

### Shivam Shrivastav - SJSU ID: 015275000
### Praveen Prabhakar Nayak - SJSU ID: 015258425 
### Kunjan Malik - SJSU ID: 015284230 
### Yadnyshree Savant - SJSU ID: 015284932 

## Real Estate Investment Prediction for the State of IOWA
Link to Project presentation video: https://drive.google.com/file/d/1XAf987auzgw_xonPzDLy2Tp8ErHut0zt/view?usp=sharing
## IOWA Housing Dataset
Main Dataset Link: https://docs.google.com/spreadsheets/d/17-rQAmHy_jwE_q6iGtpmWABW2Qjpengi0b5FfJgB3fc/edit?usp=sharing  
IOWA Dataset Link: https://drive.google.com/file/d/1P7yK2RzmLvVY9-avomTVvvNxLkPT_Pdl/view?usp=sharing    
Scrapped Dataset: https://drive.google.com/file/d/1frrCHBqil_eCGyCdHw1B7hHbCJn2DRkZ/view?usp=sharing


# COLAB LINKS
Main Colab: https://colab.research.google.com/drive/1aEYSn5zhoKjjRyBtsyUKsaKyICRR64MU?usp=sharing   
Scrapping Colab: https://colab.research.google.com/drive/12auv638GZARH6bjsiYzBLMtMOsqe2vFR#scrollTo=kbX2hSKHEfwH
# CRISP-DM
**1.Business understanding**:
Provide knowledge to an investor or buyers, whether to invest in a housing property or not. This decision has to be taken by considering various features such as, Selling Price of the property, Zestimate Price, Proximity Ranking to various Schools, Crime Rate in the area, Walk Score etc.

**2.Data understanding**:
Using IOWA Dataset. We have performed Data cleaning, data preparation and eliminated unwanted columns and considered only the required features such as, address, zip code, area, bedrooms, bathrooms, year built, price, zestimate, zestimate rent. Apart from this data, we scrapped several additional dataset from above-mentioned websites to enrich the initial dataset, amalgamate it and improve the feature set and visualization to deduce the best model.

**3.Data preparation**: How do we organize the data for modeling?
Calculate Feature importance, gini score.
Feature transformation: Transform features and add new features to dataset via amalgamations.
Data distribution
Dimensionality Reduction via PCA
Implement 3 amalgamations:
First dataset Enrichment
Second data Enrichment
Third data enrichment

**4.Modeling**: Implement different ML Algorithms to build models and refine data narrative. Modeling - Define a Golden cluster and use Fractal Clustering to find it based on the business case.
Apply various classifiers and regressors algorithms 
Classifier:
Nearest Neighbors,Linear SVM,RBF SVM,Decision Tree,Random Forest,Neural Net,AdaBoost,Naive Bayes,QDA
Regression:
GradientBoostingRegressor,RandomForestRegressor,LinearRegression,SVR,DecisionTreeRegressor,AdaBoostRegressor,GaussianProcessRegressor, LogisticRegressor

**5.Evaluation**: Compare relevant tasks in the same table
Interpret results of each algorithm.
Suggest Latent Variables or Latent Manifolds, add then to the features and see how prediction results change.
Use appropriate metrics for measuring models and compare them in a table: regression metrics and/or classification metrics (confusion matrix, F1 and R2 score).

**6.Deployment**:
Build a flask API to predict the investment property.


# Project Document
https://github.com/shivamishu/Data-Mining-Final-Project/blob/main/DM_project_doc_final.pdf

# Webapp
<img width="1792" alt="Screen Shot 2021-12-04 at 4 24 32 PM" src="https://user-images.githubusercontent.com/24988178/144729272-16751cec-bb55-4475-bab6-c8df0d241f64.png">


<img width="1792" alt="Screen Shot 2021-12-04 at 4 25 03 PM" src="https://user-images.githubusercontent.com/24988178/144729063-011e3d20-dbbf-4f04-910a-fb1633e8e6a5.png">
