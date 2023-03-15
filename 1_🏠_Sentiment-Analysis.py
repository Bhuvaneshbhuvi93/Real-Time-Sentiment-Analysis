import streamlit as st
from streamlit_player import st_player


st.set_page_config(
    layout = "wide",
    page_title = "RT Sentiment Analysis",
    page_icon = "🔥",
)
 
st.title("📍Real Time Sentiment Analysis")
st.write("Sentiment analysis is the process of analyzing text to determine the emotional tone of the text. It involves using natural language processing (NLP) techniques to classify text as positive, negative or neutral. The goal of sentiment analysis is to understand the sentiment of the writer or speaker and to determine how they feel about a particular topic or product. It has applications in a variety of fields, including marketing, customer service, and public opinion analysis.")
st.subheader("📍Use Cases")
st.write("The most common use cases we see sentiment analysis applied to is on social media, customer service, and market research.")
st_player("https://youtu.be/sG9PRsvfr5Q")

st.subheader("📍NLP and NLTK")
st.write("""The area of artificial intelligence known as NLP (Natural Language Processing) studies how computers and human language interact. It includes analyzing, comprehending, and producing human language using computational methods. Sentiment analysis, language translation, text classification, and speech detection are just a few of the many uses for NLP.

A popular Python tool for NLP is called NLTK (Natural Language Toolkit). It offers a selection of tools and materials for handling data relating to human language. Tokenization, stemming, lemmatization, part-of-speech tagging, named entity recognition, and sentiment analysis are a few of the jobs that can be carried out using NLTK. In both academia and business, NLTK is frequently used for NLP study and development.""")

st.subheader("📍Reference")
st.write("[Project Source](https://amankharwal.medium.com/data-analysis-projects-with-python-a262a6f9e68c)")
st.write("[Repository](https://github.com/Bhuvaneshbhuvi93/RealTimeSentimentAnalysis.git)")