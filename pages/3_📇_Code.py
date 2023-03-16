import streamlit as st
import base64

st.set_page_config(
    layout = "wide",
    page_title = "RT Sentiment Analysis",
    page_icon = "🔥", 
)

st.subheader("Importing Dependensies")
code = '''from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')'''

st.code(code, language='python')

st.subheader("Sentiment Analyser")
code = '''user_review = input('Please Rate Our Service: ')
sia = SentimentIntensityAnalyzer()
score = sia.polarity_scores(user_review)
print(score)'''

st.code(code, language='python')
st.write("{'neg': 1.0, 'neu': 0.0, 'pos': 0.0, 'compound': -0.5423}")

st.subheader("Final Prediction")
code = '''user_review = input('Please Rate Our Service: ')
sia = SentimentIntensityAnalyzer()
scores = sia.polarity_scores(user_review)
sentiments_score = [scores['neg'],scores['neu'],scores['pos']]
if sentiments_score[0] > sentiments_score[2]:
print('Negative')
elif sentiments_score[2] > sentiments_score[0]:
print('Positive')
else:
print('Neutral')'''

st.code(code, language='python')
st.write("Neutral")