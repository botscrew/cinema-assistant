import uuid

from pinecone import Pinecone

from config import PINECONE_API_KEY
from openaiClient import create_embedding

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("cinema-bot")


def save_embedding(text, embedding):
    index.upsert(vectors=[
        {
            "id": uuid.uuid4().hex,
            "values": embedding,
            "metadata": {"text": text}
        }
    ])

def find_top_k(embedding, top_k = 3):
    result = []
    for match in index.query(vector = embedding, top_k=top_k, include_metadata=True, include_values=False).get('matches'):
        result.append(match.get('metadata').get('text'))
    return result


