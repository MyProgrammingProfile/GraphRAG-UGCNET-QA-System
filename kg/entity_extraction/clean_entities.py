from pathlib import Path
import re

RAW_DIR = Path("kg/entity_extraction")
CLEAN_DIR = RAW_DIR / "cleaned"
CLEAN_DIR.mkdir(exist_ok=True)

def is_valid_entity(text):
    # remove numbers, symbols, very short tokens
    if len(text) < 3:
        return False
    if re.search(r"\d", text):
        return False
    if text.lower() in {"the", "and", "with", "from", "that"}:
        return False
    return True

for file in RAW_DIR.glob("*_entities.txt"):
    cleaned = set()
    for line in file.read_text(encoding="utf-8").splitlines():
        entity = line.strip().lower()
        entity = re.sub(r"\s+", " ", entity)
        if is_valid_entity(entity):
            cleaned.add(entity)

    output_file = CLEAN_DIR / file.name.replace("_entities", "_cleaned_entities")
    with open(output_file, "w", encoding="utf-8") as f:
        for e in sorted(cleaned):
            f.write(e + "\n")

    print(f"Cleaned: {file.name} → {output_file.name}")

print("Entity cleaning completed.")
