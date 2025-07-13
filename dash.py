# import streamlit as st
# import pandas as pd
# from firebase_admin import firestore

# def retrieve_predictions_for_user():
#     if 'username' not in st.session_state or not st.session_state.username:
#         st.session_state.username = None 
#         st.warning("Please Login First")
    
#     db = firestore.client()
#     user_collection_ref = db.collection('Past Records').document(st.session_state.username).collection('Predictions')

#     # Get all documents in the user's collection
#     docs = user_collection_ref.stream()

#     # List to store predictions
#     predictions = []

#     # Iterate over the documents
#     for doc in docs:
#         # Get the data from each document
#         doc_data = doc.to_dict()
        
#         # Extract heart disease diagnosis and input parameters
#         heart_disease_diagnosis = doc_data.get('heart_disease_diagnosis')
#         input_parameters = doc_data.get('input_parameters')
        
#         # Create a dictionary to hold the prediction data
#         prediction = {'Timestamp': doc.id, 'Heart Disease Diagnosis': heart_disease_diagnosis}
        
#         # Manually define parameter names
#         parameter_names = ['BMI','Smoked Frequently','alcohol','stroke','physicalhealth','mental','diffwalk','sex','realage','race','diabetic','physactivity','genhealth','sleeptime','asthma','kidney','skin','rbp','chol','fbs']  # Add more parameter names as needed
#         for name, value in zip(parameter_names, input_parameters):
#             # if name=='Smoked Frequently':
#             #     if value==0:
#             #         prediction[name]='No'
#             #     else:
#             #         prediction[name]='Yes'
#             prediction[name] = value
#         # Check if parameter names match input parameters
#         # if len(parameter_names) == len(input_parameters):
#         #     for name, value in zip(parameter_names, input_parameters):
#         #         prediction[name] = value
#         # else:
#         #     # If parameter names don't match input parameters, use generic labels
#         #     for i, param in enumerate(input_parameters):
#         #         prediction[f'Parameter {i+1}'] = param
        
#         # Append the prediction to the list of predictions
#         predictions.append(prediction)

#     return predictions

# def app():
#     # if 'username' not in st.session_state:
#     #     st.session_state.username=""
#     # if 'username' not in st.session_state:
#     #     st.session_state.username = None 
#     #     st.warning("Please Login First")
#     # st.button(label='Click To View Previous Predictions')
#     # if st.button:
#     st.title('Your Predictions')
#     user_predictions = retrieve_predictions_for_user()
    
#     # Display table
#     if user_predictions:
#         st.table(pd.DataFrame(user_predictions))
#     else:
#         if st.session_state.username:
#             st.write("No predictions found for this user.")

# # Call the app function


import streamlit as st
import pandas as pd
from firebase_admin import firestore

