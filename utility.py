import logging
from build import yt
youtube = yt()

class yt_details:
    logging.basicConfig(filename="Youtube.log", level=logging.DEBUG, filemode='w', format="%(asctime)s %(levelname)s %(message)s")
    def channel_stats(self, channel):
        if channel == 'channel1':
            channel_id = 'UCDrf0V4fcBr5FlCtKwvpfwA'
        elif channel == 'channel2':
            channel_id = 'UCb1GdqUqArXMQ3RS86lqqOw'
        else:
            channel_id = 'UCNU_lfiiWBdtULKOw6X0Dig'

        channel_response = youtube.channels().list(
                    part="snippet,contentDetails,statistics",
                    id=channel_id).execute()
        

        for data in channel_response["items"]:
            channel_name=data["snippet"]["title"]
            subscriber_count = data['statistics']['subscriberCount']
            view_count = data['statistics']['viewCount']
            video_count = data['statistics']['videoCount']
        logging.info("Channel Details retrived.")
        # Log channel statistics
        logging.info(f"Channel Name: {channel_name}")
        logging.info(f"Subscriber Count: {subscriber_count}")
        logging.info(f"View Count: {view_count}")
        logging.info(f"Video Count: {video_count}")    
        return channel_name,subscriber_count,view_count,video_count
    
    def get_video_details(self, video_id):
        try:
            req = youtube.videos().list(part='snippet,statistics,contentDetails', id=video_id)
            response = req.execute()
            video_details = {}
            for video in response['items']:
                video_details.update({
                            'Title': video['snippet']['title'],
                             'Thumbnail' : video['snippet']['thumbnails']['standard']['url'],
                            'Channel Name' : video['snippet']['channelTitle'],
                            'Published Date': video['snippet']['publishedAt'].split("T")[0],
                            'Duration': video['contentDetails']['duration'].split("PT")[1],                        
                            'Views': video['statistics']['viewCount'],
                            'Comment_Count': video['statistics']['commentCount'],
                            'Likes': video['statistics']['likeCount'],
                            'Tags' : video['snippet']['tags'][1:]
                        })

                comments = youtube.commentThreads().list(part='snippet', videoId=video_id, textFormat='plainText').execute()
                comments_list = []
                while comments:
                    for comment in comments['items']:
                        comment_dict = {
                                'Author': comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                                'Comment': comment['snippet']['topLevelComment']['snippet']['textOriginal'],
                                'Likes': comment['snippet']['topLevelComment']['snippet']['likeCount'],
                                'Time' :comment['snippet']['topLevelComment']['snippet']['publishedAt'].split("Z")[0].replace("T"," @ "),
                                
                                'replies': []
                            }

                        if comment['snippet']['totalReplyCount'] > 0:
                            replies = youtube.comments().list(part='snippet', parentId=comment['id'], textFormat='plainText').execute()
                            for reply in replies['items']:
                                reply_dict = {
                                        'Replied_By': reply['snippet']['authorDisplayName'],
                                        'Reply': reply['snippet']['textOriginal'],
                                        'reply_likes': reply['snippet']["likeCount"],
                                        'Time': reply['snippet']['publishedAt'].split("Z")[0].replace("T"," @ ")
                                        
                                    }
                                comment_dict['replies'].append(reply_dict)

                        comments_list.append(comment_dict)

                    if 'nextPageToken' in comments:
                        comments = youtube.commentThreads().list(part='snippet', videoId=video_id, 
                                                                textFormat='plainText', 
                                                                pageToken=comments['nextPageToken']).execute()
                    else:
                        break
            logging.info("Video Details retrived.")
            logging.info(f"Video Details: {video_details}")
            return (video_details,comments_list)    
        except Exception as e:
            logging.exception(str(e))
            return e
                                   
