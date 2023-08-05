import requests
import sys

# Değerleri Alma

access_key = input("API Anahtarını Giriniz: ")
currency_to = input("Dönüştürülecek Para Birimini Griniz: ")
currency_from = input("Kaynak Para Birimini Giriniz: ")
miktar = float(input("Miktar: "))

# API endpoint URL
url = 'http://apilayer.net/api/live'

# API Prametreleri

params = {
    "access_key": f"{access_key}",
    "currencies": f"{currency_to}",
    "source": currency_from,
    "format": "1"
}


try:
    #! Get isteğiyle API ye bağlanıyoruz.
    response = requests.get(url, params=params)

    # Yanıtı kontrol ediyoruz ve işliyoruz.
    if response.status_code == 200:
        data = response.json()
        print("\n\tPara Döviz Kuru: {}".format(
            data['quotes'][currency_from+currency_to] * miktar))

    else:
        print("Hata Kodu: {}".format(response.status_code))
        print("Hata Mesajı: {}".format(response.text))


except requests.exceptions.RequestException as e:
    print("İstek Hatası", e)

except KeyError as k:
    sys.stderr.write("Lütfen geçerli bir para birimi giriniz.")
    sys.stderr.flush()
