from googleapiclient.discovery import build

class YouTubeAPI(object):

  def __init__(self, developerKey):
    self._developerKey = developerKey
    self.__YOUTUBE_API_SERVICE_NAME = "youtube"
    self.__YOUTUBE_API_VERSION = "v3"

  @property
  def developerKey(self):
    return self._developerKey

  @developerKey.setter
  def developerKey(self, key):
    self._developerKey = key

  @developerKey.deleter
  def developerKey(self):
    del self._developerKey

  @property
  def api(self):
      return self.__api

  @api.setter
  def api(self, value):
      self.__api = value

  @api.deleter
  def api(self):
    del self.__api

  def init(self):
    """ This method set the self.__api service to interact with youtube api """
    self.__api = build(self.__YOUTUBE_API_SERVICE_NAME, self.__YOUTUBE_API_VERSION, developerKey=self._developerKey)

  def videosList(self, chart='mostPopular', regionCode='BR', maxResult=50, pageToken='', videoId=None):
    """ This method return a list of vídeos """
    return self.__api.videos().list(
    part="contentDetails, id, liveStreamingDetails, localizations, player, recordingDetails, snippet, statistics, status, topicDetails",
    chart=chart,
    regionCode=regionCode,
    maxResults=maxResult,
    pageToken=pageToken,
    id=videoId,
    ).execute()

  def channelList(self, channelId):
    """ This method return a channel by id """
    return self.__api.channels().list(
    part="contentDetails, id, localizations, snippet, statistics, status",
    id=channelId
  ).execute()