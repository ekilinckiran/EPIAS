#Hangi Path üzerinden API sorgusu yapılacaksa onu import edin

from EpiasApi import market

#IP erişim yetkisi aldıktan sonra EPIAS API Portal içerisinde bir application oluşturup, 
#API erişimi için bir anahtar almanız gerekmektedir. 

endPoint = market.EpiasApi("INSERT_EPIAS_API_KEY_HERE")

status, result = endPoint.DayAheadMcp("2020-05-20T00:00", "2020-05-20T23:00")

#EPIAS bazı sorgularda istatistic verilerini de göndermektedir. 
#Bu nedenle API'den gelen sonucun tüm içeriği geri dönmektedir. 
#İstenirse def detaylarında verilen JSON liste anahtarı ile yalnızca istenen veriler alınabilir. 

if status:
    print(result) #Saatlik PTF ve istatistik verileri.
    print(result["dayAheadMcpList"]) #Yalnızca saatlik PTF verileri.
else:
    print({"Hata": result})
