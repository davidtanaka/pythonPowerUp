# Passo a passo do projeto
# passo 1: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2: Fazer login
# passo 3: Importar a base de dados de produtos
# passo 4: cadastrara 1 produto
# passo 5: Repetir o cadastro para todos os produtos
from time import sleep
import pyautogui
pyautogui.PAUSE = 0.5
#Abrir o chrome
pyautogui.press('win')
pyautogui.write('crhome')
pyautogui.press('enter')

# entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# Esperar o site carregar
sleep(3)

# passo 2: Fazer login
pyautogui.click(x=744, y=405)    
pyautogui.write('davitanaka0602@gmail.com')
sleep(0.5)
pyautogui.press('tab')
pyautogui.write('1244')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: importar a  base de dados de produtos

import pandas

tabela = pandas.read_csv('produtos.csv')

