import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data (same as model training)
df = pd.read_csv("newpropro.csv")
df.dropna(subset=['actual_productivity', 'targeted_productivity', 'department', 'team'], inplace=True)
df['wip'].fillna(df['wip'].median(), inplace=True)
df['quarter'].fillna(method='ffill', inplace=True)
df['day'].fillna(method='ffill', inplace=True)
df['date'].fillna(method='ffill', inplace=True)

le_dep = LabelEncoder()
le_quarter = LabelEncoder()
le_day = LabelEncoder()
df['department'] = le_dep.fit_transform(df['department'])
df['quarter'] = le_quarter.fit_transform(df['quarter'])
df['day'] = le_day.fit_transform(df['day'])

features = ['quarter', 'department', 'day', 'team', 'targeted_productivity',
            'smv', 'wip', 'over_time', 'incentive', 'idle_time',
            'idle_men', 'no_of_style_change', 'no_of_workers']
X = df[features]
y = df['actual_productivity']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Streamlit UI
st.title("Worker Productivity Prediction")

st.markdown("Enter the factory conditions to predict worker productivity:")

quarter = st.selectbox("Quarter", le_quarter.classes_)
department = st.selectbox("Department", le_dep.classes_)
day = st.selectbox("Day", le_day.classes_)
team = st.number_input("Team Number", min_value=1, step=1)
targeted_productivity = st.slider("Targeted Productivity", 0.0, 1.0, 0.75)
smv = st.number_input("SMV (Standard Minute Value)", min_value=0.0, value=25.0)
wip = st.number_input("Work in Progress (WIP)", min_value=0.0, value=1000.0)
overtime = st.number_input("Overtime (in minutes)", min_value=0, value=1000)
incentive = st.number_input("Incentive Amount", min_value=0, value=50)
idle_time = st.number_input("Idle Time (in minutes)", min_value=0.0, value=0.0)
idle_men = st.number_input("Idle Men", min_value=0, value=0)
style_changes = st.number_input("No. of Style Changes", min_value=0, value=0)
workers = st.number_input("Number of Workers", min_value=1.0, value=50.0)

if st.button("Predict Productivity"):
    input_data = pd.DataFrame({
        'quarter': [le_quarter.transform([quarter])[0]],
        'department': [le_dep.transform([department])[0]],
        'day': [le_day.transform([day])[0]],
        'team': [team],
        'targeted_productivity': [targeted_productivity],
        'smv': [smv],
        'wip': [wip],
        'over_time': [overtime],
        'incentive': [incentive],
        'idle_time': [idle_time],
        'idle_men': [idle_men],
        'no_of_style_change': [style_changes],
        'no_of_workers': [workers]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Worker Productivity: {prediction:.4f}")
