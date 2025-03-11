# ReviewRadar-AI-Review-Assistant

This project is an AI-powered assistant that analyzes and processes reviews. It leverages transformer-based models to perform various tasks such as sentiment analysis, review summarization, fake review detection, and keyword extraction. The project uses Streamlit for a simple user interface and allows for the upload of review files (e.g., CSV, TXT, PDF) for processing.

## Features
- **Sentiment Analysis**: Analyzes the sentiment of reviews (positive or negative).
- **Summarization**: Summarizes long reviews into concise versions.
- **Fake Review Detection**: Identifies potentially fake reviews based on text patterns.
- **Keyword Extraction**: Extracts important keywords from reviews using TF-IDF.
- **Text Generation**: Generates new reviews based on custom prompts using the Falcon-7B model.

## Installation

To get started with this project, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

## Dependencies
streamlit
transformers
torch
pandas
scikit-learn

## Usage
Running the App
Run the Streamlit app (app.py) to start the interface:
```streamlit run app.py```
This will launch a local server where you can interact with the application via your web browser.

## Processing Reviews
Custom Text Generation: You can input a custom prompt to generate reviews using the generate_reviews.py script.
Review Processing: You can process reviews for sentiment analysis, summarization, keyword extraction, and fake review detection using the review_processing.py script.

## Example of Running Review Processing Script
To analyze a CSV file with reviews:
```
import pandas as pd
from review_processing import analyze_sentiment, summarize_reviews, extract_keywords, detect_fake_reviews

# Load your CSV file containing reviews
df = pd.read_csv('reviews.csv')

# Process reviews
df = analyze_sentiment(df)
df = summarize_reviews(df)
df = extract_keywords(df)
df = detect_fake_reviews(df)

# Save the processed data
df.to_csv('processed_reviews.csv', index=False)
```

## How It Works
Text Generation: The generate_reviews.py script uses the Falcon-7B model to generate text based on the input prompt.
Sentiment Analysis: The review_processing.py script uses a pre-trained sentiment analysis model from Hugging Face's transformers library.
Summarization: It uses a transformer-based summarizer to generate concise summaries of long reviews.
Fake Review Detection: The script identifies reviews that may be fake based on length and specific text patterns like overused words (e.g., "amazing").
Keyword Extraction: TF-IDF is used to extract significant keywords from reviews.

## Contributing
Feel free to fork this repository and contribute by creating issues or submitting pull requests for improvements.

## License
This project is licensed under the MIT License.

```
This README gives an overview of your project, explains the installation and usage, and describes how the key features work. You can customize it further as needed!
```


