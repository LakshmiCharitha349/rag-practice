from retriver import retrive, build_context, create_collection
from generator import generate_answer

collection = create_collection()

question = "What is the future value of an investment?"

retrieved_chunks = retrive(collection, question)
context = build_context(retrieved_chunks)

answer = generate_answer(question, context)

print("CONTEXT SENT TO QWEN:")
print(context)

print("\nAnswer:", answer)