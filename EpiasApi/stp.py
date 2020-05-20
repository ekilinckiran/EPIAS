
from EpiasApi.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def AdditionalNotification(self, startDate, endDate):
        """İlave dengeleyici işlemleri bildirim servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "additionalNotifications" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/additional-notification", params, "additionalNotifications")
 
    def Allowance(self, startDate, endDate):
        """Tahsisat verileri servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "allowances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/allowance", params, "allowances,statistics")
 
    def BalancingGasPrice(self, startDate, endDate):
        """STP Dengeleyici Gaz Fiyatları Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "prices" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/balancing-gas-price", params, "prices,statistics")
 
    def BluecodeOperation(self, startDate, endDate):
        """2 Kodlu ilave dengeleyici işlemler servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "operations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/bluecode-operation", params, "operations,statistics")
 
    def ContractAmount(self, startDate, endDate, period):
        """Kontrat işlem hacim ve miktar bilgisi servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "contractTradeAmounts" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/stp/contract-amount", params, "contractTradeAmounts,statistics")
 
    def DailyPrice(self, startDate, endDate):
        """STP Günlük Fiyat Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "stpDailyPriceDtos" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/daily-price", params, "stpDailyPriceDtos,statistics")
 
    def FourcodeOperation(self, startDate, endDate):
        """4 Kodlu ilave dengeleyici işlemler servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "operations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/fourcode-operation", params, "operations,statistics")
 
    def GreencodeOperation(self, startDate, endDate):
        """1 Kodlu ilave dengeleyici işlemler servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "operations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/greencode-operation", params, "operations,statistics")
 
    def Grf(self, startDate, endDate, period):
        """Gaz referans fiyat servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            period {string} -- Aritmetik alınacak dönem bilgisi.
 
        Returns:
            {json} -- {
                       "prices" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "period" : period }
        return self.__consumeAPI("/stp/grf", params, "prices,statistics")
 
    def ImbalanceMonthly(self, startDate, endDate):
        """STP Aylık Dengesizlik Miktarları Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "imbalances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/imbalance-monthly", params, "imbalances,statistics")
 
    def MatchingQuantity(self, startDate, endDate):
        """STP Eşleşme Miktar Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "matchingDtos" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/matching-quantity", params, "matchingDtos,statistics")
 
    def MatchingQuantityAdditionalQuantity(self, startDate, endDate):
        """İlave Dengeleyici ve Toplam Eşleşme Miktar Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "quantities" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/matching-quantity/additional-quantity", params, "quantities")
 
    def MobilePrice(self, startDate, endDate):
        """STP Mobil Fiyat Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "prices" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/mobile/price", params, "prices")
 
    def OrangecodeOperation(self, startDate, endDate):
        """3 Kodlu ilave dengeleyici işlemler servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "operations" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/orangecode-operation", params, "operations,statistics")
 
    def PastInvoice(self, startDate, endDate):
        """Doğalgaz GDDK Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "pastInvoices" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/past-invoice", params, "pastInvoices")
 
    def Price(self, startDate, endDate, priceType):
        """STP Fiyat Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            priceType {string} -- STP Fiyat Tipi ( GAS_REFERENCE : Gaz Referans Fiyat ,ADDITIONAL_BALANCING_PURCHASE: İlave Dengeleyici Alış Fiyat ,ADDITIONAL_BALANCING_SALE: İlave Dengeleyici Alış Fiyat , BALANCING_GAS_PURCHASE: Dengeleyici Gaz Alış Fiyatı, BALANCING_GAS_SALE:Dengeleyici Gaz Satış Fiyatı )
 
        Returns:
            {json} -- {
                       "prices" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate, "priceType" : priceType }
        return self.__consumeAPI("/stp/price", params, "prices")
 
    def TradeValue(self, startDate, endDate):
        """STP GRF Ticaret Miktar Servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "tradeValues" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/trade-value", params, "tradeValues,statistics")
 
    def TransactionHistory(self, startDate, endDate):
        """İşlem akışı servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "transactionHistories" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/transaction-history", params, "transactionHistories,statistics")
 
    def TransactionHistoryMarketStatistic(self):
        """STP Piyasa İstatistikleri Servisi
 
        Returns:
            {json} -- {
                       "marketStatistics" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/stp/transaction-history/market-statistic", params, "marketStatistics")
 
    def ZeroBalance(self, startDate, endDate):
        """Bakiye sıfırlama tutarı servisi
 
        Arguments:
            startDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
            endDate {string} -- Başlangıç tarih bilgisi. Örn:2016-01-01
 
        Returns:
            {json} -- {
                       "zeroBalances" : []
                       "statistics" : []
                      }
        """
        params = { "startDate" : startDate, "endDate" : endDate }
        return self.__consumeAPI("/stp/zero-balance", params, "zeroBalances,statistics")
 
