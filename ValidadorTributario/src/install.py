#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors,  Column, Container, Row
from markdownify import markdownify as md
import uuid 
import base64
import subprocess
import webbrowser
from subprocess import check_output, Popen
import platform
import sys
import os
import io
from io import StringIO
import time
import shutil
from urllib.parse import urlparse, unquote, urlencode
import mimetypes
from pathlib import Path
from time import sleep
import re
import json
import paramiko
from datetime import datetime
import hashlib
import requests
import pyperclip

### Autor Gui
###
### - Sérgio S Q 
###
###
### <!-- LICENSE -->
### # Licenças
### Distributed under the GNU General Public License (GPL), version 3. See [`LICENSE`](\LICENSE.md) for more information.
### For additional information, please check <https://www.gnu.org/licenses/quick-guide-gplv3.html>
### This license model was selected with the idea of enabling collaboration of anyone interested in projects listed within this group.
### It is in line with the **Brazilian Public Software directives**, as published at: <https://softwarepublico.gov.br/social/articles/0004/5936/Manual_do_Ofertante_Temporario_04.10.2016.pdf>
###

### O python instalou localmente a partir da loja, não foi necessário instalar versão "portable":
### pip install -r requirements.txt
### pip install PyInstaller
### Opção de interface nativa do SO ou WEB na linha final
### Gerando de forma simples um arquivo único executável distribuível:
### C:\Users\sergiosq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\flet pack main.py
### É necessário instalar o Flutter para gerar aplicativo instalável e publicar na Microsoft Store.
### https://flet.dev/ ; https://flutter.dev/ 


###
### Provisoriamente para testes iniciais a gui fica no memso arquivo
### "\nData da consulta na SRF: " + str(datetime.today()) + ""



guiapplink = "https://raw.githubusercontent.com/InovaFiscaliza/RepositorioFerramentasGRs/refs/heads/main/ValidadorTributario/dist/GuiApp" # "http://testando:13000/testes/ValidadorTributario/raw/master/GuiApp.py"
if platform.system() == "windows":
   guiapplink += ".exe"  


nomeapp = "Instalando"
nomeappgui = nomeapp





async def main(page: ft.Page):


    pbmsg = ft.Text(value="")
    pb = ft.ProgressBar(width=400)

    def progresso():  

        page.scroll = "none"
        page.clean()
        page.add(
            ft.Column(
                [ft.ProgressRing()],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
        )
        pb.value = 0.001
        page.update()

    async def instalaGuiApp():

        part = -1
        while True:

            part = part + 1

            response = requests.get(f"{guiapplink}-{part.zfill(2)}")

            local_filename = GuiApp.part
            totalbits = 0
            if response.status_code == 200:
                with open(local_filename, 'ab') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            totalbits += 1024

                            pb.value = int(r1[0]) / 100
                            pbmsg.value = f"Parte{part.zfill(2)}: Baixou {totalbits*1024}KB..."
                            page.update()

                            f.write(chunk)

            else:
                print(f"Erro ao baixar")

     
 

    page.title = "Acessando Repositórios e instalando versão atual ..."

    progresso()

    pbmsg.value = f"Acessando Repositórios e instalando versão atual ..."
    page.update()

    await instalaGuiApp()



if "SSH_CLIENT" in os.environ:
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080) # redireciona interface para http://127.0.0.1:8080/
else:
    ft.app(target=main) # GUI nativa do SO onde está executando