def retrieve_predictions_for_user():
    if 'username' not in st.session_state or not st.session_state.username:
        st.session_state.username = None 
        st.warning("Please Login First")
    
    db = firestore.client()
    user_collection_ref = db.collection('Past Records').document(st.session_state.username).collection('Predictions')

    # Get all documents in the user's collection
    docs = user_collection_ref.stream()

    # List to store predictions
    predictions = []

    # Iterate over the documents
    for doc in docs:
        # Get the data from each document
        doc_data = doc.to_dict()
        
        # Extract heart disease diagnosis and input parameters
        heart_disease_diagnosis = doc_data.get('heart_disease_diagnosis')
        input_parameters = doc_data.get('input_parameters')
        
        # Create a dictionary to hold the prediction data
        prediction = {'Timestamp': doc.id, 'Heart Disease Diagnosis': heart_disease_diagnosis}
        
        # Manually define parameter names
        parameter_names = ['BMI','Smoked Frequently','Regular Alcohol Consumption','History Of Stroke','No Of Days Experienced Poor Physical Health','No Of Days Experienced Poor Mental Health','Experienced Difficulty In Walking','Sex','Age','Race','Diabetic','Been Physically Active In Past 30 Days','General Health (Scale of 1 to 5)','Sleep Time (Hours)','Asthma History','Suffered From Kidney Disease?','Suffered From Skin Cancer?','rbp','chol','fbs']  # Add more parameter names as needed
        for name, value in zip(parameter_names, input_parameters):
            if name == 'Smoked Frequently' and value == 0:
                value = 'No'
            elif name == 'Smoked Frequently' and value == 1:
                value = 'Yes'
            elif name == 'Regular Alcohol Consumption' and value == 0:
                value = 'No'
            elif name == 'Regular Alcohol Consumption' and value == 1:
                value = 'Yes'
            elif name == 'History Of Stroke' and value == 0:
                value = 'No'
            elif name == 'History Of Stroke' and value == 1:
                value = 'Yes'
            elif name == 'History Of Stroke' and value == 0:
                value = 'No'
            elif name == 'History Of Stroke' and value == 1:
                value = 'Yes'
            elif name == 'Experienced Difficulty In Walking' and value == 0:
                value = 'No'
            elif name == 'Experienced Difficulty In Walking' and value == 1:
                value = 'Yes'
            elif name == 'Sex' and value == 0:
                value = 'Female'
            elif name == 'Sex' and value == 1:
                value = 'Male'
            elif name == 'Age' and value == 0:
                value = 'Less Than 25'
            elif name == 'Age' and value == 1:
                value = '25-29'
            elif name == 'Age' and value == 2:
                value = '30-34'
            elif name == 'Age' and value == 3:
                value = '35-39'
            elif name == 'Age' and value == 4:
                value = '40-44'
            elif name == 'Age' and value == 5:
                value = '45-49'
            elif name == 'Age' and value == 6:
                value = '50-54'
            elif name == 'Age' and value == 7:
                value = '55-59'
            elif name == 'Age' and value == 8:
                value = '60-64'
            elif name == 'Age' and value == 9:
                value = '65-69'
            elif name == 'Age' and value == 10:
                value = '70-74'
            elif name == 'Age' and value == 11:
                value = '75-79'
            elif name == 'Age' and value == 12:
                value = '80 Or Above'
            elif name == 'Race' and value == 0:
                value = 'Native American Indian/Alaskan'
            elif name == 'Race' and value == 1:
                value = 'Asian'
            elif name == 'Race' and value == 2:
                value = 'Black'
            elif name == 'Race' and value == 3:
                value = 'Hispanic'
            elif name == 'Race' and value == 4:
                value = 'Other'
            elif name == 'Race' and value == 5:
                value = 'White'
            elif name == 'Diabetic' and value == 0:
                value = 'No'
            elif name == 'Diabetic' and value == 1:
                value = 'Yes'
            
            elif name == 'Been Physically Active In Past 30 Days' and value == 0:
                value = 'No'
            elif name == 'Been Physically Active In Past 30 Days' and value == 1:
                value = 'Yes'
            elif name == 'Asthma History' and value == 0:
                value = 'No'
            elif name == 'Asthma History' and value == 1:
                value = 'Yes'
            elif name == 'Suffered From Kidney Disease?' and value == 0:
                value = 'No'
            elif name == 'Suffered From Kidney Disease?' and value == 1:
                value = 'Yes'
            
            elif name == 'Suffered From Skin Cancer?' and value == 0:
                value = 'No'
            elif name == 'Suffered From Skin Cancer?' and value == 1:
                value = 'Yes'
            prediction[name] = value
        
        # Append the prediction to the list of predictions
        predictions.append(prediction)

    return predictions

def app():
    st.title('Your Predictions')
    user_predictions = retrieve_predictions_for_user()
    
    # Display table
    if user_predictions:
        st.table(pd.DataFrame(user_predictions))
    else:
        if st.session_state.username:
            st.write("No predictions found for this user.")

# Call the app function
