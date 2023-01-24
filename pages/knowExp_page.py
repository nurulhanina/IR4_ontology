import streamlit as st
import pandas as pd

#UI stuff
st.markdown("Knowledge Expert Page")

path='C:/Users/Nurul_Hanina/Documents/Jupyter Notebook/FYP/Database/'

#define database source - IR4 Database
url = f"{path}IRword.xlsx"
df=pd.read_csv(url)
#define database source - Ontology
url1 = f"{path}newIRontology.xlsx"
df1=pd.read_csv(url1)
#define database source - Knowledge Expert
url2 = f"{path}IRnewterm.xlsx"
df1=pd.read_csv(url2)

#define list - IR4 Database
eng_word=list(df['EN'])
malay_word=list(df['MY'])
eng_def=list(df['DEF_EN'])
malay_def=list(df['DEF_MY'])
#define list - Ontology
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
sameas1=list(df1['sameas1'])
sameas2=list(df1['sameas1'])
sameas3=list(df1['sameas1'])
sameas4=list(df1['sameas1'])

#define list - Knowledge Expert
newword=list(df2['new'])

st.subheader("What would you like to do?")

classType=["Additive Manufacturing", "Augmented Reality","Autonomous Robots","Big Data","Cloud Computing", "Cyber Physical System","Internet of Service", "Internet of Things","Simulation","Other"]

classadded=["","","","","","","","","",""]
sameas=["","","","",""]

option = st.selectbox(
    'Which type of terminology you would like to enter?',
    ('New Entry', 'Automated Entry'))

st.write('You selected:', option)


def showAll(eng_term,eng_def,my_term,my_def,syn,cT):
    
    st.subheader("English Text")
    st.text("English Term: "+ eng_term)
    
    
    st.text("English Definition: " + eng_def)
    
    st.subheader("Malay Translation")

    st.text("Malay Term: " + my_term)
    
    st.text("Malay Definition: " + my_def)
    
    st.subheader("Synonym")
    st.text(syn)

    st.subheader("Hierarchy")
    st.text(cT)

def write_hierarchy():
    add_man = st.checkbox(classType[0])
    if add_man:
             classadded[0]="Additive Manufacturing"
    aug_real = st.checkbox(classType[1])
    if aug_real:
             classadded[1]="Augmented Reality"
    aut_rob = st.checkbox(classType[2])
    if aut_rob:
             classadded[2]="Autonomous Robots"
    big_data = st.checkbox(classType[3])
    if big_data:
             classadded[3]="Big Data"
    cl_comp = st.checkbox(classType[4])
    if cl_comp:
             classadded[4]="Cloud Computing"
    cps = st.checkbox(classType[5])
    if cps:
             classadded[5]="Cyber Physical System"
    ios = st.checkbox(classType[6])
    if ios:
             classadded[6]="Internet of Service"
    iot = st.checkbox(classType[7])
    if iot:
             classadded[7]="Internet of Things"
    sim = st.checkbox(classType[8])
    if sim:
             classadded[8]="Simulation"
    other = st.checkbox(classType[9])
    if other:
             classadded[9]="Other"
count=0
if option is "New Entry":
    
    st.subheader("English Text")
    new_word=st.text_input("Enter New Terminology",key=count)
    count+=1
    
    new_def=st.text_input("Enter Definition",key=count)
    count+=1
    
    st.subheader("Malay Translation")
    
    with st.expander("Malay Translation (Terminology)"):
        st.write("Terminologi") #To add MT model
    
    new_my=st.text_input("Enter Malay Translation",key=count)
    count+=1
    
    with st.expander("Malay Translation (Definition"):
        st.write("Definisi") #To add MT model
        
    def_my=st.text_input("Enter Definition in Malay",key=count)
    
    new_class=st.selectbox('What is the category this terminology belong to?', classType)
    
    new_syn="Test"
             
    write_hierarchy()
    
    if st.button("Show"):
        showAll(new_word, new_def, new_my, def_my, new_syn,new_class) 
        

elif option is "Automated Entry":
    
    count_upd=0
    st.subheader("English Text")
    upd_word=st.text_input("Enter Terminology to Update",key=count_upd)
    count_upd+=1
             
    write_hierarchy()
    
    if upd_word:
        showAll(upd_word,"hehe","ehehe","ehehe","ehhee","eheh")


    
    
    
    
    