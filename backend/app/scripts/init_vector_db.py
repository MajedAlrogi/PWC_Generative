from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone


def init_pinecone():
    
    pc = Pinecone(api_key='[Enter API KEY]')

    # Define the index configuration
    index_name = 'dictionary'
    dimension = 768  # Adjust based on your embedding model's output dimension
    metric = 'cosine'

    # Create the index
    if index_name not in pc.list_indexes():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    # Connect to the index
    index = pc.Index(index_name)
    return index

if __name__ == '__main__':
    idx = init_pinecone()
    print(f'Pinecone VectorDB Initialized: {idx}')