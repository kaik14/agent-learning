# 导入 PromptTemplate 类
# PromptTemplate 用来创建带变量的提示词模板
from langchain_core.prompts import PromptTemplate


# 创建一个 Prompt 模板
# from_template() 会自动识别 {} 里的变量
template = PromptTemplate.from_template(
    "我的邻居是: {lastname}, 最喜欢: {hobby}"
)


# ================================
# 第一种方式：使用 format()
# ================================

# format() 会直接把变量填充到模板中
# 并返回一个普通的字符串 (str)
res = template.format(
    lastname="张大明",
    hobby="钓鱼"
)

# 打印生成的字符串以及它的类型
print(res, type(res))


# ================================
# 第二种方式：使用 invoke()
# ================================

# invoke() 是 LangChain 统一的调用方式
# 需要传入一个字典作为输入
res2 = template.invoke({
    "lastname": "周杰伦",
    "hobby": "唱歌"
})

# invoke() 返回的不是字符串
# 而是 LangChain 的 PromptValue 对象
print(res2, type(res2))


# ================================
# 如果想把 invoke() 的结果变成字符串
# ================================

# 需要调用 to_string()
print(res2.to_string())