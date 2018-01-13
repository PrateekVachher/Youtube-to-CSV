def get_data():
  import os, pickle
  import google.oauth2.credentials
  from googleapiclient.discovery import build
  from googleapiclient.errors import HttpError
  from google_auth_oauthlib.flow import InstalledAppFlow

  CLIENT_SECRETS_FILE = "youtube_client_secret.json"
  SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
  API_SERVICE_NAME = 'youtube'
  API_VERSION = 'v3'

  def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
  
  def search_list_by_keyword(client, **kwargs):
    response = client.search().list(
      **kwargs
    ).execute()
    return(response)

  print()
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()

  file_open_1 = open('datafiles/AA_SPEAKER.dat','wb') 
  data_1 = search_list_by_keyword(service, part='snippet', maxResults=50, q='AA speaker', type='')
  pickle.dump(data_1,file_open_1)
  file_open_1.close()

  file_open_2 = open('datafiles/NA_SPEAKER.dat','wb') 
  data_2 = search_list_by_keyword(service, part='snippet', maxResults=50, q='NA speaker', type='')
  pickle.dump(data_2,file_open_2)
  file_open_2.close()
  print()