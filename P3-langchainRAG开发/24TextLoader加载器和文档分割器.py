from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./P3-langchainRAG开发/data/Python基础语法.txt",encoding = "utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,#分段的最大字符数
    chunk_overlap=50,#分段之间允许字符重叠数
    separators=["\n\n", "\n","。","!","？",".","!","?"," ",""],
    length_function=len,#统计字符的依据函数
)

split_docs = splitter.split_documents(docs)
print(len(split_docs))

for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)
