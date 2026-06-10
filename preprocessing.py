from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()

    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return " ".join(filtered_words)


def tokenize_text(text):

    return text.split()

def lemmatize_tokens(tokens):

    lemmas = []

    for token in tokens:
        lemmas.append(
            lemmatizer.lemmatize(token)
        )

    return lemmas
def preprocess_text(text):

    cleaned = clean_text(text)

    tokens = tokenize_text(cleaned)

    lemmas = lemmatize_tokens(tokens)

    return lemmas