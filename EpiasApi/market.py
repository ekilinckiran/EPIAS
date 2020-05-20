
from EpiasApi.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def AmountOfBlock(self, startDate, endDate):
        """GÖP Blok Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "amountOfBlockList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/amount-of-block", params, "amountOfBlockList,statistics")
 
    def BilateralContract(self, startDate, endDate):
        """İkili Anlaşma Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bilateralContractList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/bilateral-contract", params, "bilateralContractList")
 
    def BilateralContractAll(self, eic, startDate, endDate):
        """İkili Anlaşma Alış-Satış Servisi
 
        Arguments:
            eic {string} -- 
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bilateralContracts" : []
                       "statistics" : []
                      }
        """
        params = { "eic" : eic, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/bilateral-contract-all", params, "bilateralContracts,statistics")
 
    def BilateralContractBuy(self, eic, startDate, endDate):
        """İkili Anlaşma Alış Rest Servisi
 
        Arguments:
            eic {string} -- 
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bilateralContractBuyList" : []
                      }
        """
        params = { "eic" : eic, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/bilateral-contract-buy", params, "bilateralContractBuyList")
 
    def BilateralContractSell(self, eic, startDate, endDate):
        """İkili Anlaşma Satış Rest Servisi
 
        Arguments:
            eic {string} -- 
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "bilateralContractSellList" : []
                      }
        """
        params = { "eic" : eic, "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/bilateral-contract-sell", params, "bilateralContractSellList")
 
    def BpmOrderSummary(self, startDate, endDate):
        """DGP Talimat Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "statistics" : []
                       "bpmorderSummaryList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/bpm-order-summary", params, "statistics,bpmorderSummaryList")
 
    def DayAheadDiffFunds(self, startDate, endDate):
        """GÖP Fark Tutarı Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "diffFundList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/day-ahead-diff-funds", params, "diffFundList,statistics")
 
    def DayAheadInterimMcp(self, date):
        """GÖP Kesinleşmemiş PTF Rest Servisi
 
        Arguments:
            date {string} -- 
 
        Returns:
            {json} -- {
                       "interimMCPList" : []
                      }
        """
        params = { "date" : date }
        return self.__consumeAPI("/market/day-ahead-interim-mcp", params, "interimMCPList")
 
    def DayAheadMarketIncomeSummary(self, startDate, endDate, period):
        """GÖP İşlem Tutarı Toplam Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "incomes" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/day-ahead-market-income-summary", params, "incomes,statistics")
 
    def DayAheadMarketTradeVolume(self, startDate, endDate):
        """GÖP Hacim Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "dayAheadMarketTradeVolumeList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/day-ahead-market-trade-volume", params, "dayAheadMarketTradeVolumeList,statistics")
 
    def DayAheadMarketVolume(self, startDate, endDate, eic):
        """Gün Öncesi Piyasası Eşleşme Miktar Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            eic {string} -- Organizasyon EIC bilgisi . Örn:40X000000000540Y
 
        Returns:
            {json} -- {
                       "dayAheadMarketVolumeList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "eic" : eic }
        return self.__consumeAPI("/market/day-ahead-market-volume", params, "dayAheadMarketVolumeList,statistics")
 
    def DayAheadMarketVolumeSummary(self, startDate, endDate, period):
        """GÖP Eşleşme Miktarı Aritmetik Ortalama Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "volumes" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/day-ahead-market-volume-summary", params, "volumes,statistics")
 
    def DayAheadMcp(self, startDate, endDate):
        """Piyasa Takas Fiyat Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "dayAheadMCPList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/day-ahead-mcp", params, "dayAheadMCPList,statistics")
 
    def EnergyImbalanceHourly(self, startDate, endDate):
        """Enerji Dengesizlik Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "energyImbalances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/energy-imbalance-hourly", params, "energyImbalances,statistics")
 
    def EnergyImbalanceMonthly(self, startDate, endDate):
        """AylıkEnerji Dengesizlik Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "energyImbalances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/energy-imbalance-monthly", params, "energyImbalances,statistics")
 
    def ImbalanceAmount(self, startDate, endDate):
        """Dengesizlik Tutar Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "imbalanceAmountList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/imbalance-amount", params, "imbalanceAmountList")
 
    def ImbalanceQuantity(self, startDate, endDate):
        """Dengesizlik Miktar Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "imbalanceQuantityList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/imbalance-quantity", params, "imbalanceQuantityList")
 
    def IntraDayAof(self, startDate, endDate):
        """GİP Ağırlıklı Ortalama Fiyat Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "idmAofList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/intra-day-aof", params, "idmAofList,statistics")
 
    def IntraDayAofAverage(self, startDate, endDate, period):
        """GİP AOF Aritmetik Ortalama Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "idmAofList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/intra-day-aof-average", params, "idmAofList,statistics")
 
    def IntraDayIncome(self, startDate, endDate):
        """GİP İşlem Hacmi Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "incomes" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/intra-day-income", params, "incomes,statistics")
 
    def IntraDayIncomeSummary(self, startDate, endDate, period):
        """GİP İşlem Tutarı Toplam Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "incomes" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/intra-day-income-summary", params, "incomes,statistics")
 
    def IntraDayMinMaxPrice(self, startDate, endDate, offerType):
        """Güniçi Piyasası Teklif Edilen ve Eşleşme  Fiyatlarının minimum ve maksimum değerleri
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            offerType {string} -- Güniçi Piyasası Teklif Tipi
 
        Returns:
            {json} -- {
                       "minMaxPriceList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "offerType" : offerType }
        return self.__consumeAPI("/market/intra-day-min-max-price", params, "minMaxPriceList,statistics")
 
    def IntraDayQuantity(self, startDate, endDate):
        """Güniçi Piyasası Teklif Edilen Miktar(Saatlik)
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "offerQuantities" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/intra-day-quantity", params, "offerQuantities,statistics")
 
    def IntraDaySummary(self, startDate, endDate, offerType):
        """Gün İçi Piyasası Özet Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            offerType {string} -- Güniçi Piyasası Teklif Tipi
 
        Returns:
            {json} -- {
                       "intraDaySummaryList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "offerType" : offerType }
        return self.__consumeAPI("/market/intra-day-summary", params, "intraDaySummaryList,statistics")
 
    def IntraDayTradeHistory(self, startDate, endDate):
        """GİP Eşleşme Bilgisi Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "intraDayTradeHistoryList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/intra-day-trade-history", params, "intraDayTradeHistoryList,statistics")
 
    def IntraDayVolume(self, startDate, endDate):
        """Güniçi Piyasası Saatlik Eşleşme Miktar Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "matchDetails" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/intra-day-volume", params, "matchDetails,statistics")
 
    def IntraDayVolumeSummary(self, startDate, endDate, period):
        """GİP Eşleşme Miktarı Toplam Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "volumes" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/intra-day-volume-summary", params, "volumes,statistics")
 
    def MarketVolume(self, startDate, endDate, period):
        """Elektrik Piyasalarının  Hacim Bilgisi Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "marketVolumeList" : []
                       "statistics" : []
                       "ratios" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/market-volume", params, "marketVolumeList,statistics,ratios")
 
    def McpAverage(self, startDate, endDate, period):
        """GÖP Takas Fiyatı Aritmetik Ortalama Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "dayAheadMCPList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/mcp-average", params, "dayAheadMCPList,statistics")
 
    def McpSmp(self, startDate, endDate):
        """PTF-SMF Listeleme Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "mcpSmps" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/mcp-smp", params, "mcpSmps,statistics")
 
    def Participant(self, period):
        """Lisans Tipine Göre Katılımcı Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "participantList" : []
                       "ratios" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/market/participant", params, "participantList,ratios")
 
    def PfcAmount(self, startDate, endDate):
        """Primary Frequency Capacity Amount
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "frequencyReservePriceList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/pfc-amount", params, "frequencyReservePriceList")
 
    def PfcPrice(self, startDate, endDate):
        """Primary Frequency Capacity Price Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "frequencyReservePriceList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/pfc-price", params, "frequencyReservePriceList")
 
    def SfcAmount(self, startDate, endDate):
        """Secondary Frequency Capacity Amount
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "frequencyReservePriceList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/sfc-amount", params, "frequencyReservePriceList")
 
    def SfcPrice(self, startDate, endDate):
        """Secondary Frequency Capacity Price Rest Service
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "frequencyReservePriceList" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/sfc-price", params, "frequencyReservePriceList")
 
    def Smp(self, startDate, endDate):
        """SMF Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "smpList" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/market/smp", params, "smpList,statistics")
 
    def SmpAverage(self, startDate, endDate, period):
        """DGP Sistem Marjinal Fiyatı Aritmetik Ortalama Rest Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Bitiş tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "prices" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/market/smp-average", params, "prices,statistics")
 
    def SupplyDemandCurve(self, period):
        """Arz-Talep Eğrisi Rest Servisi
 
        Arguments:
            period {string} -- Dönem bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "supplyDemandCurves" : []
                      }
        """
        params = { "period" : period }
        return self.__consumeAPI("/market/supply-demand-curve", params, "supplyDemandCurves")
 
    def SupplyDemandCurveHour(self, hour):
        """Arz-Talep Eğrisi Rest Servisi (Saatlik)
 
        Arguments:
            hour {string} -- İlgili değerin geçerli olduğu tarihi bilgisi. Örn:2016-01-01T00:00
 
        Returns:
            {json} -- {
                       "supplyDemandCurves" : []
                      }
        """
        params = { "hour" : hour }
        return self.__consumeAPI("/market/supply-demand-curve-hour", params, "supplyDemandCurves")
 
