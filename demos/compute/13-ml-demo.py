# Uses Amazon Comprehend to detect sentiment

import boto3

comprehend = boto3.client('comprehend')
text = "Cloud computing is awesome!"

# Detect the sentiment of the input text
response = comprehend.detect_sentiment(
    Text=text,
    LanguageCode='en'
)

print(response['Sentiment'])