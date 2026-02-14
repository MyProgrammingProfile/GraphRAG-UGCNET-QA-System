import spacy

nlp = spacy.load("en_core_web_sm")

BIO_KEYWORDS = [
    "bryophyte", "moss", "liverwort", "chloroplast", "thylakoid", "stroma",
    "photosynthesis", "calvin", "light reaction", "sporophyte", "gametophyte",
    "rhizoid", "algae", "fungi", "pteridophyte", "gymnosperm", "angiosperm"
]

def extract_entities_from_chunks(docs):
    text = " ".join([d.page_content for d in docs]).lower()
    found = []

    for key in BIO_KEYWORDS:
        if key in text:
            found.append(key.capitalize())

    # fallback to spaCy NER but filter numbers & dates
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE", "PERSON", "DATE", "CARDINAL"]:
            continue
        if len(ent.text) > 3 and not ent.text.isdigit():
            found.append(ent.text)

    return list(set(found))
