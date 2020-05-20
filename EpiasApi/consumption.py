
from EpiasApi.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def City(self):
        """Şehir Rest Servisi
 
        Returns:
            {json} -- {
                       "cityList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/consumption/city", params, "cityList")
 
    def Consumption(self, period):
        """Serbest Tüketici Çekiş Miktar Servisi
 
        Arguments:
            period {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "consumptions" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/consumption/consumption", params, "consumptions")
 
    def Distribution(self):
        """Dağıtım Bölge Rest Servis
 
        Returns:
            {json} -- {
                       "distributionList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/consumption/distribution", params, "distributionList")
 
    def DistributionProfile(self, period, distributionId, meterReadingType, subscriberProfileGroup):
        """Profil Abone Grup Çarpan Katsayı Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
            distributionId {integer} -- 
            meterReadingType {integer} -- 
            subscriberProfileGroup {integer} -- 
 
        Returns:
            {json} -- {
                       "distributionProfileList" : []
                      }
        """
        params = { "period" : period, "distributionId" : distributionId, "meterReadingType" : meterReadingType, "subscriberProfileGroup" : subscriberProfileGroup }
        return self.__consumeAPI("/consumption/distribution-profile", params, "distributionProfileList")
 
    def EligibleConsumerQuantity(self):
        """Serbest Tüketici Sayısı Rest Servisi
 
        Returns:
            {json} -- {
                       "eligibleConsumerQuantityList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/consumption/eligible-consumer-quantity", params, "eligibleConsumerQuantityList")
 
    def LoadEstimationPlan(self, startDate, endDate):
        """Yük Tahmin Planı
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "loadEstimationPlanList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/consumption/load-estimation-plan", params, "loadEstimationPlanList,statistics")
 
    def MeterReadingCompany(self, period):
        """Sayaç Okuyan Kurum Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "meterReadingCompanyList" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/consumption/meter-reading-company", params, "meterReadingCompanyList")
 
    def MeterReadingType(self):
        """Sayaç Okuma Tip Rest Servisi
 
        Returns:
            {json} -- {
                       "meterReadingTypeList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/consumption/meter-reading-type", params, "meterReadingTypeList")
 
    def RealTimeConsumption(self, startDate, endDate):
        """Gerçek Zamanlı Tüketim Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "hourlyConsumptions" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/consumption/real-time-consumption", params, "hourlyConsumptions,statistics")
 
    def St(self, startDate, endDate):
        """Profil Abone Grubuna Göre Serbest Tüketici Sayıları Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "stList" : []
                       "statistics" : []
                       "ratios" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/consumption/st", params, "stList,statistics,ratios")
 
    def SubscriberProfileGroup(self, period, distributionId):
        """Profil Abone Grup
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
            distributionId {integer} -- 
 
        Returns:
            {json} -- {
                       "subscriberProfileGroupList" : []
                      }
        """
        params = { "period" : period, "distributionId" : distributionId }
        return self.__consumeAPI("/consumption/subscriber-profile-group", params, "subscriberProfileGroupList")
 
    def Swv(self, startDate, endDate):
        """Uzlaştırmaya Esas Çekiş Miktarı
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "swvList" : []
                       "statistic" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/consumption/swv", params, "swvList,statistic")
 
    def SwvV2(self, period):
        """Serbest Tüketici Çekiş Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "swvV2List" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/consumption/swv-v2", params, "swvV2List")
 
    def UnderSupplyLiabilityConsumption(self, startDate, endDate):
        """Tedarik Yükümlülüğü Kapsamındaki UEÇM Miktarı
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "swvList" : []
                       "statistic" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/consumption/under-supply-liability-consumption", params, "swvList,statistic")
 
