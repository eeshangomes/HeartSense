import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# import tensorflow as tf
# from PIL import Image

#st.set_page_config(page_title='HeartSense',page_icon=':anatomical_heart:',layout='wide')
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def app():
    lottie_coding=load_lottieurl('https://lottie.host/be9aacb7-d4d7-44b2-8699-1bc50f7fc006/OnsDzHMNqI.json')
    lottie_coding_2=load_lottieurl('https://lottie.host/8c42757d-fab5-4db3-bb64-b76efd1f763c/py0inVXbr5.json')
#     st.markdown(
#     """
#     <style>
#     /* Customize the background color of the +/- buttons */
#     .stMarkdown > div{
#         text-align:justify;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
    with st.container():
        st.title("HeartSense Can Potentially Save Millions Of Lives")
        #st.subheader("Heart Disease Risk Prediction Using Machine Learning")
    image_url = "https://storage.googleapis.com/kagglesdsdata/competitions/31254/3103714/images/010/0108775015.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20240427%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240427T053939Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=5731d8fdd22172b5ba00cf0df2d80429ba58cd26daf9642f7fc6ca88b532d5da3b8e9781bc2bed0c13c44fad365afa9d8935e8d0d1dd4584251498ced61288f66ad4571dd11ffd0299af478b7f1740f865d31dc06537e6c6a4a680122e3c1a38dba2c755911fc63d46cac44304aa9205aacb95b48dd4c9b1cbd71bda333a7da399303e5f6718fdf096e162b0f3b28b683811430c1be8fe9900e4ed4651933fd43829f096314e74052dd00424b44da7ebf0d2ac463efd980c13e4ff0767365eed87735a3cfc8a4bc17ac192d26bdef2c135a92053de2e9bd1d64a9134c0bfb18c61537325778f5e592cf7d0f4ca90d3b993ae1a19527d500b9043bc699ad0bd8b"  # Replace this with the actual URL
    
    # Display image using Streamlit
    #st.image(image_url, caption='Image from URL', use_column_width=True)
    with st.container():
        st.write('---')
        left_column,right_column=st.columns(2)
        with left_column:
            st.markdown(
        """
        <style>
        .left-container-text {
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
            
            st.header('The Leading Cause Of Death, Globally')
            st.write('##')
            st.markdown('<div class="left-container-text">Heart disease encompasses a range of conditions affecting the heart, its blood vessels, and its function. It stands as the leading cause of death worldwide, contributing significantly to the global burden of disease. According to the World Health Organization (WHO), heart disease accounts for an estimated <b>17.9 million deaths annually</b>, making it the primary cause of mortality across the globe.</div>', unsafe_allow_html=True)
            #st.write('Heart disease encompasses a range of conditions affecting the heart, its blood vessels, and its function. It stands as the leading cause of death worldwide, contributing significantly to the global burden of disease. According to the World Health Organization (WHO), heart disease accounts for an estimated **17.9 million deaths annually**, making it the primary cause of mortality across the globe.')
            st.write('')
            st.write('')
            st_lottie(lottie_coding_2,height='300')
            

        with right_column:
            st.markdown(
        """
        <style>
        .right-container-text {
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
            #st.metric(label="Deaths Due To CVD's",value="17.9 Mil")
            st_lottie(lottie_coding,height='300',key='heart')
            st.header('The Urgency of Early Intervention')
            st.write('##')
            st.markdown('<div class="left-container-text">Early intervention is paramount in combating heart disease and preventing its devastating consequences. Implementing preventive measures and adopting heart-healthy habits can significantly reduce the risk of developing heart conditions. Lifestyle factors such as regular physical activity, maintaining a balanced diet, avoiding tobacco use, managing stress, and monitoring blood pressure and cholesterol levels are crucial in mitigating the risk of heart disease.</div>', unsafe_allow_html=True)
            #st.write('Early intervention is paramount in combating heart disease and preventing its devastating consequences. Implementing preventive measures and adopting heart-healthy habits can significantly reduce the risk of developing heart conditions. Lifestyle factors such as regular physical activity, maintaining a balanced diet, avoiding tobacco use, managing stress, and monitoring blood pressure and cholesterol levels are crucial in mitigating the risk of heart disease.')
        
        st.header('How HeartSense Comes Into The Picture')
        st.markdown(
    """
    <div style="text-align: justify">
    HeartSense will predict the risk of suffering from heart diseases using non-medical parameters that are easily accessible to everyone and do not require expensive tests/procedures in order to obtain. Using these parameters and advanced Machine Learning Algorithms, it predicts the risk.
    </div>
    """,
    unsafe_allow_html=True
)

        #st.write('HeartSense will predict the risk of suffering from heart diseases using non-medical parameters that are easily accessible to everyone and do not require expensive tests/procedures in order to obtain. Using these parameters and advanced Machine Learning Algorithms, it predicts the risk.')
    # dataset_name = "H&M Personalized Fashion Recommendations"  # Change to your dataset name
    # file_path = "images/010/0108775044.jpg"  # Change to the file path within the dataset
    
    # # Get image from Kaggle dataset without downloading
    # with tf.io.gfile.GFile(f"/kaggle/input/{dataset_name}/{file_path}", 'rb') as f:
    #     image = Image.open(f)
    
    # # Display image using Streamlit
    # st.image(image, caption='Image from Kaggle Dataset', use_column_width=True)



    
#if __name__ == "__main__":
  #  main()
