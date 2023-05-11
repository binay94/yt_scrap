from pymongo import MongoClient
from credentials import username, password
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def add_to_mongo(channel_data,video_data):
    try:
        
        client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ojgbawe.mongodb.net/?retryWrites=true&w=majority")
        db = client["yt"]


        #insert channel data
        channel_details_collection = db["channel_details"]
        channel_details_collection.insert_one(channel_data)
        logging.debug("Channel data inserted into MongoDB.")
    
        # Insert the video details and comments list into the "videos" collection
        video_details_collection = db["video_details"]
        video_details_collection.insert_one(video_data)
        logging.debug("Video data inserted into MongoDB.")

        client.close()
        logging.debug("MongoDB connection closed.")

    except Exception as e:
        logging.exception(f"Error inserting data into MongoDB: {e}")
        return e

    


