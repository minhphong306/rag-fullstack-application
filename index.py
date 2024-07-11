import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from dotenv import load_dotenv

load_dotenv()
# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

index = None


def initialize_index():
    global index
    index_dir = "./.index"
    

    
    if os.path.exists(index_dir):
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context)
    else:
        storage_context = StorageContext.from_defaults()
        documents = SimpleDirectoryReader("./documents").load_data()
        index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
        )

        storage_context.persist(index_dir)

def get_index():
    global index
    return index