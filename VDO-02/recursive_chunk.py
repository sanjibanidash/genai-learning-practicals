from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Hello how are you?

What can I do? Also I need your help.

Please help me."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=1
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print()