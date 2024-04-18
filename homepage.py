import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

#st.set_page_config(page_title='HeartSense',page_icon=':anatomical_heart:',layout='wide')
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def app():
    
    lottie_coding=load_lottieurl('https://lottie.host/be9aacb7-d4d7-44b2-8699-1bc50f7fc006/OnsDzHMNqI.json')
    with st.container():
        st.title("HeartSense: Home")
        #st.subheader("Heart Disease Risk Prediction Using Machine Learning")
    
    with st.container():
        st.write('---')
        left_column,right_column=st.columns(2)
        with left_column:
            st.header('About')
            st.write('##')
            st.write(
                """
                Heart disease refers to a range of conditions that affect the heart, its blood vessels, and its function. It's one of the leading causes of death worldwide, with various factors contributing to its development. 
                
                """
            )
        with right_column:
            st_lottie(lottie_coding,height='300',key='heart')
    


    
#if __name__ == "__main__":
  #  main()
