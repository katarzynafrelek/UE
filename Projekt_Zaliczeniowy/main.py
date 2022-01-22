import glob

from detekcja import detekcja_osob

zdjecia = glob.glob('Zdjecia/*')
detekcja_osob(zdjecia)
