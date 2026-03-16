from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings(model="text-embedding-v1") #括号里面为空的话默认也是v1模型

print(model.embed_query("你好"))#单次转换
print(model.aembed_documents(["我喜欢你","你好"]))#输出的是文本向量