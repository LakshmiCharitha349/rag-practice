from pathlib import Path

# Get the project root directory
def load_document():
    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    file_path = PROJECT_ROOT / "data" / "documents" / "transcripts" / "New recording 1_transcript.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    return document_text, file_path.name