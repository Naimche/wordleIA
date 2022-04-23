import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

diccionario = open('Diccionario.txt', 'r')
diccionariosinformat = diccionario.read()

listadic = diccionariosinformat.split(' ')

# Opciones de la ventana

# Entrando en wordle.com
driver = webdriver.Chrome()

driver.get('https://wordle.danielfrg.com/')

time.sleep(0.4)

# Acepto Cookies
driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-1"]/div[8]/button').click()

# Teclado a Variables

aClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[1]')
bClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[6]')
cClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[4]')
dClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[3]')
eClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[3]')
fClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[4]')
gClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[5]')
hClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[6]')
iClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[8]')
jClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[7]')
kClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[8]')
lClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[9]')
mClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[8]')
nClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[7]')
enieClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[10]')
oClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[9]')
pClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[10]')
qClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[1]')
rClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[4]')
sClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/button[2]')
tClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[5]')
uClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[7]')
vClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[5]')
wClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[2]')
xClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[3]')
yClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/button[6]')
zClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[2]')
enviarClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/button[1]')

# Variables Del Cuadrado
primer1 = '//*[@id="__next"]/div/div[2]/div/div[1]/div[1]/div/div[2]/div'
primer2 = '//*[@id="__next"]/div/div[2]/div/div[1]/div[2]/div/div[2]/div'
primer3 = '//*[@id="__next"]/div/div[2]/div/div[1]/div[3]/div/div[2]/div'
primer4 = '//*[@id="__next"]/div/div[2]/div/div[1]/div[4]/div/div[2]/div'
primer5 = '//*[@id="__next"]/div/div[2]/div/div[1]/div[5]/div/div[2]/div'
columna1 = [primer1, primer2, primer3, primer4, primer5]
# segunda fila
segunda1 = '//*[@id="__next"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div'
segunda2 = '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div'
segunda3 = '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div[2]/div'
segunda4 = '//*[@id="__next"]/div/div[2]/div/div[2]/div[4]/div/div[2]/div'
segunda5 = '//*[@id="__next"]/div/div[2]/div/div[2]/div[5]/div/div[2]/div'
columna2 = [segunda1, segunda2, segunda3, segunda4, segunda5]
# tercera fila
tercera1 = '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div/div[2]/div'
tercera2 = '//*[@id="__next"]/div/div[2]/div/div[3]/div[2]/div/div[2]/div'
tercera3 = '//*[@id="__next"]/div/div[2]/div/div[3]/div[3]/div/div[2]/div'
tercera4 = '//*[@id="__next"]/div/div[2]/div/div[3]/div[4]/div/div[2]/div'
tercera5 = '//*[@id="__next"]/div/div[2]/div/div[3]/div[5]/div/div[2]/div'
columna3 = [tercera1, tercera2, tercera3, tercera4, tercera5]
# Cuarta fila
cuarta1 = '//*[@id="__next"]/div/div[2]/div/div[4]/div[1]/div/div[2]/div'
cuarta2 = '//*[@id="__next"]/div/div[2]/div/div[4]/div[2]/div/div[2]/div'
cuarta3 = '//*[@id="__next"]/div/div[2]/div/div[4]/div[3]/div/div[2]/div'
cuarta4 = '//*[@id="__next"]/div/div[2]/div/div[4]/div[4]/div/div[2]/div'
cuarta5 = '//*[@id="__next"]/div/div[2]/div/div[4]/div[5]/div/div[2]/div'
columna4 = [cuarta1, cuarta2, cuarta3, cuarta4, cuarta5]
# Quinta fila
quinta1 = '//*[@id="__next"]/div/div[2]/div/div[5]/div[1]/div/div[2]/div'
quinta2 = '//*[@id="__next"]/div/div[2]/div/div[5]/div[2]/div/div[2]/div'
quinta3 = '//*[@id="__next"]/div/div[2]/div/div[5]/div[3]/div/div[2]/div'
quinta4 = '//*[@id="__next"]/div/div[2]/div/div[5]/div[4]/div/div[2]/div'
quinta5 = '//*[@id="__next"]/div/div[2]/div/div[5]/div[5]/div/div[2]/div'
columna5 = [quinta1, quinta2, quinta3, quinta4, quinta5]
# Sexta fila
sexta1 = '//*[@id="__next"]/div/div[2]/div/div[6]/div[1]/div/div[2]/div'
sexta2 = '//*[@id="__next"]/div/div[2]/div/div[6]/div[2]/div/div[2]/div'
sexta3 = '//*[@id="__next"]/div/div[2]/div/div[6]/div[3]/div/div[2]/div'
sexta4 = '//*[@id="__next"]/div/div[2]/div/div[6]/div[4]/div/div[2]/div'
sexta5 = '//*[@id="__next"]/div/div[2]/div/div[6]/div[5]/div/div[2]/div'
columna6 = [sexta1, sexta2, sexta3, sexta4, sexta5]


