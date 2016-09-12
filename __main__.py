from pymongo import MongoClient
from Youtube.YouTubeAPI import YouTubeAPI
from MongoDB.Connector import YTRankedConnect

youtube = YouTubeAPI("AIzaSyDMFVt30FPoKQwMGcZULEaChaTphbSgxyo")
youtube.init()

mongoDB = YTRankedConnect()
mongoDB.init()

if __name__ == "__main__":
  result = youtube.videosList()
  nextPageToken = ''

  for i in range(0, result['pageInfo']['totalResults'], result['pageInfo']['resultsPerPage']):
    if result is None:
      result = youtube.videosList(pageToken=nextPageToken)

    item = 0
    for video in result['items']:
      if item == int(result['pageInfo']['resultsPerPage'] - 1):
        if 'nextPageToken' in result.keys():
          nextPageToken = result['nextPageToken']
          result = None

      item += 1

      if mongoDB.videos.find({'_id': video['id']}).count() > 0:
        print("couldn't insert video in database, id: ", video['id'], " already exist")
      else:
        video['_id'] = video['id']
        mongoDB.videos.insert(video)

      channels = youtube.channelList(video['snippet']['channelId'])
      channel = channels['items'][0]

      if mongoDB.channels.find({"_id": channel['id']}).count() > 0:
        # @todo aqui precisamos checar quando foi a última vez que atualizamos os dados desse channel.
        print("couldn't insert channel in database, id: ", channel['id'], " already exist")
      else:
        channel['_id'] = channel['id']
        mongoDB.channels.insert(channel)