# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth
# from firebase_admin import firestore

# # Initialize Firebase app if not already initialized
# if not firebase_admin._apps:
#     cred = credentials.Certificate('heartsense-47fb3-76ea125a9f6d.json')
#     firebase_admin.initialize_app(cred)

# # Get Firestore client
# db = firestore.client()

# def is_user_logged_in():
#     return 'username' in st.session_state
# def sign_out():
#     st.session_state.signedout=False
#     st.session_state.signout=False
#     st.session_state.username=""
# def save_password(username, password):
#     try:
#         # Add document to "Passwords" collection with username as document ID
#         db.collection('Passwords').document(username).set({'password': password})
#         st.success('Password saved successfully')
#     except Exception as e:
#         st.error(f'Failed to save password: {e}')

# def get_stored_password(username):
#     try:
#         # Retrieve password from Firestore
#         doc_ref = db.collection('Passwords').document(username)
#         doc = doc_ref.get()
#         if doc.exists:
#             return doc.to_dict().get('password')
#         else:
#             return None  # User does not exist
#     except Exception as e:
#         st.error(f'Failed to retrieve password: {e}')
#         return None

# def login(username, password):
#     try:
#         stored_password = get_stored_password(username)
#         if stored_password is None:
#             st.warning('User does not exist')
#             return False
#         elif password == stored_password:
#             st.success('Login Successful')
#             return True
#         else:
#             st.warning('Incorrect password')
#             return False
#     except Exception as e:
#         st.error(f'Login failed: {e}')
#         return False

# def app():
#     st.title("Login/Create An Account")

#     if 'username' not in st.session_state:
#         st.session_state.username = ""
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ""

#     if not st.session_state.get('signedout', False):
#         choice = st.selectbox('Login/Sign Up', ['Login', 'Sign-Up'])

#         if choice == 'Login':
#             email = st.text_input('E-Mail Address')
#             password = st.text_input('Password', type='password')
#             username = st.text_input('Username')
#             if st.button('Login'):
#                 if login(username, password):
#                     st.session_state.username = username
#                     st.session_state.useremail = email
#                     st.session_state.signedout = True
#                 else:
#                     st.warning('Login Failed')
#         elif choice == 'Sign-Up':
#             realname = st.text_input('Name')
#             email = st.text_input('E-Mail Address')
#             password = st.text_input('Password', type='password')
#             username = st.text_input('Enter Unique Username')
#             if st.button('Create Account'):
#                 user = auth.create_user(display_name=realname, email=email, password=password, uid=username)
#                 if user:
#                     st.session_state.username = username
#                     st.session_state.useremail = email
#                     st.session_state.signedout = True
#                     save_password(username, password)  # Save password to Firestore
#                     st.success('Account Created Successfully')

#     if st.session_state.get('signedout', False):
#         st.text('Username: ' + st.session_state.username)
#         st.text('E-mail ID: ' + st.session_state.useremail)
#         if st.button('Sign Out'):
#             sign_out()

# # Run the app
# #app()

# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth
# from firebase_admin import firestore

# # Initialize Firebase app if not already initialized
# if not firebase_admin._apps:
#     cred = credentials.Certificate('heartsense-47fb3-76ea125a9f6d.json')
#     firebase_admin.initialize_app(cred)

# # Get Firestore client
# db = firestore.client()

# def is_user_logged_in():
#     return 'username' in st.session_state

# def get_stored_password(username):
#     try:
#         # Retrieve password from Firestore
#         doc_ref = db.collection('Passwords').document(username)
#         doc = doc_ref.get()
#         if doc.exists:
#             return doc.to_dict().get('password')
#         else:
#             return None  # User does not exist
#     except Exception as e:
#         st.error(f'Failed to retrieve password: {e}')
#         return None

# def login(username, password):
#     try:
#         stored_password = get_stored_password(username)
#         if stored_password is None:
#             st.warning('User does not exist')
#             return False
#         elif password == stored_password:
#             st.success('Login Successful')
#             st.session_state.username = username
#             return True
#         else:
#             st.warning('Incorrect password')
#             return False
#     except Exception as e:
#         st.error(f'Login failed: {e}')
#         return False

# def save_password(username, password):
#     try:
#         # Add document to "Passwords" collection with username as document ID
#         db.collection('Passwords').document(username).set({'password': password})
#         st.success('Password saved successfully')
#     except Exception as e:
#         st.error(f'Failed to save password: {e}')

# def app():
#     st.title("Login/Create An Account")

#     if 'username' not in st.session_state:
#         st.session_state.username = ""

#     if not st.session_state.get('signedout', False):
#         choice = st.selectbox('Login/Sign Up', ['Login', 'Sign-Up'])

#         if choice == 'Login':
#             username = st.text_input('Username')
#             password = st.text_input('Password', type='password')
#             if st.button('Login'):
#                 if login(username, password):
#                     st.session_state.signedout = True
#                 else:
#                     st.warning('Login Failed')
#         elif choice == 'Sign-Up':
#             realname = st.text_input('Name')
#             email=st.text_input('E-Mail')
#             username = st.text_input('Enter Unique Username')
#             password = st.text_input('Password', type='password')
#             if st.button('Create Account'):
#                 user = auth.create_user(display_name=realname, email=email, password=password, uid=username)
#                 if user:
#                     st.session_state.username = username
#                     st.session_state.signedout = True
#                     save_password(username, password)  # Save password to Firestore
#                     st.success('Account Created Successfully')

