import streamlit as st

from streamlit_option_menu import option_menu


import homepage, HeartWebApp, login, features
#from login import is_user_logged_in
st.set_page_config(page_title="HeartSense",page_icon='🫀') #layout="wide")
if __name__=="__main__":
    import dash


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='HeartSense ',
                options=['Home','Features','Login/SignUp','Predict Risk','Dashboard'],
                icons=['house-fill','book','person-circle','binoculars-fill','journal-text','people'],#'trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='heart-pulse',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#fff6e9'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#40a2e3"},
        "nav-link-selected": {"background-color": "#bbe2ec"},}
                
                )

        
        if app == "Home":
            homepage.app()
        if app == "Predict Risk":
             HeartWebApp.app()
        if app == "Login/SignUp":
            login.app()
        if app=="Dashboard":
            dash.app()
        if app=='Features':
            features.app()
        # if app=='Team':
        #     team.app()
         
             
          
             
    run()      