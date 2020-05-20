
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def Market(self, date, type):
        """Karşılaştırma Rest Servisi
 
        Arguments:
            date {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            type {string} -- Karşılaştırma yapılacak donem bilgisi.
 
        Returns:
            {json} -- {
                       "marketCompares" : []
                      }
        """
        params = { "date" : date, "type" : type }
        return self.__consumeAPI("/compare/market", params, "marketCompares")
 
    def MarketDaily(self, date):
        """Günlük Karşılaştırma Servisi
 
        Arguments:
            date {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "marketCompares" : []
                      }
        """
        params = { "date" : date }
        return self.__consumeAPI("/compare/market/daily", params, "marketCompares")
 
