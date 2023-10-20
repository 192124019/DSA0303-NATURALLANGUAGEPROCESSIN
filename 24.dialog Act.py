#24Create a python program that recognizes dialog acts in a given dialog or conversation.
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a list of dialog acts and their corresponding keywords
dialog_acts = {
    "Greeting": ["hello", "hi", "hey"],
    "Request": ["please", "can you", "would you", "tell me", "give me"],
    "Statement": ["I think", "I believe", "in my opinion"],
    "Question": ["what", "how", "why", "where", "when", "who"]
}

def recognize_dialog_act(text):
    doc = nlp(text)
    for act, keywords in dialog_acts.items():
        for keyword in keywords:
            if keyword in text.lower():
                return act
    return "Other"

# Example conversation
conversation = [
    "Hello! How are you doing?",
    "Can you please pass me the salt?",
    "I believe this movie is great.",
    "What time is the meeting?",
    "Tell me more about your project."
]

for utterance in conversation:
    dialog_act = recognize_dialog_act(utterance)
    print(f"Utterance: '{utterance}' -> Dialog Act: {dialog_act}")
