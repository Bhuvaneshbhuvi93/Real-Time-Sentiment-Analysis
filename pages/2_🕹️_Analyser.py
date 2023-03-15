import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
from PIL import Image

st.set_page_config( 
    layout = "wide",
    page_title = "RT Sentiment Analysis",
    page_icon = "🔥",
)

st.title("Real Time Sentiment Analyzer")

st.markdown("""---""")
st.header("⭐User Rating")
st.markdown("""---""")
user_review = st.slider("Please rate our service:",1,5)

st.write("""Where: \n 
⭐ is 'Very Bad'\n 
⭐⭐ is 'Bad'\n 
⭐⭐⭐ is 'Neutral'\n 
⭐⭐⭐⭐ 'Good'\n 
⭐⭐⭐⭐⭐'Very Good'""")

review_list = []
if user_review == 1:
    review_list.append('Very Bad')
elif user_review == 2:
    review_list.append('Bad')
elif user_review == 3:
    review_list.append('Neutral')
elif user_review == 4:
    review_list.append('Good')
elif user_review == 5:
    review_list.append('Very Good')
else:
    print("Invalid rating. Please enter a rating between 1 and 5.")

st.markdown("""---""")

sia = SentimentIntensityAnalyzer()
scores = sia.polarity_scores(review_list[0])


sentiments_score = [scores['neg'],scores['neu'],scores['pos']]

negative = Image.open('disappointed.png')
neutral = Image.open('neutral.png')
positive = Image.open('winking.png')

st.header("😶Sentiment")
st.markdown("""---""")
if sentiments_score[0]  > sentiments_score[2]:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Negative**')
    col2.image(negative)
elif sentiments_score[2]  > sentiments_score[0]:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Positive**')
    col2.image(positive)
else:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Neutral**')
    col2.image(neutral)



st.markdown("""---""")
st.header("✍🏽User Review")
st.markdown("""---""")

user_review = st.text_input('Feedback in few words:')
st.markdown("""---""")
sia = SentimentIntensityAnalyzer()
scores = sia.polarity_scores(user_review)

sentiments_score = [scores['neg'],scores['neu'],scores['pos']]

st.header("😶Sentiment")
st.markdown("""---""")

if sentiments_score[0]  > sentiments_score[2]:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Negative**')
    col2.image(negative)
elif sentiments_score[2]  > sentiments_score[0]:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Positive**')
    col2.image(positive)
else:
    col1,col2 = st.columns([1,1])
    col1.subheader('**Neutral**')
    col2.image(neutral)