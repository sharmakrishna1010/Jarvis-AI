import chromadb

chroma_client = chromadb.PersistentClient(path="./.jarvis_memory")

try:
    memory_collection = chroma_client.get_collection(name="conversation_history")
except:
    memory_collection = chroma_client.create_collection(name="conversation_history")

def save_memory(user_query, ai_response, interaction_id):
    memory_chunk = f"User said: {user_query} | Jarvis replied: {ai_response}"
    memory_collection.add(
        documents=[memory_chunk],
        metadatas=[{"role": "conversation"}],
        ids=[f"interaction_{interaction_id}"],
    )


def recall_relevant_memories(current_query):
    results = memory_collection.query(query_texts=[current_query], n_results=2)

    if results["documents"][0]:
        return "\n".join(results["documents"][0])
    return "No relevant memories found."
