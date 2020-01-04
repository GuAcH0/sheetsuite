import gspread
from oauth2client.service_account import ServiceAccountCredentials


def gspread_to_list_of_dictionaries(filename):   #what if NO INDEX column given? Need to keep track
    thebiglist = sheet.get_all_records()
    return thebiglist
# or a separate function that looks at the index? Can this be done w/ list of dictionaries? ex. sheet.find('index')


def gspreadauthenticator(filename):
    print('\nImporting...')
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(filename, scope) 
    client = gspread.authorize(creds)
    spreadsheet_name = client.list_spreadsheet_files()[0]['name']
    sheet = client.open(spreadsheet_name).sheet1                   #assumes sheet1
    print('Imported sheet1 from ' + str(spreadsheet_name) + '.')   #sheet1
    return sheet



if __name__ == "__main__":
    #from sheetsuite import init_spreadsheet
    #init_spreadsheet()
    sheet = gspreadauthenticator()
    thebiglist = sheet.get_all_records()
    print(thebiglist[0])
    column_keys = thebiglist[0].keys()    # returns keys, which are actually first row of gspreadsheet
    column_headers = [str.lower(x) for x in column_keys]
    'index' in column_headers   # if not, ask user. if it is, ask user to confirm








