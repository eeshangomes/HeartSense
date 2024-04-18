import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
if not firebase_admin._apps:
    cred=credentials.Certificate('heartsense-47fb3-76ea125a9f6d.json')
    firebase_admin.initialize_app(cred)
def is_user_logged_in():
    return 'username' in st.session_state
def app():
    st.title("Login/Create An Account")
    #choice=st.selectbox('Login/Sign Up',['Login','Sign-Up'])
    if 'username' not in st.session_state:
        st.session_state.username=""
    if 'useremail' not in st.session_state:
        st.session_state.useremail=""
    def f():
        try:
            user=auth.get_user_by_email(email)
            st.write('Login Successfull')
            st.session_state.username=user.uid
            st.session_state.useremail=user.email
            st.session_state.signedout=True
            st.session_state.signout=True
        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signedout=False
        st.session_state.signout=False
        st.session_state.username=""

    if "signedout" not in st.session_state:
        st.session_state.signedout=False
    if "signout" not in st.session_state:
        st.session_state.signout=False

    if not st.session_state['signedout']:
        choice=st.selectbox('Login/Sign Up',['Login','Sign-Up'])

        if choice=='Login':
            email=st.text_input('E-Mail Address')
            password=st.text_input('Password',type='password')
            st.button('Login',on_click=f)
        elif choice=='Sign-Up':
            email=st.text_input('E-Mail Address')
            password=st.text_input('Password',type='password')
            username=st.text_input('Enter Unique Username')
            if st.button('Create Account'):
                user=auth.create_user(email=email,password=password,uid=username)

                st.success('Account Created Succesfully')
                st.balloons()
    if st.session_state.signout:
        st.text('Name: '+st.session_state.username)
        st.text('E-mail ID: '+st.session_state.useremail)
        st.button('Sign Out',on_click=t)
