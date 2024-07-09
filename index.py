import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)

# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ["OPENAI_API_KEY"] = "your key here"

index = None


def initialize_index():
    global index
    index_dir = "./.index"
    
    storage_context = StorageContext.from_defaults(persist_dir=index_dir)
    
    if os.path.exists(index_dir):
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader("./documents").load_data()
        index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
        )
        storage_context.persist(index_dir)