# funcion que analiza la palabra y la escribe en wordle

def analisisYescritura(palabra):
    listapalabra = list(palabra)

    for i in range(len(listapalabra)):
        time.sleep(0.20)
        if 'A' == listapalabra[i]:
            aClick.click()
        elif 'B' == listapalabra[i]:
            bClick.click()
        elif 'C' == listapalabra[i]:
            cClick.click()
        elif 'D' == listapalabra[i]:
            dClick.click()
        elif 'E' == listapalabra[i]:
            eClick.click()
        elif 'F' == listapalabra[i]:
            fClick.click()
        elif 'G' == listapalabra[i]:
            gClick.click()
        elif 'H' == listapalabra[i]:
            hClick.click()
        elif 'I' == listapalabra[i]:
            iClick.click()
        elif 'J' == listapalabra[i]:
            jClick.click()
        elif 'K' == listapalabra[i]:
            kClick.click()
        elif 'L' == listapalabra[i]:
            lClick.click()
        elif 'M' == listapalabra[i]:
            mClick.click()
        elif 'N' == listapalabra[i]:
            nClick.click()
        elif 'Ñ' == listapalabra[i]:
            enieClick.click()
        elif 'O' == listapalabra[i]:
            oClick.click()
        elif 'P' == listapalabra[i]:
            pClick.click()
        elif 'Q' == listapalabra[i]:
            qClick.click()
        elif 'R' == listapalabra[i]:
            rClick.click()
        elif 'S' == listapalabra[i]:
            sClick.click()
        elif 'T' == listapalabra[i]:
            tClick.click()
        elif 'U' == listapalabra[i]:
            uClick.click()
        elif 'V' == listapalabra[i]:
            vClick.click()
        elif 'W' == listapalabra[i]:
            wClick.click()
        elif 'X' == listapalabra[i]:
            xClick.click()
        elif 'Y' == listapalabra[i]:
            yClick.click()
        elif 'Z' == listapalabra[i]:
            zClick.click()
    enviarClick.click()


def filtradoDeLetrasInexistentes(diccionarioParam):
    letrasIncorrectas = driver.find_elements(By.CLASS_NAME, 'css-1hwd5vh')
    listaIncorrectas = []
    for i in range(len(letrasIncorrectas)):
        listaIncorrectas.append(letrasIncorrectas[i].text)

    dicFiltrando = diccionarioParam
    for i in range(len(listaIncorrectas)):
        for u in sorted(range(len(dicFiltrando)), reverse=True):
            if listaIncorrectas[i] in dicFiltrando[u]:
                dicFiltrando.pop(u)

    return dicFiltrando


def indiceDeAmarilla(columna):
    claseAmarilla = '[contains(@class, "css-140kyip")]'
    contador = 0
    indiceAmarillo = []
    for i in range(5):
        try:
            driver.find_element(By.XPATH, columna[i] + claseAmarilla)
            indiceAmarillo.append(i)
        except NoSuchElementException:
            -1
    return indiceAmarillo


def indiceDeCorrectas(columna):
    claseVerde = '[contains(@class, "css-1jtxyvl")]'
    indiceDeVerde = []

    for i in range(5):
        try:
            driver.find_element(By.XPATH, columna[i] + claseVerde)
            indiceDeVerde.append(i)
        except NoSuchElementException:
            -1
    return indiceDeVerde


