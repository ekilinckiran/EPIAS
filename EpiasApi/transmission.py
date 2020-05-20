
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def CongestionRent(self, startDate, endDate, orderType):
        """Kısıt Maliyet Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            orderType {string} -- 
 
        Returns:
            {json} -- {
                       "urgentMarketMessageList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "orderType" : orderType }
        return self.__consumeAPI("/transmission/congestion-rent", params, "urgentMarketMessageList")
 
    def EntsOrganization(self, period, organizationId):
        """ENTSO-E X Kodları Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
            organizationId {integer} -- 
 
        Returns:
            {json} -- {
                       "urgentMarketMessageList" : []
                      }
        """
        params = { "period" : period, "organizationId" : organizationId }
        return self.__consumeAPI("/transmission/ents-organization", params, "urgentMarketMessageList")
 
    def NominalCapacity(self, startDate, endDate):
        """Nominal Capacity Service
 
        Arguments:
            startDate {string} -- Dönem bilgisi. Örn:2016-01-01
            endDate {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "nominalCapacitiyList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/transmission/nominal-capacity", params, "nominalCapacitiyList")
 
    def TransmissionSystemLossFactor(self, startDate, endDate):
        """ISKK Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "urgentMarketMessageList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/transmission/transmission-system-loss-factor", params, "urgentMarketMessageList")
 
    def ZeroBalance(self, startDate, endDate):
        """Sıfır Bakiye Servisi
 
        Arguments:
            startDate {string} -- Dönem bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "zeroBalances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/transmission/zero-balance", params, "zeroBalances,statistics")
 
