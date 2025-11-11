import requests
import random
import time


#Simulador teste

URL = "http://127.0.0.1:8000/dados/"

while True:
     sensor_id = 1
     velocidade = round(random.uniform(30, 150), 2)
     aceleracao = round(random.uniform(-20, 80), 2)

     response = requests.post(URL, params={
         "sensor_id": sensor_id,
         "velocidade": velocidade,
         "aceleracao": aceleracao
     })

     print(f"📡 Enviado -> Velocidade: {velocidade:.2f} km/h | Aceleração: {aceleracao:.2f} m/s² | Status: {response.status_code}")
     print(response.json())
     time.sleep(7)  # envia a cada 7 segundos



# CONFIGURAÇÃO DA API
#URL = "http://192.168.0.100:8000/dados/"  # IP do PC rodando a API

'''
import network
import time
import urequests
from machine import Pin, time_pulse_us


# CONFIGURAÇÕES DE REDE E API

SSID = "nome_rede"
PASSWORD = "senha_rede"
URL = "http://192.168.0.100:8000/dados/"
SENSOR_ID = 1


# CONFIGURAÇÕES DOS SENSORES

DISTANCIA_ENTRE_SENSORES = 0.5  # metros
LIMIAR_DETECCAO = 50  # cm - distância abaixo da qual detecta veículo

# Lista de sensores (trigger, echo)
sensores = [
    {"trigger": Pin(4, Pin.OUT), "echo": Pin(5, Pin.IN)},
    {"trigger": Pin(18, Pin.OUT), "echo": Pin(19, Pin.IN)},
    {"trigger": Pin(21, Pin.OUT), "echo": Pin(22, Pin.IN)},
    {"trigger": Pin(23, Pin.OUT), "echo": Pin(25, Pin.IN)},
]


# CONECTAR AO WI-FI

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


# MEDIÇÃO DE DISTÂNCIA (ULTRASSÔNICO)

def medir_distancia(trigger, echo):
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(10)
    trigger.off()

    duracao = time_pulse_us(echo, 1, 30000)  # tempo de resposta em microssegundos
    if duracao < 0:  # falha na leitura
        return 999
    distancia = (duracao / 2) / 29.1  # conversão para cm
    return distancia


# ENVIO DE DADOS PARA A API

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
        print("❌ Erro ao enviar dados:", e)


# CAPTURA DE VEÍCULO

def capturar_veiculo():
    print("Aguardando passagem de veículo...")

    while True:
        # Detecta o primeiro sensor
        if medir_distancia(sensores[0]["trigger"], sensores[0]["echo"]) < LIMIAR_DETECCAO:
            tempos = []
            print("\n🚗 Veículo detectado!")

            # Percorre os 4 sensores
            for i, sensor in enumerate(sensores):
                # Espera até o veículo passar na frente do sensor
                while medir_distancia(sensor["trigger"], sensor["echo"]) >= LIMIAR_DETECCAO:
                    time.sleep_ms(10)
                tempos.append(time.ticks_us())
                print(f"→ Sensor {i+1} acionado")

                # Evita interferência entre sensores
                time.sleep_ms(100)

            # Cálculos
            intervalos = [(tempos[i+1] - tempos[i]) / 1_000_000 for i in range(len(tempos) - 1)]
            velocidades = [DISTANCIA_ENTRE_SENSORES / t for t in intervalos if t > 0]

            if len(velocidades) >= 2:
                v1 = velocidades[0]
                v4 = velocidades[-1]
                t_total = (tempos[-1] - tempos[0]) / 1_000_000

                v_media_kmh = ((v1 + v4) / 2) * 3.6
                aceleracao = (v4 - v1) / t_total

                enviar_dados(v_media_kmh, aceleracao)

                print(f"🕒 Tempo total: {t_total:.4f}s | 💨 Velocidade média: {v_media_kmh:.2f} km/h | ⚡ Aceleração: {aceleracao:.2f} m/s²")

            print("\n🔄 Aguardando novo veículo...\n")
            time.sleep(2)


# EXECUÇÃO PRINCIPAL

try:
    conectar_wifi()
    capturar_veiculo()
except KeyboardInterrupt:
    print("\n🛑 Programa interrompido.")

'''

