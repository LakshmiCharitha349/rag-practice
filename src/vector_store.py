import chromadb
from loader import load_document
from chunker import chunker
from embedder import embedder


def create_collection():
    
    # Create a persistent ChromaDB client. Stores the database locally on disk.
    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    # Create a collection
    collection = client.get_or_create_collection(
        name="finance_documents"
    );

    print("finanace_documents collection created succesfully");
    return collection;


def store_chunks(collection, chunks, embeddings, file_name):
    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[" ".join(chunk) for chunk in chunks],
        embeddings=embeddings.tolist(),
        metadatas=[
            {"source": file_name}
            for _ in chunks
        ]
    )

    print("Total stored chunks:", collection.count());


def get_data(collection):
    result = collection.get(
    ids=["chunk_0"],
    include=["documents", "metadatas"]
    )

    print(result)



# document_text, file_name = load_document();
# chunks = chunker(document_text);
# embeddings = embedder(chunks);

# collection = create_collection();
# store_chunks(collection, chunks,embeddings, file_name);
# print("file name ::" + file_name);

# get_data(collection);