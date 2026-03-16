from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./P3-langchainRAG开发/data/stu.csv",
    csv_args={
        "delimiter": ",", #指定分隔符
        "quotechar": '"', #指定带有分隔符的文本是包围是什么引号
        "fieldnames": ["name", "age", "gender","hobby"]#如果数据原本有表头 就不用了
    },
    encoding = "utf-8",
)

#批量加载

# documents = loader.load()

# for document in documents:
#     print(document)

#懒加载
for document in loader.lazy_load():
    print(document)