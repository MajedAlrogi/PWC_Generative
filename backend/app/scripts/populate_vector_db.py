from pinecone import Pinecone
from sentence_transformers import SentenceTransformer


# Initialize Pinecone
pc = Pinecone(api_key='[ENTER API KEY]')
index_name = "dictionary"

# Connect to the index
index = pc.Index(index_name)

model = SentenceTransformer('all-mpnet-base-v2')

def get_embedding(text):
    return model.encode(text).tolist()
    

def populate_vector_db(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    vectors = []
    ids = []

    for i, line in enumerate(lines):
        embedding = get_embedding(line.strip())
        vectors.append(embedding)
        ids.append(str(i))  # Store line number as string
    
    # Upsert vectors into Pinecone index
    index.upsert(vectors=zip(ids, vectors))

if __name__ == "__main__":
    file_path = "../assets/page_texts.txt"  # Path to your text file
    populate_vector_db(file_path)
