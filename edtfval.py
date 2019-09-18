import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from edtf_validate.valid_edtf import is_valid


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('py_cred.json', scope)
gc = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = gc.open("Copy of Box 30 - BFMF Metadata - amj").sheet1

# Extract and print all of the values
data = sheet.get_all_values()
headers = data.pop(0)

# Create dataframe from the values, get column date_created, make a list
df = pd.DataFrame(data, columns=headers)
edtf = df.get('date_created')
edtf_list = (list(edtf))

# Loop thru list and validate date_created values
count = 1
for item in edtf_list:
    valitem = is_valid(item)
    count = count + 1
    if valitem == False:
        print(str(count) + "  " + item + "  Invalid")
