import streamlit as st
import pandas as pd
from PyPDF2 import *

st.header("Upload Page")
text_raw="Test"



#Functions for PDF extraction
def pdf_page_num(pdf_file):
    reader = PdfReader(pdf_file)
    page_num = len(reader.pages)
    return page_num

def clean_pdf(pdf):
    lines = [line for line in pdf.split('\n') if line.strip()]
    return lines

def extract_pdf(pdf_file,s,e):
    reader = PdfFileReader(pdf_file)
    pdftext=[]
    for page in range(s,e):
            content=reader.getPage(page).extract_text()
            pdftext.append(content)
    pdf_text="".join(pdftext)
    pdf_text=clean_pdf(pdf_text)
    pdf_text="".join(pdf_text)
    return pdf_text 
    


#Functions for Showing Text
def show_text(t):
    st.caption("This is the text that has been uploaded")
    st.markdown(t)
    st.caption("Press Process to begin")
    if st.button("Process"):
        text_raw=t

#Function for Keyword Extraction
#def tf_idf(text):


#upload file
with st.expander("Uploading text"):
    st.caption("Upload a paragraph of a journal, research paper, newsletter to get your keywords.")
    text_upload=st.text_input("Enter Text")
    if text_upload:
        show_text(text_upload)
        

with st.expander("Uploading PDF File"):
    st.caption("Upload a PDF file of a journal, research paper, newsletter to get your keywords.")
    uploaded_file = st.file_uploader("Choose a file", "pdf")
    if uploaded_file is not None:
        st.caption("Choose the pages to be process")
        start=st.slider("Start Page",0,pdf_page_num(uploaded_file),3)
        end=st.slider("End Page",0,pdf_page_num(uploaded_file),3)
        if st.button("Confirm Pages"):
            upload_text=extract_pdf(uploaded_file,start,end)
            show_text(upload_text)
        
st.markdown("The Keywords Extracted")


        
        
        


        
    

   
