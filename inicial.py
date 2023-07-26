# Importar as bibliotecas

import pandas as pd
import time 
import pyautogui as pa


"""
1 - Entrar no site da empresa
    - Abrir o google
    - Entrar no site
"""
pa.PAUSE = 0.3

pa.press("win")
pa.write("chrome")
pa.press("enter")
time.sleep(4)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(5)

"""
2 - Fazer o login
    - Posicionar o mouse no campo e digitar o e-mail
    - TAB e digitar a senha
"""
pa.click(x=657, y=363)
pa.write("pythonimpressionador@gmail.com")

pa.press("tab")
pa.write("senha")

pa.press("tab")
pa.press("enter")

"""
3 - Importar base para cadastro

"""
base_cadastro = pd.read_csv("produtos.csv")

"""
4 - Cadastrar produto e repetir processo com loop

"""
for linha in base_cadastro.index:

    time.sleep(1.5)
    pa.click(x=501, y=243)

    codigo = base_cadastro.loc[linha, "codigo"]
    pa.write(str(codigo))

    pa.press("tab")

    marca = base_cadastro.loc[linha, "marca"]
    pa.write(str(marca))

    pa.press("tab")

    tipo = base_cadastro.loc[linha, "tipo"] 
    pa.write(str(tipo))

    pa.press("tab")

    categoria = base_cadastro.loc[linha, "categoria"]  
    pa.write(str(categoria))

    pa.press("tab")

    preco_unitario = base_cadastro.loc[linha, "preco_unitario"]   
    pa.write(str(preco_unitario))

    pa.press("tab")

    custo = base_cadastro.loc[linha, "custo"]    
    pa.write(str(custo))

    pa.press("tab")

    obs = base_cadastro.loc[linha, "obs"]

    if not pd.isna(obs): 

        pa.write(str(obs))

    pa.press("tab")
    pa.press("enter")

    pa.scroll(5000)