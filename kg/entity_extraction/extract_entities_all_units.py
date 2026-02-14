import spacy
from pathlib import Path

# Load SciSpacy model
nlp = spacy.load("en_core_sci_sm")

BASE_CORPUS = Path("corpus")
OUTPUT_DIR = Path("kg/entity_extraction")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_entities_from_folder(input_folder, unit_id):
    entities = set()
    for txt_file in input_folder.glob("*.txt"):
        text = txt_file.read_text(encoding="utf-8", errors="ignore")
        doc = nlp(text)
        for ent in doc.ents:
            # keep entities longer than 2 characters
            if len(ent.text.strip()) > 2:
                entities.add(ent.text.strip())
    return sorted(entities)

for section in ["textbooks", "reviews"]:
    section_path = BASE_CORPUS / section
    for unit_folder in section_path.iterdir():
        if unit_folder.is_dir():
            unit_id = unit_folder.name
            print(f"Processing {section.upper()} — {unit_id}")
            entities = extract_entities_from_folder(unit_folder, unit_id)
            output_file = OUTPUT_DIR / f"{unit_id}_{section}_entities.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for e in entities:
                    f.write(e + "\n")

print("Entity extraction completed for all units.")
