from pypdf import PdfReader

doc = PdfReader("sample_vmware_sop.pdf")

text = "" 

for page in doc.pages:
    text += page.extract_text() 

print(text)    