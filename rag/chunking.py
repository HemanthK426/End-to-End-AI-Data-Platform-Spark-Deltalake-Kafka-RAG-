from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_data(text_data):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text_data)