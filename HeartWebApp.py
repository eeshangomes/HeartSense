import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from login import is_user_logged_in
from firebase_admin import firestore
loaded_model=pickle.load(open('/Users/eeshanonweb/Desktop/College/Mini Project/trained_model.sav','rb'))
medical_model=pickle.load(open('/Users/eeshanonweb/Desktop/College/Mini Project/medical_model.sav','rb'))
def heartdisease_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    if(prediction[0]==0):
        return "You are not at a risk of suffering from heart disease"
    else:
        return "You are at a high risk of suffering from heart disease"
def medical_prediction(medical_data):
    medical_data_as_numpy_array=np.asarray(medical_data)
    medical_data_reshaped=medical_data_as_numpy_array.reshape(1,-1)
    medical_prediction=medical_model.predict(medical_data_reshaped)
    if(medical_prediction[0]==0):
        return "According to medical data, you are NOT at a risk of suffering from heart disease"
    else:
        return "According to medical data, you are at a risk of suffering from heart disease"
def app():
    #st.set_page_config(
      #  page_title='HeartSense',
       # page_icon='🫀',
    #)
    if 'username' not in st.session_state or not st.session_state.username:
        st.warning("Please log in first.")
        st.stop() 
    try:
        # selected=option_menu(
        #     menu_title='',
        #     options=['Home','Prediction','Team'],
        #     icons=['house','magnifying_glass','phone'],
        #     menu_icon='cast',
        #     orientation='horizontal',
        # )
        st.title("Risk Prediction")
        #st.warning("Hello")
        st.subheader("Enter the following parameters to check whether you are at risk.")
        #getting input data
        st.markdown(
    """
    <style>
    /* Customize the color of the number input box */
    .stNumberInput > div > div > div > input {
        background-color:white; /* Change the color to your desired color */
        border-color: #aaa; /* Change the border color if needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)
        st.markdown(
    """
    <style>
    /* Customize the background color of the +/- buttons */
    .stNumberInput > div > div > button {
        background-color:white; /* Change the color to your desired color */
        border-color: #aaa; /* Change the border color if needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)
        db=firestore.client()
        st.session_state.db=db
        weight=st.number_input("Weight in Kilograms",value=60)
        height=st.number_input("Height in Metres",value=1.5)
        bmi=float(weight/(float(height)*float(height)))
        #st.write(bmi)
        #bmi=st.text_input("Body Mass Index")
        #smoking=st.text_input("Smoking")
        smoking=st.radio("Have You Smoked Frequently In The Past?",['No','Yes'])
        if smoking=='No':
            smoking=0
        else:
            smoking=1
        #st.write(smoking)
        #alcohol=st.text_input("Alcohol Consumption")
        alcohol=st.radio("Have You Comsumed Alcohol Regularly In The Past?",['No','Yes'])
        if alcohol=='No':
            alcohol=0
        else:
            alcohol=1
        stroke=st.radio("Have you had a stroke in the past?",['No','Yes'])
        if stroke=='No':
            stroke=0
        else:
            stroke=1
        #physicalhealth=st.text_input("Number Of Days In A Month You Experience Poor Physical Health")
        physicalhealth=st.slider('Number Of Days In A Month You Experience Poor Physical Health',min_value=0,max_value=30,value=10)
        #mental=st.text_input("Number Of Days In A Month You Experience Poor Mental Health")
        mental=st.slider('Number Of Days In A Month You Experience Poor Mental Health',min_value=0,max_value=30,value=20)
        diffwalk=st.radio("Experience Difficulty In Walking",['No','Yes'])
        if diffwalk=='No':
            diffwalk=0
        else:
            diffwalk=1
        sex=st.radio("Sex",['Male','Female'])
        realsex=0
        if sex=='Male':
            sex=1
            realsex=0
        else:
            sex=0
            realsex=1
        agecat=st.slider("Age",min_value=0,max_value=120,value=28)
        realage=agecat
        if agecat<=24:
            agecat=0
        elif agecat>=25 and agecat<=29:
            agecat=1
        elif agecat>=30 and agecat<=34:
            agecat=2
        elif agecat>=35 and agecat<=39:
            agecat=3
        elif agecat>=40 and agecat<=44:
            agecat=4
        elif agecat>=45 and agecat<=49:
            agecat=5
        elif agecat>=50 and agecat<=54:
            agecat=6
        elif agecat>=55 and agecat<=59:
            agecat=7
        elif agecat>=60 and agecat<=64:
            agecat=8
        elif agecat>=65 and agecat<=69:
            agecat=9
        elif agecat>=70 and agecat<=74:
            agecat=10
        elif agecat>=75 and agecat<=79:
            agecat=11
        elif agecat>=80:
            agecat=12
        race=st.radio("Race",['Asian','White','Black','Hispanic','Native American Indian/Alaskan','Other'])
        if race=='Native American Indian/Alaskan':
            race=0
        elif race=='Asian':
            race=1
        elif race=='Black':
            race=2
        elif race=='Hispanic':
            race=3
        elif race=='Other':
            race=4
        elif race=='White':
            race=5
        diabetic=st.radio("Are you diabetic?",['Yes','No'])
        if diabetic=='Yes':
            diabetic=1
        else:
            diabetic=0
        physactivity=st.radio("Have you been physically active in the past 30 days apart from your regular job?",['Yes','No'])
        if physactivity=='Yes':
            physactivity=1
        else:
            physactivity=0
        genhealth=st.slider("General Health On A Scale of 1 to 5 (1 being the Worst and 5 being the Best)",min_value=1,max_value=5,value=3)
        genhealth=genhealth-1
        sleeptime=st.slider("Sleep Time (Hours)",min_value=1,max_value=24,value=6)
        asthma=st.radio("Were/Are You Asthmatic?",['Yes','No'])
        if asthma=='Yes':
            asthma=1
        else:
            asthma=0
        #kidney=st.text_input("Kidney Disease")
        kidney=st.radio("Excluding kidney stones, bladder infection or incontinence, have you suffered from any kidney disease?",['Yes','No'])
        if kidney=='Yes':
            kidney=1
        else:
            kidney=0
        #skin=st.text_input("Skin Cancer")
        skin=st.radio("Have you suffered from Skin Cancer (Malignant Melanoma)?",['Yes','No'])
        if skin=='Yes':
            skin=1
        else:
            skin=0
        medical_tick=st.checkbox(label="Check this box to include medical parameters to the prediction",value=False)
        if medical_tick==True:
            rbp=st.number_input(label="Systolic Blood Sugar",value=120)
            chol=st.number_input(label="Cholestrol Level",value=170)
            fbs=st.number_input(label="Fasting Blood Sugar Level",value=80)
            if fbs>120:
                fbs=1
            else:
                fbs=0
            
        #prediction
        diagnosis=""
        medical_diagnosis=""
        #creating a button for prediciton
        if st.button('Click To Check Prediction'):
            temp=[bmi,smoking,alcohol,stroke,physicalhealth,mental,diffwalk,sex,agecat,race,diabetic,physactivity,genhealth,sleeptime,asthma,kidney,skin]
            db.collection('Past Records').document(st.session_state.username).set({'array_parameters':temp})
            diagnosis=heartdisease_prediction([bmi,smoking,alcohol,stroke,physicalhealth,mental,diffwalk,sex,agecat,race,diabetic,physactivity,genhealth,sleeptime,asthma,kidney,skin])
            if medical_tick:
                medical_diagnosis=medical_prediction([realage,realsex,rbp,chol,fbs])
                st.success(medical_diagnosis)
            else:
                st.success(diagnosis)
        
    except:
        if st.session_state.username=='':
            st.text('Please Login first')     

if __name__=='__main__':
    app()