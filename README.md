Insurance Premium Predictor App

The Insurance Premium Predictor is an interactive web application built with Python and Streamlit that predicts health insurance premiums based on user information. Using a machine learning model with 98% R² accuracy, this app helps users estimate insurance costs quickly and reliably.

Key Features

- Accurate Predictions: Powered by a high-performing Random Forest Regressor model.  
- User-Friendly Interface: Easy-to-use input form for personal and medical details.  
- Personalized Inputs: Includes Age, Gender, Number of Dependants, Marital Status, Income, and Medical History (9 categories).  
- Instant Results: Predicts estimated premium immediately after input.  
- Automated Data Processing: Handles categorical encoding and numerical scaling automatically.  

Technology Stack

- Python, Streamlit – Web app development  
- Scikit-learn – Model training and prediction  
- Pandas & NumPy – Data manipulation  
- Pickle – Model saving and loading  
- Seaborn & Matplotlib – Data visualization  

How It Works

1. Users input their personal and medical information.  
2. The app preprocesses the data using a trained pipeline.  
3. The Random Forest model predicts the expected insurance premium.  
4. Users receive an instant, reliable estimate(98% accurate).
