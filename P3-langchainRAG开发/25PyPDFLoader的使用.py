from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./P3-langchainRAG开发/data/pdf1.pdf",
    mode="page",

    password="itheima"#读pdf2的时候用
    )

# 初始化一个计数器
i = 0
# 使用 lazy_load 方法逐页懒加载 PDF 文档
# 这种方法会返回一个迭代器，有助于节省内存
for doc in loader.lazy_load():
    i+=1
    # 打印分隔符，方便区分每一页的内容
    print("="*20)
    # 打印当前加载的文档页面对象
    print(doc)
    # 打印分隔符和计数器的当前值
    print("="*20,i)
