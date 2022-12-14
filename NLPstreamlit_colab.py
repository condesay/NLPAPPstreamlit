# -*- coding: utf-8 -*-
"""AppNLPBien.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-5mqeCWt8CpkDY8S0OVfBtdTTSSE0Uxr

<br>
Description<br>
Application NLP traitant:<br>
+ Tokenization & Lemmatization utilisant Spacy<br>
+ Named Entity Recognition(NER) utilisant SpaCy<br>
+ Sentiment Analysis utilisant TextBlob<br>
+ Document/Text Resu,é utilisant Gensim/Sumy<br>
Construit avec  Streamlit Framework, un très bon framework pour les projets ML and NLP avec peu de codes et facile à comprendre.<br>

Probleme à resoudre:
Gensim summarization et sentiment analysis donné directement positif ou negatif aulieu de polarité et subjectivité
"""

!pip install streamlit
import streamlit as st
import os

"""NLP Pkgs

Sumy Summary Pkg
"""

!pip install sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re

"""Function for Sumy Summarization"""

# Commented out IPython magic to ensure Python compatibility.
# 
# %%writefile app.py
# # Core Pkgs
# import streamlit as st
# import os
# import re
# 
# # NLP Pkgs
# from textblob import TextBlob
# import spacy
# from gensim.summarization.summarizer import summarize
# import nltk
# nltk.download('punkt')
# 
# # Sumy Summary Pkg
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer
# # function gensim summarization
# def summarize(doc):
#    doc = re.sub(r'\n|\r', ' ', doc)
#    doc = re.sub(r' +', ' ', doc)
#    doc = doc.strip()
#    result_gen= summarize(doc,word_count=75, split=False)
#    return result_gen
# # Function for Sumy Summarization
# def sumy_summarizer(docx):
# 	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
# 	lex_summarizer = LexRankSummarizer()
# 	summary = lex_summarizer(parser.document,3)
# 	summary_list = [str(sentence) for sentence in summary]
# 	result = ' '.join(summary_list)
# 	return result
# 
# # Function to Analyse Tokens and Lemma
# @st.cache
# def text_analyzer(my_text):
# 	nlp = spacy.load('en_core_web_sm')
# 	docx = nlp(my_text)
# 	# tokens = [ token.text for token in docx]
# 	allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
# 	return allData
# 
# # Function For Extracting Entities
# @st.cache
# def entity_analyzer(my_text):
# 	nlp = spacy.load('en_core_web_sm')
# 	docx = nlp(my_text)
# 	tokens = [ token.text for token in docx]
# 	entities = [(entity.text,entity.label_)for entity in docx.ents]
# 	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
# 	return allData
# 
# 
# def main():
# 	""" NLP Based App with Streamlit """
# 
# 	# Title
# 	st.title(" NLP Application")
# 	st.subheader("Natural Language Processing Application")
# 	st.markdown("""
#     	#### Description
#     	+ C'est une application de Natural Language Processing(NLP) Basée sur les taches simples u traitement du language Naturel, entre autres nous avons: 
#     	Tokenization , Lemmatization, Named Entity Recognition (NER), Sentiment Analysis, Text Summarization. 
#     	""")
# 
# 	# Summarization
# 	if st.checkbox("Get the summary of your text"):
# 		st.subheader("Summarize Your Text")
# 
# 		message = st.text_area("Enter Text","Type Here....")
# 		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
# 		if st.button("Summarize"):
# 			if summary_options == 'sumy':
# 				st.text("Using Sumy Summarizer ..")
# 				summary_result = sumy_summarizer(message)
# 			elif summary_options == 'gensim':
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)
# 			else:
# 				st.warning("Using Default Summarizer")
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)
# 			st.success(summary_result)
#   
# 	# Sentiment Analysis
# 	if st.checkbox("Get the Sentiment Score of your text"):
# 		st.subheader("Identify Sentiment in your Text")
# 
# 		message = st.text_area("Enter Text","Type Here...")
# 		if st.button("Analyze"):
# 			blob = TextBlob(message)
# 			result_sentiment = blob.sentiment
# 			st.success(result_sentiment)
# 
# 	# Entity Extraction
# 	if st.checkbox("Get the Named Entities of your text"):
# 		st.subheader("Identify Entities in your text")
# 
# 		message = st.text_area("Enter Text","Type Here..")
# 		if st.button("Extract"):
# 			entity_result = entity_analyzer(message)
# 			st.json(entity_result)
# 
# 	# Tokenization 
# 	if st.checkbox("Get the Tokens and Lemma of text"):
# 		st.subheader("Tokenize Your Text")
# 
# 		message = st.text_area("Enter Text","Type Here.")
# 		if st.button("Analyze"):
# 			nlp_result = text_analyzer(message)
# 			st.json(nlp_result)
# 
#   # Translate 
# 	if st.checkbox("Get the translation of your text"):
# 		st.subheader(" Translate  your Text")
# 
# 		message = st.text_area("Enter Text","Type Here...")
# 		if st.button("Translate"):
# 			blobt = TextBlob(message)
# 			result = blobt.translate(from_lang="fr",to="en")
# 			st.success(result) 
#  
# 
# 	st.sidebar.subheader("Info de l'App")
# 	st.sidebar.text("NLP Application.")
# 	st.sidebar.info("Permet de trouver le sentiment score, tokens , lemma, Named Entities et Resumé  du texte.!")
# 	
# 
# if __name__ == '__main__':
# 	main()
# 
#

!npm install localtunnel

"""Function to Analyse Tokens and Lemma"""

!streamlit run /content/app.py &>/content/logs.txt &

!npx localtunnel --port 8501