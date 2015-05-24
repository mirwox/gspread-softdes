# -*- coding:utf-8 -*-

# Adaptado dos exemplos fornecidos em https://github.com/burnash/gspread

import gspread

from tkinter import simpledialog, Tk


root = Tk()
root.withdraw()
print("Atenção à caixa de diálogo que vai pedir a senha")
password = simpledialog.askstring("Password", "Enter password:", show='*')


# Login with your Google account
gc = gspread.login('softdes.gspread', password)

# Abre uma aba da planilha
wks = gc.open("Planilha Teste").sheet1

wks.update_acell('B2', "Teste na planilha")

# Busca uma faixa de células
cell_list = wks.range('A1:B7')

print(cell_list)

