import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer, PorterStemmer
from nltk.corpus import stopwords
import nltk
from nltk.corpus import stopwords

from fastapi import FastAPI

app = FastAPI()

model = joblib.load('prediction_pipline_svm.json')

stemmer = SnowballStemmer("french")
stop_words = set(stopwords.words('french'))

def preprocess(text_string):
    text_string = text_string.lower() # Convert everything to lower case.
    text_string = re.sub('[^A-Za-z0-9]+', ' ', text_string) # Remove special characters and punctuations
    
    x = text_string.split()
    new_text = []
    
    for word in x:
        if word not in stop_words:
            new_text.append(stemmer.stem(word))
            
    text_string = ' '.join(new_text)
    return text_string

def classify_message(model, message):
	msg = preprocess(message)
	toxicity = ''
	if int(model.predict([msg])[0]) == 1:
		toxicity = 'Non toxic'
	else:
		toxicity = 'Toxic'
	return {'tweet': message, 'toxicity': toxicity}

@app.get('/')
def get_root():
	print("passed first")
	return {'message': 'Welcome to the toxicity analyzer API'}

@app.get('/toxicity_detection_query/')
async def detect_toxicity_query(message: str):
	return classify_message(model, message)

@app.get('/toxicity_detection_path/{message}')
async def detect_toxicity_path(message: str):
	return classify_message(model, message)
