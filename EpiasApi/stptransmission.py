
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def Actualization(self, startDate, endDate):
        """Stok Miktarı Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "actualizations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp-transmission/actualization", params, "actualizations,statistics")
 
    def Transport(self, startDate, endDate):
        """Taşıma Giriş Miktarı Bildirimi Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "transport" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp-transmission/transport", params, "transport,statistics")
 
