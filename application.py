from flask import Flask, render_template, request
import logging
from build import yt
from utility import yt_details
from mongo_op import add_to_mongo

obj = yt_details()
youtube = yt()


application = Flask(__name__)
app=application
# Set up logging
logging.basicConfig(filename = "Youtube.log",level = logging.DEBUG,filemode = 'w', format = "%(asctime)s %(levelname)s %(message)s")



@app.route('/')
def homePage():
    logging.info("Homepage Displayed")
    return render_template("index.html")
    


@app.route('/stats', methods=['POST'])
def channel_details():
    channel = request.form.get('channel')
    try:
        logging.info("Initiating retrival of channel details")
        channel_name,subscriber_count,view_count,video_count=obj.channel_stats(channel)
        channel_data = {"name": channel_name, "subscribers": subscriber_count, "views": view_count, "videos": video_count}
        add_to_mongo(channel_data, None)
        logging.info("channel details added to mongo db")
        return render_template('channel_result.html',channel_name=channel_name, subscriber_count=subscriber_count, view_count=view_count, video_count=video_count)
    
        
    except Exception as e:
        logging.exception(str(e))
        return str(e)

@app.route('/video_details', methods=['GET', 'POST'])
def vid_details():
    try:
        logging.info("Initiating retrival of video details")
        if request.method == 'POST':
            # Get the YouTube video URL from the form
            video_url = request.form.get("video_url")
            # Extract the video ID from the URL
            video_id = video_url.split("=")[1]
            video_details,comments_list = obj.get_video_details(video_id)
            # Add video data to MongoDB
            video_data = {"details": video_details, "comments": comments_list}
            add_to_mongo({}, video_data)
            logging.info("Comments & Video details added to mongo db")
            return render_template("video_result.html", video_details=video_details, comments_list=comments_list)
        
    except Exception as e:
        logging.exception(str(e))
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
