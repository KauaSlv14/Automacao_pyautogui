import pyautogui
import time

#entrar no site par fazer a automaçao
pyautogui.press("Win")

#entrar no navegador
pyautogui.write("Chrome")
pyautogui.press("Enter")
time.sleep(3)
pyautogui.click(x=663, y=68)

#Url do site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
pyautogui.press("Enter")
time.sleep(3)

#fazer login no site
pyautogui.click(x=788, y=380)
pyautogui.write("Kaua.slv@gmail.com")
pyautogui.press("Tab")
pyautogui.write("Kaua.slv344")
pyautogui.press("Tab")
pyautogui.press("Enter")
pyautogui.click()

#importando o pandas para ler dados
import pandas as pd
tabela=pd.read_csv("produtos.csv")

#faz a automacao 
for linha in tabela.index:
    time.sleep(1)
    pyautogui.click(x=787, y=267)
    codigo=tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    marca=tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("Tab")

    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    categoria=tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("Tab")

    custo=tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    obs=tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press('Tab')
    if obs=="non":
        None
    
    pyautogui.press("Enter")
    pyautogui.scroll(500000)
