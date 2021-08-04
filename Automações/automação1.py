import pyautogui
import time
import pyperclip

pyautogui.alert("Vai começar. Aperte em OK e não mexa em nada.")
pyautogui.click(346,750)
time.sleep(3)
pyautogui.hotkey("ctrl" , "t")
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyperclip.copy(link)
time.sleep(5)
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(15)
pyautogui.click(371,293, clicks=2)
time.sleep(5)
pyautogui.click(449,325)
time.sleep(2)

import pandas as pd
tabela = pd.read_excel(r"C:\Users\Markfgui675\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

pyautogui.hotkey("ctrl" , "v")
link = "https://mail.google.com/mail/u/0/#inbox"
pyperclip.copy(link)
time.sleep(5)
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(50)
pyautogui.click(143,214)
time.sleep(15)
pyautogui.write("markfgui2006@gmail.com")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
assunto = "Só testando - Relatório de Vendas"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl" , "v")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
texto_email ='''
Prezados, Bom dia

O faturamento de ontem foi de: {} 
O total de produtos vendidos: {}

Marcos Gumarães'''.format(faturamento, quantidade)

pyautogui.write(texto_email)
time.sleep(1)
pyautogui.click(841,692)
time.sleep(5)
