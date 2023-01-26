import streamlit as st
import pandas as pd
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
import gspread

#UI Stuff
st.title("Sistem Istilah Dwibahasa")
st.markdown("Search Query")

json_auth='gs_credential.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('json_auth', scope=scope)
client = gspread.authorize(creds)
sheet = client.open('ir4_database')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.get_all_records()
records_df = pd.DataFrame.from_dict(records_data)
# view the top records
#records_df.head()
st.markdown(sheet_instance.cell(col=3,row=2))


