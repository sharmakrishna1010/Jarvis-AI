import chromadb
import datetime

chroma_client = chromadb.PersistentClient(path="./.jarvis_memory")

def get_conversation_history():
    try:
        return chroma_client.get_collection(name="conversation_history")
    except:
        return chroma_client.create_collection(name="conversation_history")

def get_preference():
    try:
        return chroma_client.get_collection(name="preference")
    except:
        return chroma_client.create_collection(name="preference")

memory_collection = get_conversation_history()
preference_collection = get_preference()

def save_memory(user_query, ai_response, interaction_id):
    readable_time = datetime.datetime.fromtimestamp(float(interaction_id)).strftime('%Y-%m-%d %H:%M:%S')
    memory_chunk = f"[{readable_time}] User said: {user_query} | Jarvis replied: {ai_response}"
    memory_collection.add(
        documents=[memory_chunk],
        metadatas=[{"role": "conversation"}],
        ids=[f"interaction_{interaction_id}"],
    )

def save_preference(key, value, updated_at=None):
    if updated_at is None:
        updated_at = str(datetime.datetime.now().timestamp())
    
    existing = preference_collection.get(where={"key": key})
    if existing["ids"]:
        preference_collection.update(
            ids=existing["ids"],
            metadatas=[{"key": key, "value": str(value), "updated_at": str(updated_at)} for _ in existing["ids"]],
            documents=[f"{key} = {value}" for _ in existing["ids"]]
        )
    else:
        preference_collection.add(
            documents=[f"{key} = {value}"],
            metadatas=[{"key": key, "value": str(value), "updated_at": str(updated_at)}],
            ids=[f"pref_{key}_{updated_at}"]
        )

def delete_preference(key):
    existing = preference_collection.get(where={"key": key})
    if existing["ids"]:
        preference_collection.delete(ids=existing["ids"])
        return True
    return False

def recall_preference_memories():
    existing = preference_collection.get()
    if existing["documents"]:
        return "\n".join(existing["documents"])
    return "No relevant preferences found."

def recall_relevant_memories(current_query):
    results = memory_collection.query(query_texts=[current_query], n_results=2)
    if results["documents"][0]:
        return "\n".join(results["documents"][0])
    return "No relevant memories found."