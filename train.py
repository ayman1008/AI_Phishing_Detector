import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Data load karna
# Hum pandas ka use kar rahe hain, jo Excel sheet jaisa kaam karta hai
df = pd.read_csv('phishing_emails.csv')

# 2. Vectorizer setup
# Ye hamare text (words) ko numbers mein badal dega
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Model training
# Logistic Regression hamara "teacher" hai jo pattern seekhega
model = LogisticRegression()
model.fit(X, y)

# 4. Files save karna
# Taaki hum baad mein is "brain" ko app mein use kar sakein
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model successfully train ho gaya aur save ho gaya!")