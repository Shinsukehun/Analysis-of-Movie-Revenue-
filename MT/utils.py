import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def summarize_prompt(prompt):
    doc = nlp(prompt)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    summarized = " ".join(keywords[:6]) if keywords else "N/A"
    return summarized.capitalize()