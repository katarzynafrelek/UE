# Import potrzebnej biblioteki python opencv
import cv2

# Wczytanie zdjęcia metodą imread(sciezka do pliku)
zdjecie = cv2.imread('Zdjecie1.jpeg')
# zdjecie = cv2.imread('Zdjecie2.jpeg')
# zdjecie = cv2.imread('Zdjecie3.jpeg')

# Wczytanie modelu
siec = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')

# Parametry konfiguracji wczytanego modelu - nie zmieniac, tak było w dokumentacji
siec.setInputSize(320, 320)  # Musi byc drugi parametr, bez tego nie dziala
siec.setInputScale(1.0 / 127.5)
siec.setInputMean((125.7, 125.7, 125.7))
siec.setInputSwapRB(True)

# Sciezka do pliku zawierającego nazwy klas, które będą wykrywane
labelkiSciezka = 'labelki'
# Otwarcie pliku i pobranie z niego wartości, rstrip('\n') usuwa wskazane znaki na końcu wartości, Dzieli stringa na tablice po wskazanym znaku split('\n')
with open(labelkiSciezka, 'rt') as labelkiPlik:
    labelkiLista = labelkiPlik.read().rstrip('\n').split('\n')

# Wywołuje metode detec z obiektu siec - parametry wejściowe: obraz oraz parametr dokladnosci okreslajacy przy jakiej wartosci dokladnosci bedzie wykrywany obiekt
# parametry wyjściowe siec.detect: lista identyfikatorow klas, lista dokladnosci z jaka wykonano detekcje, ramka ograniczajaca
idKlas, dokladnosc, ramkiOgraniczajaca = siec.detect(zdjecie, confThreshold=0.5)
# Wykonuję petlę na równoległą na kilku listach: idKlas, dokladnosc, ramkiOgraniczajaca. Listy są ze sobą skorelowane po iteratorze
for idKlasy, dokladnosc, ramkaOgraniczajaca in zip(idKlas, dokladnosc, ramkiOgraniczajaca):
    # If zawężajacy rysowanie ramek tylko dla obiektu, który zostal zakwalifikowany jako person
    if labelkiLista[idKlasy - 1] == "person":
        # Metoda rectangle rysuje ramkę na zdjęciu, parametry wejściowe: zdjęcie, ramka ograniczajaca zwrocona przez model, kolor ramki (RGB), grubosc ramki)
        cv2.rectangle(zdjecie, ramkaOgraniczajaca, (0, 255, 255), thickness=1)
        # Metoda putTex dokłada tekst do ramki. Jako wspolrzedne startowe wykorzystuje przesuniecie wspolrzednych ramki z modelu
        cv2.putText(zdjecie, labelkiLista[idKlasy - 1] + " " + str(round((dokladnosc * 100), 2)) + "%",
                    (ramkaOgraniczajaca[0] + 10, ramkaOgraniczajaca[1] + 30), cv2.FONT_ITALIC, 1, (0, 255, 255), 1)

# Pokazuje zdjecie po obrobce
cv2.imshow("Output", zdjecie)
# Zamkniecie okna po przycisnieciu klawisza
cv2.waitKey(0)
