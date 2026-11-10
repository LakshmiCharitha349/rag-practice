from pathlib import Path
from loader import load_document

def chunker(document_text):
    chunk_size = 200;
    overlap = 50;

    words = document_text.split();
    chunks = [];
    step_size = chunk_size - overlap;

    for i in range(0, len(words), step_size):
        
        chunk = words[i: i+(chunk_size)];
        chunks.append(chunk);

    return chunks;

# document_text, file_name = load_document();
# chunks = chunker(data);

# print("Total chunks : ", len(chunks));

# for i in range(0, len(chunks)):
#     print("chunk",i , "::", chunks[i]);