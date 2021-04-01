import cv2
import numpy as np
from pyzbar.pyzbar import decode
from catalogo import catalogo
import csv
from csv import DictWriter
import os


def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='', encoding='utf-8') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(frame, string, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print("Barcode: "+barcodeData + " | Type: "+barcodeType)
        cap.release()
        cv2.destroyAllWindows()
        return barcodeData


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    variable = decoder(frame)
    cv2.imshow('BarCode', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break

# ¿Hacer algo con los datos obtenidos?
print(variable)
cata = catalogo(variable)
print(cata)

archivo_csv = "catálogo.csv"
field_names = ['clasificación', 'autoría', 'título', 'editorial', 'ISBN']

if not os.path.exists(archivo_csv):
    with open(archivo_csv, 'w', encoding='utf-8') as acsv:
        dw = csv.DictWriter(acsv, fieldnames = field_names)
        dw.writeheader()
        acsv.close()

append_dict_as_row(archivo_csv, cata, field_names)
