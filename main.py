#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from pathlib import Path
import time

EDT_SELECT_URL = 'https://lise.ensam.eu/faces/ChoixPlanning.xhtml'
EDT_URL = 'https://lise.ensam.eu/faces/Planning.xhtml'


session = requests.Session()

headers = {
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr'
}

# Arrivée 
rep = session.get(EDT_SELECT_URL)
javax_faces_ViewState = BeautifulSoup(rep.text, features='html5lib').find(id='j_id1:javax.faces.ViewState:0')['value']
print(javax_faces_ViewState)

time.sleep(0.5)

data = {
    'form': 'form',
    'form:j_idt247_focus': '',
    'form:j_idt247_input': '44323',
    'javax.faces.ViewState': javax_faces_ViewState,
    'javax.faces.partial.ajax': 'true',
    'javax.faces.source': 'form:j_idt45',
    'javax.faces.partial.execute': 'form:j_idt45',
    'javax.faces.partial.render': 'form:sidebar',
    'form:j_idt45': 'form:j_idt45',
    'webscolaapp.Sidebar.ID_SUBMENU': 'submenu_1292865'
}


# Menu data 
rep = session.post(EDT_SELECT_URL, data=data, headers=headers)

time.sleep(0.5)

data = {
    'form': 'form',
    'form:largeurDivCenter': '1236',
    'form:j_idt247_focus': '',
    'form:j_idt247_input': '44323',
    'form:largeurDivCenter': '1236',
    'form:sidebar': 'form:sidebar',
    'form:sidebar_menuid': '1_1',
    'javax.faces.ViewState': javax_faces_ViewState
}

# Menu click
rep = session.post(EDT_SELECT_URL, data=data, headers=headers)
#print(rep.text)
javax_faces_ViewState = BeautifulSoup(rep.text, features='html5lib').find(id='j_id1:javax.faces.ViewState:0')['value']
print(javax_faces_ViewState)

time.sleep(0.5)


data = {
    'form': 'form',
    'form:largeurDivCenter': '1219',
    'form:search-texte': '',
    'form:search-texte-avancer': '',
    'form:input-expression-exacte':	'',
    'form:input-un-des-mots': '',
    'form:input-aucun-des-mots': '',
    'form:input-nombre-debut': '',
    'form:input-nombre-fin': '',
    'form:calendarDebut_input': '',
    'form:calendarFin_input': '',
    'form:j_idt180_reflowDD': '0_0',
    'form:j_idt180:j_idt185:filter': '',
    'form:j_idt180:j_idt187:filter': '',
    'form:j_idt180:j_idt189:filter': '',
    'form:j_idt180:j_idt191:filter': '',
    'form:j_idt180_checkbox': 'on',
    'form:j_idt180_selection': '47711527',
    'form:j_idt239': '',
    'form:j_idt249_focus': '',
    'form:j_idt249_input': '44323',
    'javax.faces.ViewState': javax_faces_ViewState
}

# EDT select
rep = session.post(EDT_SELECT_URL, data=data, headers=headers)
javax_faces_ViewState = BeautifulSoup(rep.text, features='html5lib').find(id='j_id1:javax.faces.ViewState:0')['value']
print(javax_faces_ViewState)
print(rep.text)
print(rep.url)
time.sleep(0.5)


data = {
    'form': 'form',
    'form:largeurDivCenter': '',
    'form:j_idt234_focus': '',
    'form:j_idt234_input': '44323',
    'javax.faces.partial.ajax': 'true',
    'javax.faces.source': 'form:j_idt117',
    'javax.faces.partial.execute': 'form:j_idt117',
    'javax.faces.partial.render': 'form:j_idt117',
    'form:j_idt117': 'form:j_idt117',
    'form:j_idt117_start': '1599429600000',
    'form:j_idt117_end': '1599861600000',
    'form:date_input': '07/09/2020',
    'form:week': '37-2020',
    'form:j_idt117_view': 'agendaWeek',
    'form:offsetFuseauNavigateur': '-7200000',
    'form:onglets_activeIndex': '0',
    'form:onglets_scrollState': '0',
    'javax.faces.ViewState': javax_faces_ViewState
}

headers = {
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Faces-Request': 'partial/ajax',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr'
}

rep = session.post(EDT_URL, data=data, headers=headers)
print(rep.text)


