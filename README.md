# LISE ICS agenda generator

This project is not complete and is only a simple and dirty python script to generate an ics agenda file from an online service called LISE.

Currently configured to generate and download 7GIE, 7GIE ED2 and 7GIE TP22 (2021) agenda from LISE.

## Usage

Edit the different constants in `main.py` especially the EDT_SELECTION array that contain the LISE id of the different agenda that should be manually fond by copying the content of the field `form:j_idtXX_selection` in a request to show the needed agendas from the page `EDT_URL` (https://lise.ensam.eu/faces/Planning.xhtml). You need be not connected on LISE to do that.

Sometime, extra hours are downloaded (ex: in the 7GIE agenda, hours for 7GIE ED1 can be found sometimes) so it is needed to add the groups to save in the ics agenda in the array `ALLOWED_GROUPS`.

## Dependencry installation

```bash
pip install -r requirments.txt
```

