# 🧵 Worker Productivity Prediction App

A **Streamlit-based Machine Learning web app** that predicts the **actual productivity** of garment workers in a factory based on multiple real-time input factors such as overtime, incentive, idle time, style changes, and more.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://worker-appuctivity-prediction-mpmf9skrhqqlz6crqt8gyn.streamlit.app/)


---

## 📌 Project Overview

This app uses a **Random Forest Regressor** to predict worker productivity.  
It allows users to interactively input factory conditions like:

- Quarter, department, day
- Team number and number of workers
- Targeted productivity
- SMV (Standard Minute Value)
- Overtime, idle time, incentives
- Style changes and WIP (Work In Progress)

And receive an accurate prediction of **actual productivity**.

---

## 📁 Files in this Repository

| File                | Description                               |
|---------------------|-----------------------------------------|
| `app.py`            | The main Streamlit web app code          |
| `newpropro.csv`     | Sample dataset used for training         |
| `requirements.txt`  | List of Python dependencies              |
| `README.md`         | This file (project documentation)        |

---