#     if st.session_state.get('signedout', False):
#         st.text('Username: ' + st.session_state.username)
#         if st.button('Sign Out'):
#             st.session_state.clear()

# # Run the app
# #app()

# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth
# from firebase_admin import firestore

# # Initialize Firebase app if not already initialized
# if not firebase_admin._apps:
#     cred = credentials.Certificate('heartsense-47fb3-76ea125a9f6d.json')
#     firebase_admin.initialize_app(cred)

# # Get Firestore client
# db = firestore.client()

# def is_user_logged_in():
#     return 'username' in st.session_state

# def sign_out():
#     st.session_state.signedout = False
#     st.session_state.signout = False
#     st.session_state.username = ""

# def save_password(email, password):
#     try:
#         # Add document to "Passwords" collection with email as document ID
#         db.collection('Passwords').document(email).set({'password': password})
#         st.success('Password saved successfully')
#     except Exception as e:
#         st.error(f'Failed to save password: {e}')

# def get_stored_password(email):
#     try:
#         # Retrieve password from Firestore
#         doc_ref = db.collection('Passwords').document(email)
#         doc = doc_ref.get()
#         if doc.exists:
#             return doc.to_dict().get('password')
#         else:
#             return None  # User does not exist
#     except Exception as e:
#         st.error(f'Failed to retrieve password: {e}')
#         return None

# def login(email, password):
#     try:
#         stored_password = get_stored_password(email)
#         if stored_password is None:
#             st.warning('User does not exist')
#             return False
#         elif password == stored_password:
#             st.success('Login Successful')
#             return True
#         else:
#             st.warning('Incorrect password')
#             return False
#     except Exception as e:
#         st.error(f'Login failed: {e}')
#         return False

# def app():
#     st.title("Login/Create An Account")

#     if 'username' not in st.session_state:
#         st.session_state.username = ""
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ""

#     if not st.session_state.get('signedout', False):
#         choice = st.selectbox('Login/Sign Up', ['Login', 'Sign-Up'])

#         if choice == 'Login':
#             email = st.text_input('E-Mail Address')
#             password = st.text_input('Password', type='password')
#             if st.button('Login'):
#                 if login(email, password):
#                     st.session_state.username = email
#                     st.session_state.useremail = email
#                     st.session_state.signedout = True
#                 else:
#                     st.warning('Login Failed')
#         elif choice == 'Sign-Up':
#             realname = st.text_input('Name')
#             email = st.text_input('E-Mail Address')
#             password = st.text_input('Password', type='password')
#             if st.button('Create Account'):
#                 user = auth.create_user(display_name=realname, email=email, password=password)
#                 if user:
#                     st.session_state.username = email
#                     st.session_state.useremail = email
#                     st.session_state.signedout = True
#                     save_password(email, password)  # Save password to Firestore
#                     st.success('Account Created Successfully')

#     if st.session_state.get('signedout', False):
#         #st.text('Username: ' + st.session_state.username)
#         st.text('E-mail ID: ' + st.session_state.useremail)
#         if st.button('Sign Out'):
#             sign_out()

# # Run the app
# #app()

import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import hashlib

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('heartsense-47fb3-76ea125a9f6d.json')
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

def encrypt_password(password):
    # Generate a hash using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_password(email, password):
    try:
        # Encrypt password before saving
        encrypted_password = encrypt_password(password)
        # Add document to "Passwords" collection with email as document ID
        db.collection('Passwords').document(email).set({'password': encrypted_password})
        #st.success('Password saved successfully')
    except Exception as e:
        st.error(f'Failed to save password: {e}')

def get_stored_password(email):
    try:
        # Retrieve password from Firestore
        doc_ref = db.collection('Passwords').document(email)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict().get('password')
        else:
            return None  # User does not exist
    except Exception as e:
        st.error(f'Failed to retrieve password: {e}')
        return None

def login(email, password):
    try:
        stored_password = get_stored_password(email)
        if stored_password is None:
            st.warning('User does not exist')
            return False
        elif encrypt_password(password) == stored_password:
            st.success('Login Successful')
            return True
        else:
            st.warning('Incorrect password')
            return False
    except Exception as e:
        st.error(f'Login failed: {e}')
        return False

def app():
    st.title("Login/Create An Account")

    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ""

    if not st.session_state.get('signedout', False):
        choice = st.selectbox('Login/Sign Up', ['Login', 'Sign-Up'])

        if choice == 'Login':
            email = st.text_input('E-Mail Address')
            password = st.text_input('Password', type='password')
            if st.button('Login'):
                if login(email, password):
                    st.session_state.username = email
                    st.session_state.useremail = email
                    st.session_state.signedout = True
                else:
                    st.warning('Login Failed')
        elif choice == 'Sign-Up':
            realname = st.text_input('Name')
            email = st.text_input('E-Mail Address')
            password = st.text_input('Password', type='password')
            if st.button('Create Account'):
                save_password(email, password)  # Save hashed password to Firestore
                st.success('Account Created Successfully')
                st.session_state.username = email
                st.session_state.useremail = email
                st.session_state.signedout = True

    if st.session_state.get('signedout', False):
        #st.text('Username: ' + st.session_state.username)
        st.text('E-mail ID: ' + st.session_state.useremail)
        if st.button('Sign Out'):
            st.session_state.signedout = False
            st.session_state.signout = False
            st.session_state.username = ""