def filtradoDePosicion(palabra, posicionesCorrectas, diccionarioParam):
    dicFiltrando = diccionarioParam
    for i in sorted(range(len(dicFiltrando)), reverse=True):
        for u in posicionesCorrectas:
            if palabra[u].upper() != dicFiltrando[i][u]:
                dicFiltrando.pop(i)

    return dicFiltrando


def filtradoDeExistencia(palabra, posicionesCorrectas, diccionarioParam):
    dicFiltrando = diccionarioParam

    # No contienen la letra
    for x in sorted(range(len(dicFiltrando)), reverse=True):
        for u in posicionesCorrectas:
            try:
             if palabra[u] not in dicFiltrando[x]:
                    dicFiltrando.pop(x)
            except IndexError:
                -1

    for i in sorted(range(len(dicFiltrando)), reverse=True):
        for u in posicionesCorrectas:
            if palabra[u] == dicFiltrando[i][u]:
                dicFiltrando.pop(i)

    return dicFiltrando


def ia():
    # Declaracion de variables
    filter1 = 'AIREO'
    analisisYescritura(filter1)

    # primera columna
    print(indiceDeCorrectas(columna1))
    print(indiceDeAmarilla(columna1))
    diccionarioFilter1 = filtradoDeLetrasInexistentes(listadic)
    diccionarioFilter1 = filtradoDePosicion(filter1, indiceDeCorrectas(columna1), diccionarioFilter1)
    diccionarioFilter1 = filtradoDeExistencia(filter1, indiceDeAmarilla(columna1), diccionarioFilter1)

    # SegundaColumna
    filter1 = diccionarioFilter1[0]
    analisisYescritura(filter1)
    print(indiceDeCorrectas(columna2))
    print(indiceDeAmarilla(columna2))
    diccionarioFilter1 = filtradoDeLetrasInexistentes(diccionarioFilter1)
    diccionarioFilter1 = filtradoDePosicion(filter1, indiceDeCorrectas(columna2), diccionarioFilter1)
    diccionarioFilter1 = filtradoDeExistencia(filter1, indiceDeAmarilla(columna2), diccionarioFilter1)

    # terceraColumna

    filter1 = diccionarioFilter1[0]
    analisisYescritura(filter1)
    print(indiceDeCorrectas(columna3))
    print(indiceDeAmarilla(columna3))
    diccionarioFilter1 = filtradoDeLetrasInexistentes(diccionarioFilter1)
    diccionarioFilter1 = filtradoDePosicion(filter1, indiceDeCorrectas(columna3), diccionarioFilter1)
    diccionarioFilter1 = filtradoDeExistencia(filter1, indiceDeAmarilla(columna3), diccionarioFilter1)

    # CuartaColumna
    filter1 = diccionarioFilter1[0]
    analisisYescritura(filter1)
    print(indiceDeCorrectas(columna4))
    print(indiceDeAmarilla(columna4))
    diccionarioFilter1 = filtradoDeLetrasInexistentes(diccionarioFilter1)
    diccionarioFilter1 = filtradoDePosicion(filter1, indiceDeCorrectas(columna4), diccionarioFilter1)
    diccionarioFilter1 = filtradoDeExistencia(filter1, indiceDeAmarilla(columna4), diccionarioFilter1)
    # Columna 5
    filter1 = diccionarioFilter1[0]
    analisisYescritura(filter1)
    print(indiceDeCorrectas(columna5))
    print(indiceDeAmarilla(columna5))
    diccionarioFilter1 = filtradoDeLetrasInexistentes(diccionarioFilter1)
    diccionarioFilter1 = filtradoDePosicion(filter1, indiceDeCorrectas(columna5), diccionarioFilter1)
    diccionarioFilter1 = filtradoDeExistencia(filter1, indiceDeAmarilla(columna5), diccionarioFilter1)

    # Sexta Columna
    filter1 = diccionarioFilter1[0]
    analisisYescritura(filter1)

ia()
