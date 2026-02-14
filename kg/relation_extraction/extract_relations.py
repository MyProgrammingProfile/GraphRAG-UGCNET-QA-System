import spacy
from pathlib import Path

nlp = spacy.load("en_core_sci_sm")

INPUT_DIR = Path("corpus")
OUTPUT_FILE = Path("kg/relation_extraction/relations.txt")
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

RELATION_PATTERNS = [
    ("is a", "is_a"),
    ("part of", "part_of"),
    ("occurs in", "occurs_in"),
    ("produces", "produces"),
    ("regulates", "regulates"),
    ("prevents", "prevents")
]

relations = set()

def extract_relations_from_text(text):
    doc = nlp(text.lower())
    for sent in doc.sents:
        sent_text = sent.text
        for phrase, rel in RELATION_PATTERNS:
            if phrase in sent_text:
                parts = sent_text.split(phrase)
                if len(parts) == 2:
                    head = parts[0].strip()
                    tail = parts[1].strip()
                    if len(head) > 2 and len(tail) > 2:
                        relations.add((head, rel, tail))

for section in ["textbooks", "reviews"]:
    for unit_folder in (INPUT_DIR / section).iterdir():
        if unit_folder.is_dir():
            for txt_file in unit_folder.glob("*.txt"):
                text = txt_file.read_text(encoding="utf-8", errors="ignore")
                extract_relations_from_text(text)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for h, r, t in sorted(relations):
        f.write(f"{h} | {r} | {t}\n")

print(f"Extracted {len(relations)} relations.")
