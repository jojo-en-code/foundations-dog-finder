import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("dog_db").sheet1

# if os.path.isfile('filepath'):
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('filepath',
#                                                                     ["https://spreadsheets.google.com/feeds", 
#                                                                     "https://www.googleapis.com/auth/spreadsheets", 
#                                                                     "https://www.googleapis.com/auth/drive.file", 
#                                                                     "https://www.googleapis.com/auth/drive"])
# else:
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('./credentials.json',
#                                                                     ["https://spreadsheets.google.com/feeds", 
#                                                                     "https://www.googleapis.com/auth/spreadsheets", 
#                                                                     "https://www.googleapis.com/auth/drive.file", 
#                                                                     "https://www.googleapis.com/auth/drive"])