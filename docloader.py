from docx import Document

content = Document("NewIID.docx")

text = ""

for para in content.paragraphs :
    text += para.text  + "\n"
    

print(text) 