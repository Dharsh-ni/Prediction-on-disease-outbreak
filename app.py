import os
import pickle  # Pre-trained model loading
import streamlit as st  # Web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# Load models
diabetes_model = pickle.load(open(r"C:\Prediction on disease outbreak\saved_models\diabeties_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Prediction on disease outbreak\saved_models\heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Prediction on disease outbreak\saved_models\parkinsons_data.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# ============================ DIABETES PREDICTION ============================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    
    st.success(diab_diagnosis)

# ============================ HEART DISEASE PREDICTION ============================
elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input("Age")
    with col2:
        Sex = st.text_input("Sex (1=Male, 0=Female)")
    with col3:
        ChestPain = st.text_input("Chest Pain Type")
    with col1:
        RestingBP = st.text_input("Resting Blood Pressure")
    with col2:
        Cholesterol = st.text_input("Serum Cholesterol")
    with col3:
        FastingBS = st.text_input("Fasting Blood Sugar (1=True, 0=False)")
    with col1:
        RestECG = st.text_input("Resting ECG Results")
    with col2:
        MaxHR = st.text_input("Max Heart Rate Achieved")
    with col3:
        ExerciseAngina = st.text_input("Exercise-Induced Angina (1=Yes, 0=No)")
    with col1:
        Oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        Slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")
    with col3:
        MajorVessels = st.text_input("Number of Major Vessels (0-3)")
    with col1:
        Thalassemia = st.text_input("Thalassemia (0-3)")

    heart_diagnosis = ''
    if st.button("Heart Disease Test Result"):
        user_input = [Age, Sex, ChestPain, RestingBP, Cholesterol, FastingBS, RestECG, 
                      MaxHR, ExerciseAngina, Oldpeak, Slope, MajorVessels, Thalassemia]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = "The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
    
    st.success(heart_diagnosis)

# ============================ PARKINSON'S PREDICTION ============================
elif selected == "Parkinson's Prediction":
    st.title("Parkinson’s Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVP_Flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    with col3:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col1:
        Spread1 = st.text_input("Spread1")
    with col2:
        Spread2 = st.text_input("Spread2")
    
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, NHR, HNR, RPDE, DFA, Spread1, Spread2]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson’s disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson’s disease"
    
    st.success(parkinsons_diagnosis)
