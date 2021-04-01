# Catálogo

Una pequeña aplicación para gestionar un inventario de biblioteca personal.

## versión alpha

En este momento esta aplicación puede leer el código de barras y añade a un archivos csv ("catálogo.csv") los siguientes elementos:

> ['clasificación', 'autoría', 'título', 'editorial', 'ISBN']

Las fuentes de datos son:

* [Classify](http://classify.oclc.org/classify2/), un proyecto del [OCLC Research](http://www.oclc.org/research.html)
* [WorldCat](https://www.worldcat.org/)

## Prerrequisitos

Es recomendable crear un entorno virtual.

### Entorno virtual con `venv`

Crear un entorno virtual:

```
python3 -m venv catbiblio
```

Activar el entorno virtual

En Windows:

```
catbiblio\Scripts\activate.bat
```

En Unix o MacOS:

```
source catbiblio/bin/activate
```

### Entorno virtual con `conda`

Para crear un entorno virtual en Anaconda solamente debe ejecutar el siguiente código:

```
conda create --name catbiblio python
```

Para activar el entorno, solamente es necesario ejecutar lo siguiente:

```
conda activate catbiblio
```

### Instalar dependencias

Para utilizar esta aplicación se require instalar las librerías `OpenCV`, `pyzbar`, `requests` y `BeautifulSoup`. Después de activar el entorno virtual, puede ejecutar el archivo 'requirements.txt' para instalar las versiones adecuadas:

```
pip install -r requirements.txt
```

## Uso

El programa se ejecuta desde `main.py`.

Al ejecutar el script, se inicia la cámara web y se abre una ventana con el video. Acercar el código de barras del libro a la cámara hasta que el programa lo reconozca (la imagen se congela y el código de barras se enmarca con los datos del código de barras y su tipo)

<img src="imgs\captura.png" weight="400px">

La ventana se cerrará automáticamente cuando el registro del libro se halla escrito en el archivo csv.

En la terminal se imprimirán una serie de mensajes como el siguiente:

```
Barcode: 9786070743603 | Type: EAN13
[ WARN:1] global C:\User9786070743603s
\appveyor\AppData\Local\Temp\1\pip-req-build-wvn_it83\opencv\modules\videoio\src\cap_msmf.cpp (434) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
{'clasificación': '813.54', 'autoría': 'Philip K Dick; Miguel Antón; Planeta (Firm : Mexico City, Mexico),', 'título': '¿Sueñan los androides con ovejas eléctricas?', 'editorial': 'Ciudad de México : Editorial Planeta Mexicana : bajo el sello Minotauro, [2017] 2017', 'ISBN': '9786070743603'}
```

Si es la primera vez que se ejecuta el programa, se creará un archivo csv llamado 'catálogo.csv'. 

Cada vez que el proceso se repita se añadirá un elemento al archivo csv.

