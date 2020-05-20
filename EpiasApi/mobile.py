
from Api.EndPoint import _EpiasApi

class EpiasApi(_EpiasApi):    
    """ Transparency API
    """
    def FinalConciliationPeriod(self):
        """Last Conciliation Period Rest Service
 
        Returns:
            {json} -- {
                       "topic" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/mobile/final-conciliation-period", params, "topic")
 
    def Topics(self):
        """Mobil Uygulama Topic Listeleme
 
        Returns:
            {json} -- {
                       "topics" : []
                      }
        """
        params = {}
        return self.__consumeAPI("/mobile/topics", params, "topics")
 
    def UserTopics(self, uid):
        """Mobil Uygulama Kullanıcı Topic Listeleme
 
        Arguments:
            uid {string} -- 
 
        Returns:
            {json} -- {
                       "topic" : []
                      }
        """
        params = { "uid" : uid }
        return self.__consumeAPI("/mobile/user-topics", params, "topic")
 
