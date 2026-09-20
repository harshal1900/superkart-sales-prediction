# Rubric

### 1. Data Overview and Exploratory Data Analysis
- **Points:** 6
- **Criteria:** 
  - Observations on the shape of data, data types of various attributes, missing values, duplicate values and statistical summary.
  - Univariate Analysis (boxplots, distribution plots for important variables)
  - Bivariate Analysis
  - Insights based on EDA

### 2. Data Preprocessing
- **Points:** 5
- **Criteria:** 
  - Feature engineering (provide rationale if not needed)
  - Outlier detection and treatment (provide rationale if treatment is not needed)
  - Prepare the data for analysis (Train and Test sets)
  - Define the preprocessing pipeline for encoding categorical features

### 3. Model Building
- **Points:** 7
- **Criteria:** 
  - Choose the metric of choice with proper rationale
  - Build any 2 ML models as a part of a pipeline with the data preprocessing steps
  - Comment on the performance of the models
  *Note: The ML models to be built can be any two out of Decision Tree, Bagging, Random Forest, AdaBoost, Gradient Boosting, and XGBoost*

### 4. Model Performance Improvement
- **Points:** 7
- **Criteria:** 
  - Hyperparameter Tuning: Use hyperparameter tuning to tune the models w.r.t. the metric of choice
  - Comment on the performance of the tuned models

### 5. Model Performance Comparison, Final Model Selection, and Serialization
- **Points:** 7
- **Criteria:** 
  - Compare the performances of all models built and choose the best model (with proper rationale)
  - Check the performance of the best model on the test set
  - Serialize the best model
  - Load the serialized model and make predictions on the test set

### 6. Deployment - Backend
- **Points:** 6
- **Criteria:** 
  - Define the Flask API
  - Define the dependencies
  - Define the Dockerfile

### 7. Deployment - Frontend
- **Points:** 10
- **Criteria:** 
  - Define the Streamlit app
  - Define the dependencies
  - Define the Dockerfile
  - Push backend and frontend files to the repository
  - Define the forwarded URL
  - Online inference: Single prediction
  - Batch inference

### 8. Actionable Insights and Recommendations
- **Points:** 4
- **Criteria:** 
  - Write down insights from the analysis conducted
  - Provide actionable business recommendations

### 9. Presentation/Notebook - Overall Quality
- **Points:** 8
- **Criteria (Low-Code):** 
  - Structure and flow
  - Crispness
  - Visual appeal
  - Conclusion and Business Recommendations
- **Criteria (Full-Code):** 
  - Structure and flow
  - Well commented code
  - Conclusion and Business Recommendations