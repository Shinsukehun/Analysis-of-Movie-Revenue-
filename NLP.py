import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer, WordNetLemmatizer

# # Sample text
# text = "Natural Language Processing is amazing! NLP allows computers to understand human language."

# # Tokenization
# words = word_tokenize(text)
# sentences = sent_tokenize(text)

# # Removing stopwords
# stop_words = set(stopwords.words('english'))
# filtered_words = [word for word in words if word.lower() not in stop_words]

# # Stemming & Lemmatization
# stemmer = PorterStemmer()
# lemmatizer = WordNetLemmatizer()
# stemmed_words = [stemmer.stem(word) for word in filtered_words]
# lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# print(f"Original Words: {words}")
# print(f"Filtered Words: {filtered_words}")
# print(f"Stemmed Words: {stemmed_words}")
# print(f"Lemmatized Words: {lemmatized_words}")
from sklearn.feature_extraction.text import CountVectorizer

documents = ["I love programming", "Python is great", "I love Python"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)

print(tfidf_vectorizer.get_feature_names_out())
print(X_tfidf.toarray())

