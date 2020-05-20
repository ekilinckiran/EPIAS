
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def Daily(self, date):
        """EPİAŞ Günlük Bülten Servisi
 
        Arguments:
            date {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bulletins" : []
                      }
        """
        params = { "date" : date }
        return self.__consumeAPI("/bulletin/daily", params, "bulletins")
 
    def Monthly(self):
        """EPİAŞ Aylık Bülten Servisi
 
        Returns:
            {json} -- {
                       "bulletins" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/bulletin/monthly", params, "bulletins")
 
    def NaturalgasDaily(self, date):
        """EPİAŞ Daily Natural Gas Bulletin Rest Service
 
        Arguments:
            date {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bulletins" : []
                      }
        """
        params = { "date" : date }
        return self.__consumeAPI("/bulletin/naturalgas/daily", params, "bulletins")
 
    def Weekly(self):
        """EPİAŞ Haftalık Bülten Servisi
 
        Returns:
            {json} -- {
                       "bulletins" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/bulletin/weekly", params, "bulletins")
 
    def Year(self):
        """EPİAŞ Yıllık Bülten Servisi
 
        Returns:
            {json} -- {
                       "bulletins" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/bulletin/year", params, "bulletins")
 
