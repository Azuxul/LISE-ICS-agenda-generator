#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from pathlib import Path
import time
from datetime import datetime, timedelta
import xmltodict
import ics

EDT_SELECT_URL = 'https://lise.ensam.eu/faces/ChoixPlanning.xhtml'
EDT_URL = 'https://lise.ensam.eu/faces/Planning.xhtml'

EDT_SELECTION = [60745372, 60745322, 60745364] # Obtained from https://lise.ensam.eu/faces/Planning.xhtml by getting the value from the feild form:j_idt181_selection in the request
ALLOWED_GROUPS = ['7GIE CM', '7GIE TP22', '7GIE ED2']

def get_monday(datetime_of_week: datetime):
    t = datetime(datetime_of_week.year, datetime_of_week.month, datetime_of_week.day)
    return t - timedelta(days=t.weekday())


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

print("page 1")
#time.sleep(2)


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

#print(rep.text)
#time.sleep(2)


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
javax_faces_ViewState = BeautifulSoup(rep.text, features='html5lib').find(id='j_id1:javax.faces.ViewState:0')['value']

print("3")
#print(rep.text)
#time.sleep(2)

# idt numbers values can change very offten (example value : form:j_idt180_reflowDD)
idt_1 = 181
idt_2 = 240
idt_3 = 250

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
    'form:j_idt'+str(idt_1)+'_reflowDD': '0_0',
    'form:j_idt'+str(idt_1)+':j_idt185:filter': '',
    'form:j_idt'+str(idt_1)+':j_idt187:filter': '',
    'form:j_idt'+str(idt_1)+':j_idt189:filter': '',
    'form:j_idt'+str(idt_1)+':j_idt191:filter': '',
    'form:j_idt'+str(idt_1)+'_checkbox': 'on',
    'form:j_idt'+str(idt_1)+'_selection': ",".join(str(x) for x in EDT_SELECTION), 
    'form:j_idt'+str(idt_2): '',
    'form:j_idt'+str(idt_3)+'_focus': '',
    'form:j_idt'+str(idt_3)+'_input': '44323',
    'javax.faces.ViewState': javax_faces_ViewState
}

# EDT select
rep = session.post(EDT_SELECT_URL, data=data, headers=headers)
#print(rep.text)
#print(rep.url)
javax_faces_ViewState = BeautifulSoup(rep.text, features='html5lib').find(id='j_id1:javax.faces.ViewState:0')['value']
print("4")
#time.sleep(2)

date = datetime.now()

t_start = int(date.timestamp())
start = str(t_start) + "000"
end = str(t_start+432000000) + "000"

date_input = str(date.day) + "/" + str(date.month) + "/" + str(date.day)
iso_date = date.isocalendar()
week = str(iso_date[1]) + "-" + str(iso_date[0])

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
    'form:j_idt117_start': start,
    'form:j_idt117_end': end,
    'form:date_input': date_input,
    'form:week': week,
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

result = xmltodict.parse(rep.text)
print(result)
json_str = result['partial-response']['changes']['update'][1]['#text']
#print(json_str)
json_result = json.loads(json_str)
#print(json_result)

calendar = ics.Calendar()

for event in json_result['events']:

    data = event['title'].split(' - ')

    groups = data[-1].split(' / ')

    valid_event = False

    for a_group in ALLOWED_GROUPS:
        if a_group in groups:
            valid_event = True
            break

    print(event)
    if valid_event:
#        print(event)
        ics_event = ics.Event()
        ics_event.name = data[1] + " - " + data[2] + " - " + data[4]
        ics_event.organizer = data[3]
        ics_event.begin = event['start']
        ics_event.end = event['end']
        
        calendar.events.add(ics_event)

with open('my.ics', 'w') as my_file:
    my_file.writelines(calendar)
	