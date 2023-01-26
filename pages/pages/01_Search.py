import streamlit as st
import pandas as pd

#UI Stuff
st.markdown("Search Query")

st.title("Sistem Istilah Dwibahasa")
#st.image("Documents\Jupyter Notebook\FYP\Images\Header.png")

#define database source
sheet_id = "1t7jm8MidWPXJn-gRxatbpPEtJcm-sSygSapt2bPUHwo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df=pd.read_csv(url, keep_default_na=False)
sheet_name1 = "Sheet2"
url1 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name1}"
df1=pd.read_csv(url1, keep_default_na=False)

#define list
eng_word=list(df['EN'])
malay_word=list(df['MY'])
eng_def=list(df['DEF_EN'])
malay_def=list(df['DEF_MY'])
eng_ref=list(df1['EN'])
type0=list(df1['type1'])
type1=list(df1['type2'])
type2=list(df1['type3'])
type3=list(df1['type4'])
type4=list(df1['type5'])
type5=list(df1['type6'])
type6=list(df1['type7'])
type7=list(df1['type8'])
type8=list(df1['type9'])
type9=list(df1['type10'])
sameas0=list(df1['sameas1'])
sameas1=list(df1['sameas2'])
sameas2=list(df1['sameas3'])
sameas3=list(df1['sameas4'])
sameas4=list(df1['sameas5'])

#FUNCTION DECLARATION
def printtext(text_w):
    st.text(text_w)
    
def printwhole():
    st.subheader("English Text")
    st.text(word_search)
    eng_definition="\nDefinition: "+eng_def[count-1]
    st.text(eng_definition)
    
    st.subheader("Malay Translation")
    st.text(malay_word[count-1])
    st.text("Terjemahan: " + malay_def[count-1])
    
    st.subheader("Synonym")
    if sameas0 is not 0:
        printtext(sameas0[count-1])
    if sameas1 is not 0:
        printtext(sameas1[count-1])
    if sameas2 is not 0:
        printtext(sameas2[count-1])
    if sameas3 is not 0:
        printtext(sameas3[count-1])
    if sameas4 is not 0:
        printtext(sameas4[count-1])

    st.subheader("Hierarchy")
    printtext(str(type0[count-1]))
    printtext(str(type1[count-1]))
    printtext(str(type2[count-1]))
    printtext(str(type3[count-1]))
    printtext(str(type4[count-1]))
    printtext(str(type5[count-1]))
    printtext(str(type6[count-1]))
    printtext(str(type7[count-1]))
    printtext(str(type8[count-1]))
    printtext(str(type9[count-1]))
    
#Main Interface
word_search=st.text_input("Enter Text")
if word_search:
    count=0
    for i in eng_word:
        count+=1
        if word_search.lower()==i.lower():
            printwhole()
            break
        else:
            printtext("Word Not Found")
            break
            
