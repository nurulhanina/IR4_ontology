import streamlit as st
import pandas as pd

#UI stuff
st.markdown("Knowledge Expert Page")

#define database source
sheet_id = "1t7jm8MidWPXJn-gRxatbpPEtJcm-sSygSapt2bPUHwo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df=pd.read_csv(url)
sheet_name1 = "Sheet2"
url1 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name1}"
df1=pd.read_csv(url1)
sheet_name2 = "Sheet3"
url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name2}"
df2=pd.read_csv(url2)

