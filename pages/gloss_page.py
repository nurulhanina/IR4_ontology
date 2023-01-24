import streamlit as st
import pandas as pd

st.markdown("Glossary Page")

#define database source
sheet_id = "1t7jm8MidWPXJn-gRxatbpPEtJcm-sSygSapt2bPUHwo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df=pd.read_csv(url)

df=df.dropna(how='all')
gloss=list(df['EN'])

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l_alpha=[]

for i in range(len(alpha)):
    l=[]
    for j in gloss:
        j=str(j)
        if j is not None:
            if j[0].isdigit():
                continue
            if j[0].lower()==alpha[i]:
                l.append(j)
    l_alpha.append(l)
    


def gloss_column(ij):
    
    l=l_alpha[ij]
    if l:gloss_err(ij)
    else:st.write("There is no terminology that starts with this letter")
          
def gloss_err(i):
    l=l_alpha[i]
    url="https://www.google.com/"  #for testing purpose
    
    colms=st.columns((1,2,1))
    field=["No.","Terminology","Search"]
    
    for col, field_Name in zip(colms, field):
        col.write(field_Name)
        
    for x, idx in enumerate(l):
        col1,col2,col3=st.columns((1,2,1))
        col1.write(x)
        col2.write(l[x])
        button="Search" 
        button_phold=col3.empty()
        do_action=button_phold.button(button,key=x+(i*1000))
        if do_action:
            webbrowser.open_new_tab(url)
            button_phold.empty()  
    
with st.expander("A Glossary"):
    st.write("Letter A")
    gloss_column(0)
    
with st.expander("B Glossary"):
    st.write("Letter B")
    gloss_column(1)
    
with st.expander("C Glossary"):
    st.write("Letter C")
    gloss_column(2)
    
with st.expander("D Glossary"):
    gloss_column(3)
    
with st.expander("E Glossary"):
    gloss_column(4)
    
with st.expander("F Glossary"):
    gloss_column(5)
    
with st.expander("G Glossary"):
    gloss_column(6)
    
with st.expander("H Glossary"):
    gloss_column(7)

with st.expander("I Glossary"):
    gloss_column(8)
    
with st.expander("J Glossary"):
    gloss_column(9)
    
with st.expander("K Glossary"):
    gloss_column(10)
    
with st.expander("L Glossary"):
    st.write("Letter L")
    gloss_column(11)
    
with st.expander("M Glossary"):
    st.write("Letter M")
    gloss_column(12)
    
with st.expander("N Glossary"):
    st.write("Letter N")
    gloss_column(13)
    
with st.expander("O Glossary"):
    st.write("Letter O")
    gloss_column(14)
    
with st.expander("P Glossary"):
    st.write("Letter P")
    gloss_column(15)
    
with st.expander("Q Glossary"):
    st.write("Letter Q")
    gloss_column(16)
    
with st.expander("R Glossary"):
    st.write("Letter R")
    gloss_column(17)

with st.expander("S Glossary"):
    st.write("Letter S")
    gloss_column(18)
    
with st.expander("T Glossary"):
    st.write("Letter T")
    gloss_column(19)
    
with st.expander("U Glossary"):
    st.write("Letter U")
    gloss_column(20)
    
with st.expander("V Glossary"):
    st.write("Letter V")
    gloss_column(21)
    
with st.expander("W Glossary"):
    st.write("Letter W")
    gloss_column(22)
        
with st.expander("X Glossary"):
    st.write("Letter X")
    gloss_column(23)
    
with st.expander("Y Glossary"):
    st.write("Letter Y")
    gloss_column(24)
    
with st.expander("Z Glossary"):
    st.write("Letter Z")
    gloss_column(25)
    
