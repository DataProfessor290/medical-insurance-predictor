# 🏥 Medical Insurance Charges Predictor

A machine learning application that predicts medical insurance charges for individuals 
based on features such as age, BMI, smoking habits, and region.  
Built using Python (Scikit-learn, Pandas, NumPy) and Random Forest Regressor.  

📌 FEATURES
---------------------------------
- Cleaned and preprocessed dataset
- Outlier detection using IQR
- Encoded categorical variables
- Built ML pipelines for numeric & categorical data
- Trained multiple regression models
- Selected Random Forest as best model
- Evaluated with MSE, MAE, MAPE, R²
- Feature importance analysis

⚙️ TECH STACK
---------------------------------
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Streamlit (for deployment)

📊 DATASET COLUMNS
---------------------------------
age       -> Age of individual  
sex       -> Gender  
bmi       -> Body Mass Index  
children  -> Number of dependents  
smoker    -> Smoking status  
region    -> Residential region  
charges   -> Insurance charges (Target)  

🛠️ INSTALLATION & USAGE
---------------------------------
# Clone repository
git clone https://github.com/DataProfessor290/medical-insurance-predictor.git
cd medical-insurance-predictor

# Create virtual environment and install dependencies
pip install -r requirements.txt

# Run Jupyter Notebook
jupyter notebook

# OR run Streamlit app
streamlit run app.py

📈 MODEL TRAINING
---------------------------------
Models tested:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor (✅ BEST)

Evaluation Metrics:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- R² Score

🔑 FEATURE IMPORTANCE (Random Forest)
---------------------------------
1. Smoker  
2. BMI  
3. Age  
4. Children  
5. Region  
6. Sex  

📌 FUTURE IMPROVEMENTS
---------------------------------
- Deploy Streamlit app online  
- Hyperparameter tuning with GridSearchCV  
- Add SHAP/LIME for interpretability  

🤝 CONTRIBUTING
---------------------------------
Contributions, pull requests, and issues are welcome!  

👤 AUTHOR
---------------------------------
Tolulope Emuleomo (a.k.a Data Professor)  

- LinkedIn: https://www.linkedin.com/in/tolulope-emuleomo-77a231270/  
- GitHub:   https://github.com/DataProfessor290  
- X (Twitter): @DataProfessor_  
