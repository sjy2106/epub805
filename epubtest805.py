import nltk
from ebooklib import epub
import ebooklib
import os
input_path="/Users/test/test805"
test_wd=[]
book=epub.read_epub(os.path.join(input_path,'test.epub'))
for doc in book.get_items():
    doc_content=str(doc.content)
    for w in nltk.word_tokenize(doc_content):
        test_wd.append(w.lower())
fo = open("test805.txt","w")
for t in test_wd:
    fo.write(t + ",")
fo.close()
