import gradio as gr
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
os.system('python -m spacy download en_core_web_sm')
import spacy
from spacy import displacy

nltk.download("vader_lexicon")
sid = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")

def multi_analysis(text):
    scores = sentiment_analysis(text)
    pos_tokens, pos_count, html = text_analysis(text)
    return scores, pos_tokens, pos_count, html

def sentiment_analysis(text):
    scores = sid.polarity_scores(text)
    del scores["compound"]
    return scores

def text_analysis(text):
    doc = nlp(text)
    html = displacy.render(doc, style="dep", page=True)
    html = (
        "<div style='max-width:100%; max-height:360px; overflow:auto'>"
        + html
        + "</div>"
    )
    pos_count = {
        "char_count": len(text),
        "token_count": 0,
    }
    pos_tokens = []

    for token in doc:
        pos_tokens.extend([(token.text, token.pos_), (" ", None)])

    return pos_tokens, pos_count, html

demo = gr.Interface(
    fn=multi_analysis,
    inputs=gr.Textbox(placeholder="Enter sentence here..."),
    outputs=["label", "highlight", "json", "html"],
    examples=[
        ["What a beautiful morning for a walk!"],
        ["It was the best of times, it was the worst of times."],
    ],
)

demo.launch()
