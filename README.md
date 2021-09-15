# LISE ICS agenda generator

This projet is not complete and is only a simple and durty python script to generate an ics agenda file from an online service caled LISE.

Currently configured to generate and download 7GIE, 7GIE ED2 and 7GIE TP22 (2021) agenda from LISE.

## Usage

Edit the diffrents constants in `main.py` especialy the EDT_SELECTION array that contain the LISE id of the difrents agenda that shoud be manualy fund by copying the content of the field `form:j_idtXX_selection` in a request to show the needed agendas from the page `` (https://lise.ensam.eu/faces/Planning.xhtml)

## Dependencry installation

```bash
pip install -r requirments.txt
```

