from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
embed_model = FastEmbedEmbeddings(model_name="BAAI/bge-base-en-v1.5")

def get_retriever():
    urls = [
        "https://theindosphere.com/history/kashmir-origins-history-invasion/",
        "https://www.kashmirtourpackage.org/history-of-kashmir.html",
        "https://www.britannica.com/place/Jammu-and-Kashmir/Government-and-society",
        "https://www.cambridge.org/core/journals/modern-intellectual-history/article/pure-kashmir-nature-freedom-and-counternationalism/E4562347F59C96D93E6257ECEAB9DB9D",
    ]

    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]
    print(f"len of documents :{len(docs_list)}")

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=512, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)
    print(f"length of document chunks generated :{len(doc_splits)}")

    vectorstore = Chroma.from_documents(documents=doc_splits,
                                        embedding=embed_model,
                                        collection_name="local-rag")

    return vectorstore.as_retriever(search_kwargs={"k":2})