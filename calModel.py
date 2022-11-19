from __future__ import print_function

import os.path
import google.auth
import pickle
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
url = 'https://github.com/Amharc-Hash/Naning_API/blob/main/healt.pkl?raw=true'
# req = requests.get(url)

# The ID and range of a sample spreadsheet.
SERVICE_ACCOUNT_FILE = 'keys.json'
SAMPLE_SPREADSHEET_ID = '1Hvnnmf77f9M_LnxM1_6gkGXUcTbBKkgoj01lDC75NV8'
SAMPLE_RANGE_NAME = 'Revalue!A2:K'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


###########################################

    # creds, _ = google.auth.default()
    # pylint: disable=maybe-no-member
    try:

        values = [
                      ['K']
                  ]
        body = {
            'values': values
        }
        value_input_option = "USER_ENTERED"
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Revalue!K2',
            valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error



if __name__ == '__main__':
    main()
    # print(req)

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials


# scopes = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     # 'https://www.googleapis.com/auth/drive'
# ]

# creds = ServiceAccountCredentials.from_json_keyfile_name('E:\\API_NANING\\keys.json', scopes=scopes)

# file = gspread.authorize(creds)
# workbook = file.open('แบบประเมินความเสี่ยงที่จะเป็นโรคหลอดเลือดสมอง (Responses)')
# sheet = workbook.sheet1

# for cell in sheet.range('A2:A5'):
#     print(cell.value)



