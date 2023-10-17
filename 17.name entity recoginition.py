#17Implement a Python program using the SpaCy library to perform Named Entity Recognition (NER) on a given text.
import spacy

def named_entity_recognition(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Iterate over named entities in the text
    for entity in doc.ents:
        print(f"Entity: {entity.text}, Label: {entity.label_}")

text = "Apple is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, software, and online services. It was established on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne. Apple is the world's largest technology company by revenue (totaling $274.5 billion in 2020) and, since January 2021, the world's most valuable company. As of 2021, Apple is the largest publicly traded company in the world by market capitalization. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, the AirPods wireless earbuds, and the HomePod smart speaker. In addition, the company provides software services, such as the macOS operating system for Macintosh computers, the iOS operating system for iPad, iPhone, and iPod Touch, the iPadOS operating system for iPad, and the watchOS operating system for Apple Watch."

named_entity_recognition(text)
