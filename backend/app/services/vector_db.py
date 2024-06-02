from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
pc = Pinecone(api_key='[ENTER API KEY]')
index_name = "dictionary"
index = pc.Index(index_name)

model = SentenceTransformer('all-mpnet-base-v2')

def get_embedding(text):
    return model.encode(text).tolist()

def query_vector_db(query_text, top_k_entries=3):
    query_vector = get_embedding(query_text)
    results = index.query(vector=query_vector, top_k=top_k_entries)

    # Extract line numbers from the results
    line_numbers = [int(match['id']) for match in results['matches']]

    # Read the lines from the text file
    with open("./app/assets/page_texts.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Retrieve the corresponding lines
    retrieved_lines = [lines[line_number].strip() for line_number in line_numbers]

    return retrieved_lines