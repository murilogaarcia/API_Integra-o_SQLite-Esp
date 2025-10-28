import requests
import random
import time


#Simulador teste

URL = "http://127.0.0.1:8000/dados/"

while True:
     sensor_id = 1
     velocidade = round(random.uniform(30, 150), 2)
     aceleracao = round(random.uniform(10, 80), 2)

     response = requests.post(URL, params={
         "sensor_id": sensor_id,
         "velocidade": velocidade,
         "aceleracao": aceleracao
     })

     print(response.json())
     time.sleep(7)  # envia a cada 7 segundos



# ---- CONFIGURAÇÃO DA API
#URL = "http://192.168.0.100:8000/dados/"  # IP do PC rodando a API

'''
import network
import time
import urequests
from machine import Pin

# ======= CONFIGURAÇÕES =======
SSID = "nome_rede"
PASSWORD = "senha_rede"
URL = "http://192.168.0.100:8000/dados/"
SENSOR_ID = 1

# 4 piezos (em metros, igualmente espaçados)
piesos = [
    Pin(4, Pin.IN),   # Piezo 1
    Pin(5, Pin.IN),   # Piezo 2
    Pin(18, Pin.IN),  # Piezo 3
    Pin(19, Pin.IN)   # Piezo 4
]

DISTANCIA_ENTRE_SENSORES = 0.5  # metros
DISTANCIA_TOTAL = DISTANCIA_ENTRE_SENSORES * (len(piesos) - 1)


# ======= FUNÇÃO DE CONEXÃO WIFI =======
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
        print("\n✅ Conectado com sucesso!")
        print("IP do ESP32:", wlan.ifconfig()[0])
    else:
        print("\n❌ Falha na conexão Wi-Fi.")


# ENVIO DE DADOS 
def enviar_dados(velocidade, aceleracao):
    try:
        response = urequests.post(
            URL,
            params={
                "sensor_id": SENSOR_ID,
                "velocidade": round(velocidade, 2),
                "aceleracao": round(aceleracao, 2),
            }
        )
        print(f"📡 Enviado -> Velocidade: {velocidade:.2f} km/h | Aceleração: {aceleracao:.2f} m/s² | Status: {response.status_code}")
        response.close()
    except Exception as e:
        print("Erro ao enviar dados:", e)


# ======= CAPTURA DOS DADOS =======
def capturar_veiculo():
    print("Aguardando passagem de veículo...")
    while True:
        # Espera o primeiro sensor detectar
        if piesos[0].value() == 1:
            tempos = []
            print("\n🚗 Veículo detectado!")

            # Captura tempo de detecção de cada piezo
            for i, piezo in enumerate(piesos):
                while piezo.value() == 0:
                    pass
                tempos.append(time.ticks_us())
                print(f"→ Sensor {i+1} acionado")

            # Calcula intervalos de tempo entre sensores (em segundos)
            intervalos = [(tempos[i+1] - tempos[i]) / 1_000_000 for i in range(len(tempos) - 1)]

            # Calcula velocidades parciais (em m/s)
            velocidades = [DISTANCIA_ENTRE_SENSORES / t for t in intervalos if t > 0]

            if len(velocidades) >= 2:
                v1 = velocidades[0]
                v4 = velocidades[-1]
                t_total = (tempos[-1] - tempos[0]) / 1_000_000

                # Velocidade média (km/h)
                v_media_kmh = ((v1 + v4) / 2) * 3.6

                # Aceleração média (m/s²)
                aceleracao = (v4 - v1) / t_total

                enviar_dados(v_media_kmh, aceleracao)

                print(f"🕒 Tempo total: {t_total:.4f}s | 💨 Velocidade média: {v_media_kmh:.2f} km/h | ⚡ Aceleração: {aceleracao:.2f} m/s²")

            time.sleep(2)  # Evita leituras consecutivas


# PROGRAMA PRINCIPAL
try:
    conectar_wifi()
    capturar_veiculo()
except KeyboardInterrupt:
    print("Programa interrompido.")
'''

