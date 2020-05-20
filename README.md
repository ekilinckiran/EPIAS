# EPIAS
EPIAŞ Şeffaflık Platformu API Erişimi

EPİAŞ tarafından yayınlanan Rest Api platformuna erişim için https://seffaflik.epias.com.tr/transparency/technical/swagger.json adresindeki Swagger.json kullanılarak otomatik olarak oluşturulmuştur.

EPIAŞ Şeffaflık Platformuna API üzerinden ulaşım için statik ip adresine sahip olmanız ve https://www.epias.com.tr/wp-content/uploads/2016/10/Web-Servis-%C5%9Eartnamesi-1.docx adresindeki şartnameyi doldurarak EPİAŞ'a göndermeniz gerekmektedir. 

Erişim yetkisi bulunan IP adreslerinden sorgu yapmak için:

```
from EpiasApi import market

endPoint = market.EpiasApi("INSERT_EPIAS_API_KEY_HERE")
status, result = endPoint.DayAheadMcp("2020-05-20T00:00", "2020-05-20T23:00")

if status:
    print(result)
else:
    print({"Hata": result})
```
API'ler ile çalışırken en büyük sorun tarih/saat formatıdır. Bu nedenle 1.1.1970 tarihinden bugune kadar olan saniyeyi gösteren EPOCH saniyesini kullanmak kullanışlı bir yöntemdir. Utils altında yer alan EpiasDateTime.py modülü bu amaçla geliştirilmiştir. Modül varsayılan olarak Türkiye'nin zaman dilimi olan GMT+3 zaman diliminde sonuç almakta ve getirmektedir. 

Kullanımı:
```
from Utils import EpiasDateTime

epochTimeFromShortFormat = EpiasDateTime.toEpoch("2020-12-25T23:00") 
epochTimeFromLongFormat = EpiasDateTime.toEpoch("2020-05-24T01:00:00.000+0300")

epiasTimeToShortFormat = EpiasDateTime.toEpiasShort(1589925600) #returns "2020-05-20T01:00"
epiasTimeToLongFormat = EpiasDateTime.toEpiasLong(1589925600) #returns "2020-05-20T01:00:00.000+0300"

```

