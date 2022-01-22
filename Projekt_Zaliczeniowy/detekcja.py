import cv2


def detekcja_osob(zdjecia: []):
    siec = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')

    siec.setInputSize(320, 320)
    siec.setInputScale(1.0 / 127.5)
    siec.setInputMean((125.7, 125.7, 125.7))
    siec.setInputSwapRB(True)

    labelkiSciezka = 'labelki'
    with open(labelkiSciezka, 'rt') as labelkiPlik:
        labelkiLista = labelkiPlik.read().rstrip('\n').split('\n')

    for plik in zdjecia:
        zdjecie = cv2.imread(plik)
        idKlas, dokladnosci, ramkiOgraniczajaca = siec.detect(zdjecie, confThreshold=0.5)
        for idKlasy, dokladnosc, ramkaOgraniczajaca in zip(idKlas, dokladnosci, ramkiOgraniczajaca):
            if labelkiLista[idKlasy - 1] == "person":
                cv2.rectangle(zdjecie, ramkaOgraniczajaca, (0, 255, 255), thickness=1)
                cv2.putText(zdjecie, labelkiLista[idKlasy - 1] + " " + str(round((dokladnosc * 100), 2)) + "%",
                            (ramkaOgraniczajaca[0] + 10, ramkaOgraniczajaca[1] + 30), cv2.FONT_ITALIC, 1, (0, 255, 255),
                            1)

        cv2.imshow("Output", zdjecie)
        cv2.waitKey(0)
