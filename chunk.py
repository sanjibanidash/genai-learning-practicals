from langchain_text_splitters import CharacterTextSplitter

text = "Hello how are you?\n\nWhat can I do? Also I need your help.\n\nPlease help me."

splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
    separator="\n\n"
)

chunks = splitter.split_text(text)

for i in chunks:
    print(i)
    print()