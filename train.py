import pandas as pd
import pickle
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# download stopwords
nltk.download('stopwords')

# load dataset
data = pd.read_csv(
    "spam.csv",
    encoding='latin-1'
)

# keep only required columns
data = data[['v1', 'v2']]

# rename columns
data.columns = ['label', 'message']

# convert labels into numbers
data['label'] = data['label'].map({
    'ham': 0,
    'spam': 1
})

# remove missing values
data.dropna(inplace=True)

# preprocessing
ps = PorterStemmer()

def clean_text(text):

    text = str(text).lower()

    words = text.split()

    filtered_words = []

    for word in words:
        if word not in stopwords.words('english'):
            filtered_words.append(ps.stem(word))

    return " ".join(filtered_words)

# apply preprocessing
data['message'] = data['message'].apply(clean_text)

# feature extraction
cv = CountVectorizer()

X = cv.fit_transform(data['message']).toarray()

y = data['label']

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# train model
model = MultinomialNB()

model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(cv, open("vectorizer.pkl", "wb"))

print("Model and Vectorizer Saved Successfully")