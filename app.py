import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    # a.
    text = text.lower()
    # b.
    text = nltk.word_tokenize(text)
    # c.
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    # d.
    from nltk.corpus import stopwords
    stopwords.words('english')

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # e.
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/ SMS Spam Classifier")


input_sms = st.text_input('Enter The Message')
if st.button('Predict'):
    #1.preprocess
    transformed_sms = transform_text(input_sms)
    #2.vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. Predict
    result = model.predict(vector_input)[0]
    #4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
