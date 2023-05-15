from json import loads
import spacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

def summarizer(text):
    nltk.download('punkt')
    nltk.download('stopwords')
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from collections import Counter

    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Extract the top 5 most common words as keywords
    keywords = [word for word, count in Counter(filtered_words).most_common(5)]

    # Extract the sentences that contain the keywords
    relevant_sentences = []
    for sentence in sentences:
        for keyword in keywords:
            if keyword.lower() in sentence.lower():
                relevant_sentences.append(sentence)

    # Generate the abstract from the relevant sentences
    abstract = ' '.join(relevant_sentences)
    return(abstract)




def semanticsearch(docs, query):
    # Load the pre-trained spacy model
    nlp = spacy.load("en_core_web_lg")
    # Process the query using the spacy model
    query_doc = nlp(query)

    # Iterate through the documents and calculate their similarity to the query
    scores = []
    for doc in docs:
        doc = nlp(doc)
        score = query_doc.similarity(doc)
        scores.append(score)

    # Retrieve the top N documents based on their similarity scores
    N = 5
    top_docs = [doc for _, doc in sorted(zip(scores, docs), reverse=True)[:N]]
    return (f"este es el resultado de la busqueda semantik {top_docs}")


def aiselectfromlist(tabla, query):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(query)
    for name, description in tabla.items():
        if nlp(description).similarity(doc) > 0.2:
            return name
    return "Lo siento, no entiendo la pregunta. Por favor, inténtelo de nuevo."
