
import sys

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


query = sys.argv[1]

loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

if (index.query(query) == " I don't know."):
    print("Please ask a question about Me")
else:
    print(index.query(query))
