# Real Estate Law Chatbot for Monaco

## Overview

This chatbot provides information and answers questions related to real estate laws in Monaco. 
* designed to assist users in French. The bot is built using a fine-tuned language model and is deployed through a Streamlit application for easy interaction.

### WHY?
* A lot of foreigners move to Monaco every year.
* Most of them are unfamiliar with local laws, and how to become a resident. 

They usually come to real estate companies, or accounting firms for advice on how to set up their business and the steps to become a resident. 

* Monaco is quite unusual as it has many different real estate and residency laws that are specific to the country, despite its very small size. 
* Our aim with this project is to provide a resource for these foreigners to be better informed, and make the whole process less daunting.
* Our chatbot can, and will also be used by professionals in real estate/accounting to keep them informed. 

## Data

Our data for the model had to be structured as input, output at first. For a few reasons we have kept the datasize small, mainly this make the process less hardware intensive, and we are not subject matter expert and will require more input to make the model more accurate. 
We scraped the data from various websites. These are the government website, several real estate firms' websites, and the "monaco laws bible". The mian challenge here was to split data from one source into the smaller sized chunks that still conatined all the information we needed the model to know. Law texts are long, tedious and often include language that is not necessary in our application. This is where we can use a subject matter expert's opinion and guidance. 
We made use of chat gpt to structure our data properly and prepare it for the model. We then split it into test and training sets. 

## Model Used 
We want to use Mistral 7B in this case, as it is open source, cheaper to train and outperforms a lot of models. 
However, due to some computational challenges we chose DistilBERT (much smaller), and can do the trick for the demo, and until we get more data. 
This will allow us to focus on the data, and adding to it until we have ~500 samples. 

## Requirements

* Python 3.6 or later
* Streamlit
* Transformers library by Hugging Face
* PyTorch


## Running the app
`streamlit run app.py`

## Usage 
Enter your question about Monaco's real estate law in French in the text input field. The chatbot will process your question and provide a response in French.

## Improvements 
There are a lot of improvements that we could do, these include actually training a model, and making it conversational. 
The main improvement that I will focus on before training a model, is to get a lot more data points and make sure that these are accurate for all the potential users. 
We might have to use a different model, like a new custom GPT, but that would not be cost efficient, for an experimental project.
The goal with this is to have a chatbot that could be used by lawyers, accountants and real estate professionals alike. 

## Disclaimer
This chatbot is intended for informational purposes only and does not substitute for professional legal advice. Reliance on the information provided by the chatbot is solely at the user's risk.
