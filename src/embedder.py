from sentence_transformers import SentenceTransformer
from loader import load_document
from chunker import chunker

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embedder(chunks):

    texts = [" ".join(chunk) for chunk in chunks]; # batch rocessing
    return model.encode(texts);

    
data, file_name = load_document();
chunks = chunker(data);
embedded_data = embedder(chunks);

print("Total chunksembeddings : ", len(embedded_data));
print("Embedding shape:", embedded_data.shape) #gives total chunks, and its embedding length

# for i in range(0, len(embedded_data)):
#     print("chunk",i , "::", embedded_data[i]);

# print("Embedding:", embedding)
# print("Dimensions:", len(embedding))