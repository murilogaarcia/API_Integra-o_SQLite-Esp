import requests
import random
import time


#Simulador teste

URL = "http://127.0.0.1:8000/dados/"

while True:
     sensor_id = 1
     velocidade = round(random.uniform(30, 120), 2)

     response = requests.post(URL, params={
         "sensor_id": sensor_id,
         "velocidade": velocidade
     })

     print(response.json())
     time.sleep(7)  # envia a cada 2 segundos



# ---- CONFIGURAÇÃO DA API
#URL = "http://192.168.0.100:8000/dados/"  # IP do PC rodando a API

'''
import network
import time
import urequests  # biblioteca do MicroPython para requisições HTTP
from machine import Pin

# Configurando wifi
SSID = "nome_rede"         # coloque o nome da sua rede Wi-Fi
PASSWORD = "senha_rede"    # e a senha

# configurando API
URL = "http://192.168.0.100:8000/dados/"  # IP do PC rodando a API FastAPI
SENSOR_ID = 1

# Configurando sensores
piesos = [
    Pin(4, Pin.IN),   # Piezo 1
    Pin(5, Pin.IN),   # Piezo 2
    Pin(18, Pin.IN),  # Piezo 3
    Pin(19, Pin.IN),  # Piezo 4
    Pin(21, Pin.IN)   # Piezo 5
]
DISTANCIA_TOTAL = 2.0  # distância total entre o primeiro e o último piezo (em metros)

# Conexão wifi
def conectar_wifi():
    print("Conectando ao Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    tentativas = 0
    while not wlan.isconnected() and tentativas < 10:
        print(".", end="")
        time.sleep(1)
        tentativas += 1

    if wlan.isconnected():
        print("\nConectado com sucesso!")
        print("IP do ESP32:", wlan.ifconfig()[0])
    else:
        print("\nFalha na conexão Wi-Fi.")

# Enviando os dados para a API
def enviar_velocidade(velocidade):
    """Envia a velocidade calculada para a API"""
    try:
        response = urequests.post(URL, params={"sensor_id": SENSOR_ID, "velocidade": velocidade})
        print("Dados enviados -> Velocidade:", velocidade, "km/h | Status:", response.status_code)
        response.close()
    except Exception as e:
        print("Erro ao enviar dados:", e)

# capturando os dados dos piesos
def capturar_veiculo():
    print("Aguardando passagem de veículo...")
    while True:
        # Espera o primeiro sensor detectar
        if piesos[0].value() == 1:
            t_inicial = time.ticks_us()

            # Espera o último sensor detectar
            while piesos[-1].value() == 0:
                pass
            t_final = time.ticks_us()

            # Calcula tempo em segundos
            tempo = (t_final - t_inicial) / 100000000

            # Calcula velocidade (m/s -> km/h)
            if tempo > 0:
                velocidade = DISTANCIA_TOTAL / tempo
                velocidade_kmh = round(velocidade * 3.6, 2)
                enviar_velocidade(velocidade_kmh)
                print("Velocidade:", velocidade_kmh, "km/h")

            # Evita múltiplas leituras seguidas
            time.sleep(1)

# programa principal
try:
    conectar_wifi()
    capturar_veiculo()
except KeyboardInterrupt:
    print("Programa interrompido.")'''

