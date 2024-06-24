import requests
import time
from sensors import read_dht22
from actuator import control_pump

SERVER_URL = "http://your-server-ip:5000/data"
KOI_TYPE_ID = 1  # Ganti dengan ID jenis koi yang sesuai

def main():
    while True:
        temperature, humidity = read_dht22()
        if temperature and humidity:
            data = {
                "temperature": temperature,
                "ph": humidity,  # Ganti dengan nilai pH aktual jika tersedia
                "koi_type_id": KOI_TYPE_ID
            }
            response = requests.post(SERVER_URL, json=data)
            if response.status_code == 201:
                print("Data posted successfully")
            else:
                print("Failed to post data")
        
        # Contoh pengendalian pompa berdasarkan suhu
        if temperature > 30:
            control_pump(True)
        else:
            control_pump(False)

        time.sleep(60)

if __name__ == "__main__":
    main()
