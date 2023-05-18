# Youtube Scrapping

1. Youtube Scraping API runs on google api client.
2. First user needs to update the API Key, MongoDB database username and password in the credential file.
3. All the required packages have been provided in the requirements.txt file. 
4. It is developed to scrape the Youtube Channel Details of "Collegewallah","iNeuron" & "Krish Naik". 
5. It also scrapes video details along with comments and replies of any user inputted Youtube video url.
6. All the Channel details  & Video details scraped is stored in mongo DB.
7. This application can be deployed in the Beanstalk.
8. The application uses logging to log all the information.
9. Data is scraped only for learning purpose and is deleted and app removed from deployed server.

## Output as shown below.

### Homepage:

![Homepage](https://github.com/binay94/yt_scrap/assets/116953493/0de7223e-2d8b-43b9-a99e-a320c4f57e1a)

### Video Details:

![videodetails](https://github.com/binay94/yt_scrap/assets/116953493/723f0d85-ca20-4832-a122-546479f5cfc1)

### Mongo DB:

![Mongodb op](https://github.com/binay94/yt_scrap/assets/116953493/3cfdf533-66f1-464c-a2c5-ff3c7f1d7d01)

### AWS Beanstalk Deployment:

![aws](https://github.com/binay94/yt_scrap/assets/116953493/fa7a0809-2869-4289-ba6a-de0f83ff0d6b)
