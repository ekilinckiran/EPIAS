
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def Aic(self, organizationEIC, uevcbEIC, startDate, endDate):
        """Emre Amade Kapasite Rest Servisi
 
        Arguments:
            organizationEIC {string} -- Organizasyon EIC bilgisi . Örn:40X000000000540Y
            uevcbEIC {string} -- UEVÇB EIC bilgisi . Örn:40W0000000001960
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "aicList" : []
                       "statistics" : []
                      }
        """
        params = { "organizationEIC" : organizationEIC, "uevcbEIC" : uevcbEIC, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/aic", params, "aicList,statistics")
 
    def Dpp(self, organizationEIC, uevcbEIC, startDate, endDate):
        """Kesinleşmiş Günlük Üretim Rest Servisi
 
        Arguments:
            organizationEIC {string} -- Organizasyon EIC bilgisi . Örn:40X000000000540Y
            uevcbEIC {string} -- UEVÇB EIC bilgisi . Örn:40W0000000001960
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "dppList" : []
                       "statistics" : []
                      }
        """
        params = { "organizationEIC" : organizationEIC, "uevcbEIC" : uevcbEIC, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/dpp", params, "dppList,statistics")
 
    def DppInjectionUnitName(self, organizationEIC):
        """KGÜP UEVÇB Rest Servisi
 
        Arguments:
            organizationEIC {string} -- Organizasyon EIC bilgisi . Örn:40X000000000540Y
 
        Returns:
            {json} -- {
                       "injectionUnitNames" : []
                      }
        """
        params = { "organizationEIC" : organizationEIC }
        return self.__consumeAPI("/production/dpp-injection-unit-name", params, "injectionUnitNames")
 
    def DppOrganization(self, organizationName):
        """KGÜP Organizasyon Rest Servisi
 
        Arguments:
            organizationName {string} -- Organization name info (You must enter a minimum of 3 characters to search by name).
 
        Returns:
            {json} -- {
                       "organizations" : []
                      }
        """
        params = { "organizationName" : organizationName }
        return self.__consumeAPI("/production/dpp-organization", params, "organizations")
 
    def FinalDpp(self, startDate, endDate):
        """Toplam Kesinleşmiş Günlük Üretim Planı Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "finalDPPList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/final-dpp", params, "finalDPPList")
 
    def GddkAmount(self, startDate, endDate):
        """GDDK Tutarı Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "gddkAmountList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/gddk-amount", params, "gddkAmountList")
 
    def InstalledCapacity(self, period):
        """Kurulu Güç Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "installedCapacityList" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/production/installed-capacity", params, "installedCapacityList")
 
    def InstalledCapacityOfRenewable(self, period):
        """YEKDEM Kurulu Güç Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "installedCapacityOfRenewableList" : []
                       "statistics" : []
                       "ratios" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/production/installed-capacity-of-renewable", params, "installedCapacityOfRenewableList,statistics,ratios")
 
    def PowerPlant(self, period):
        """Santral Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "powerPlantList" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/production/power-plant", params, "powerPlantList")
 
    def RealTimeGeneration(self, startDate, endDate):
        """Gerçek Zamanlı Üretim Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "hourlyGenerations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/real-time-generation", params, "hourlyGenerations,statistics")
 
    def RealTimeGenerationPowerPlantList(self):
        """Real Time Generation Power Plants Rest Service
 
        Returns:
            {json} -- {
                       "powerPlantList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/production/real-time-generation-power-plant-list", params, "powerPlantList")
 
    def RealTimeGeneration_with_powerplant(self, startDate, endDate, powerPlantId):
        """Real Time Generation With Power Plant Parameter Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            powerPlantId {integer} -- Santral ID bilgisi .Örn:415
 
        Returns:
            {json} -- {
                       "hourlyGenerations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "powerPlantId" : powerPlantId }
        return self.__consumeAPI("/production/real-time-generation_with_powerplant", params, "hourlyGenerations,statistics")
 
    def Region(self):
        """Bölge Rest Servisi
 
        Returns:
            {json} -- {
                       "regionList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/production/region", params, "regionList")
 
    def RenewableSmForecast(self, startDate, endDate):
        """YEKDEM Üretim Tahmini Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMForecastList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-forecast", params, "renewableSMForecastList")
 
    def RenewableSmImbalanceCost(self, startDate, endDate):
        """YEKDEM Dengesizlik Maliyeti Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMImbalanceCostList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-imbalance-cost", params, "renewableSMImbalanceCostList")
 
    def RenewableSmImbalanceQuantity(self, startDate, endDate):
        """YEKDEM Dengesizlik Miktarı Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMImbalanceQuantityList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-imbalance-quantity", params, "renewableSMImbalanceQuantityList")
 
    def RenewableSmLicensedInjectionQuantity(self, startDate, endDate):
        """(YEKDEM) Licensed Generation Amount Injection Quantity Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "statistics" : []
                       "renewableSMProductionList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-licensed-injection-quantity", params, "statistics,renewableSMProductionList")
 
    def RenewableSmLicensedPowerPlantList(self, period):
        """(YEKDEM) Power Plants Rest Service
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "powerPlantList" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/production/renewable-sm-licensed-power-plant-list", params, "powerPlantList")
 
    def RenewableSmLicensedRealTimeGeneration(self, startDate, endDate):
        """(YEKDEM) Licensed Generation Amount Real Time Generation Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableLicencedGenerationAmount" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-licensed-real-time-generation", params, "renewableLicencedGenerationAmount")
 
    def RenewableSmLicensedRealTimeGeneration_with_powerplant(self, startDate, endDate, powerPlantId):
        """(YEKDEM) Licensed Generation Amount Real Time Generation With Power Plant Parameter Rest Service 
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            powerPlantId {integer} -- Santral ID bilgisi .Örn:415
 
        Returns:
            {json} -- {
                       "renewableLicencedGenerationAmount" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "powerPlantId" : powerPlantId }
        return self.__consumeAPI("/production/renewable-sm-licensed-real-time-generation_with_powerplant", params, "renewableLicencedGenerationAmount")
 
    def RenewableSmPortfolioIncome(self, startDate, endDate):
        """Yekdem Portföy Geliri Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMPortfolioIncomeList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-portfolio-income", params, "renewableSMPortfolioIncomeList")
 
    def RenewableSmProduction(self, startDate, endDate):
        """YEKDEM Üretim Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMProductionList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-production", params, "renewableSMProductionList,statistics")
 
    def RenewableSmSpotOrder(self, startDate, endDate):
        """YEKDEM Spot Teklif Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMSpotOrderList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-spot-order", params, "renewableSMSpotOrderList")
 
    def RenewableSmUnitCost(self, startDate, endDate):
        """YEKDEM Birim Maliyet Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableSMUnitCostList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-sm-unit-cost", params, "renewableSMUnitCostList")
 
    def RenewableUnlicencedGenerationAmount(self, startDate, endDate):
        """(YEKDEM) License Exempt Generation Feed-In Amount Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewableLicencedGenerationAmount" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewable-unlicenced-generation-amount", params, "renewableLicencedGenerationAmount")
 
    def RenewablesSupport(self, startDate, endDate):
        """Yekdem Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "renewablesSupports" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/renewables-support", params, "renewablesSupports,statistics")
 
    def Sbfgp(self, organizationId, uevcbId, startDate, endDate):
        """SBFGB Rest Service
 
        Arguments:
            organizationId {integer} -- Organization ID info. Sample:415
            uevcbId {integer} -- UEVÇB ID bilgisi . Örn:415
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "dppList" : []
                       "statistics" : []
                      }
        """
        params = { "organizationId" : organizationId, "uevcbId" : uevcbId, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/sbfgp", params, "dppList,statistics")
 
    def Ssv(self, startDate, endDate):
        """Uzlaştırmaya Esas Veriş Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "ssvList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/ssv", params, "ssvList")
 
    def SsvCategorized(self, startDate, endDate):
        """UEVM Kategori Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "ssvList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/production/ssv-categorized", params, "ssvList,statistics")
 
    def Uevcb(self, period, powerPlantId):
        """UEVÇB Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
            powerPlantId {integer} -- Santral ID bilgisi .Örn:415
 
        Returns:
            {json} -- {
                       "uevcbList" : []
                      }
        """
        params = { "period" : period, "powerPlantId" : powerPlantId }
        return self.__consumeAPI("/production/uevcb", params, "uevcbList")
 
    def UrgentMarketMessage(self, startDate, endDate, regionId, messageTypeId, powerPlantId, uevcbId):
        """Piyasa Mesaj Sistem Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            regionId {integer} -- Bölge ID bilgisi. Örn:1: Türkiye
            messageTypeId {integer} -- Piyasa Mesaj Sistemi Mesaj Tip ID bilgisi . Örn:0: Santral Arızası , 2: Santral Bakımı
            powerPlantId {integer} -- Santral ID bilgisi .Örn:415
            uevcbId {integer} -- UEVÇB ID bilgisi . Örn:415
 
        Returns:
            {json} -- {
                       "urgentMarketMessageList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "regionId" : regionId, "messageTypeId" : messageTypeId, "powerPlantId" : powerPlantId, "uevcbId" : uevcbId }
        return self.__consumeAPI("/production/urgent-market-message", params, "urgentMarketMessageList")
 
    def UrgentMarketMessageType(self):
        """Piyasa Mesaj Sistemi Mesaj Tip Rest Servisi
 
        Returns:
            {json} -- {
                       "ummTypeList" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/production/urgent-market-message-type", params, "ummTypeList")
 
