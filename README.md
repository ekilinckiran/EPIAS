# EPIAS
EPIAŞ Şeffaflık Platformu API Erişimi

EPİAŞ tarafından yayınlanan Rest Api platformuna erişim için https://seffaflik.epias.com.tr/transparency/technical/swagger.json adresindeki Swagger.json kullanılarak otomatik olarak oluşturulmuştur.

EPIAŞ Şeffaflık Platformuna API üzerinden ulaşım için statik ip adresine sahip olmanız ve https://www.epias.com.tr/wp-content/uploads/2016/10/Web-Servis-%C5%9Eartnamesi-1.docx adresindeki şartnameyi doldurarak EPİAŞ'a göndermeniz gerekmektedir. 

Erişim yetkisi bulunan IP adreslerinden sorgu yapmak için:


from EpiasApi import market

endPoint = market.EpiasApi("INSERT_EPIAS_API_KEY_HERE")
status, result = endPoint.DayAheadMcp("2020-05-20T00:00", "2020-05-20T23:00")

if status:
    print(result)
else:
    print({"Hata": result})
    
