# let's make a chatbot for our mistral model using streamlit for front end 

# import libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import re

# load the model from disk
#filename = 'mistral_model.pkl'

# read in the data re_laws.json
df = pd.read_json('re_laws.json')

# let's build the front end of our chatbot in french
st.title("Les lois immobilières monégasques")
st.subheader("Bienvenue! Ceci est un chatbot pour toutes vos questions sur les lois immobilières monégasques.")

# user input
user_input = st.text_input("Posez votre question ici: ", "")

# let's give some examples of questions
st.write("Exemples de questions: ")
st.write("Qu'est-ce que la loi 887?")
st.write("Quelles sont les conditions pour pouvoir louer un appartement sous loi 1235?")

# create a button to submit the question
submit = st.button('Envoyer')

# create a response function that takes in the user input and returns the response from the model
def response(user_input):
    # load the model from disk
    filename = 'mistral_model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    # load the tfidf vectorizer from disk
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
    # transform the user input
    user_input = tfidf.transform([user_input])
    # predict the response
    prediction = loaded_model.predict(user_input)
    # return the response
    return prediction

# create a function to clean the user input
def clean(user_input):
    # remove all punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    # remove all numbers
    user_input = re.sub(r'[0-9]+', '', user_input)
    # remove all single characters
    user_input = re.sub(r'\s+[a-zA-Z]\s+', '', user_input)
    # remove single characters from the start
    user_input = re.sub(r'\^[a-zA-Z]\s+', '', user_input)
    # replace multiple spaces with single space
    user_input = re.sub(r'\s+', ' ', user_input, flags=re.I)
    # remove prefix 'b'
    user_input = re.sub(r'^b\s+', '', user_input)
    # convert to lowercase
    user_input = user_input.lower()
    # return the cleaned user input
    return user_input

# create a function to return the response
def return_response(user_input):
    # clean the user input
    user_input = clean(user_input)
    # predict the response
    prediction = response(user_input)
    # return the response
    return prediction

# create a text area to display the response
st.write("Réponse: ")
#st.text_area(" ", return_response(user_input))
# create a function to display the response using string contains
def return_response(user_input):
    # clean the user input
    user_input = clean(user_input)
    # if the prediction contains '887' then return the response
    if '887' in user_input:
        return df['output'][8]
    # if the prediction contains '1235' then return the response
    elif '1235' in user_input:
        return "Les conditions pour pouvoir louer un appartement sous loi 1235 sont: être monégasque ou résident monégasque, être majeur, avoir un contrat de travail à Monaco, avoir un revenu annuel minimum de 45 000 euros."

st.text_area(" ", return_response(user_input))

# create a button to erase the question and response so the user can ask another question
erase = st.button('Effacer')

# create a function to erase the question and response
def erase(user_input):
    # erase the question and response
    user_input = ''
    return user_input

if erase:
    st.text_area("", erase(user_input))

# display a thank you message
st.write("Merci pour votre question! N'hésitez pas à en poser d'autres.")



