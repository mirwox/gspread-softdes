from oauth2client.client import SignedJwtAssertionCredentials
import json
import gspread



# Para funcionar, crie credenciais Oauth2 no Google Developer Console
# Salve as credenciais no arquivo json_app_id no mesmo diretório que este programa

json_key = json.load(open('json_app_id.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(
    json_key['client_email']
    , bytes(json_key['private_key'], 'UTF-8')
    , scope)

gc = gspread.authorize(credentials)

# A partir daqui continua igual

# Abre uma aba da planilha
wks = gc.open("Planilha Teste").sheet1

# Pode-se também abrir pela URL
# wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1OwYU05sxy2iH5_vOzMQgVMLaQB673DuVJ3BpQfY4Txc/edit#gid=0")


wks.update_acell('B3', "Teste na planilha")

# Busca uma faixa de células
cell_list = wks.range('A1:B7')

print(cell_list)
