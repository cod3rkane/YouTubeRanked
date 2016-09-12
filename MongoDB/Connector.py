from pymongo import MongoClient

class YTRankedConnect(object):

  def __init__(self, host='localhost', port=27017):
    self.__host = host
    self.__port = port

  def init(self):
    """ Here connect in MongoClient ytRanked and set-up YTRankedConnect properties. """
    self.__client = MongoClient(host=self.__host, port=self.__port)
    self.__channels = self.__client.ytRanked.channels
    self.__videos = self.__client.ytRanked.videos

  @property
  def channels(self):
      return self.__channels

  @channels.setter
  def channels(self, value):
      self.__channels = value

  @channels.deleter
  def channels(self):
      del self.__channels

  @property
  def videos(self):
      return self.__videos

  @videos.setter
  def videos(self, value):
      self.__videos = value

  @videos.deleter
  def videos(self):
    del self.__videos