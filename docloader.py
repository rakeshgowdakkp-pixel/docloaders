from docx import Document

content = Document("Sample_word.docx")

text = ""

for para in content.paragraphs :
    text += para.text  + "\n"
    


print(text) 
