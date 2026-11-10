from sentence_transformers import SentenceTransformer
from vector_store import create_collection

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_query(query):
    return model.encode(query);


def retrive(collection,question):
    
    query_embedding = embed_query(question);

    return collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)


def build_context(retrieved_chunks):
    documents = retrieved_chunks["documents"][0];

    context = "\n\n".join(documents)

    return context;

def test(question,retrived_chunks):
    print("Question:", question)

    for chunk in retrived_chunks["documents"][0]:
        print("\n--- Retrieved Chunk ---")
        print(chunk)
    
    print("Distances:", retrived_chunks["distances"][0]);
    print("IDs:", retrived_chunks["ids"])
    print("Documents:", retrived_chunks["documents"])
    print("Distances:", retrived_chunks["distances"])

# collection = create_collection();
# question = "What is savings?"
# retrived_chunks = retrive(collection, question);
# context = build_context(retrived_chunks)
# print("---- Retrieved Context ----")
# print(context)

# print("Matched IDs:", retrived_chunks["ids"])
# print("Matched documents:", retrived_chunks["documents"])
# print("Distances:", retrived_chunks["distances"])


# test(question,retrived_chunks);
# print("Embedding dimensions:", len(query_embedding))