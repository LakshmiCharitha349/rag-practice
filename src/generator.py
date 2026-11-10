from ollama import chat

def generate_answer(question, context):
    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": """
                You are a question-answering assistant.

                Follow these rules:
                1. Answer only using the provided context.
                2. Do not assume, calculate, or invent missing information.
                3. Preserve exact numbers, percentages, dates, and units.
                4. If the context is ambiguous or contradictory,
                explicitly mention that.
                5. If the answer cannot be established from the context,
                say you don't have enough information.
                6. use nice words and use emojis if needed
                """
               },
            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {question}
                """
            }
        ]
    )

    return response.message.content