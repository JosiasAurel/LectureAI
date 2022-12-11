import requests
import csv
# import moviepy.editor as mp

# # You will start by running this one it will do all the post requests
# filename = "/Users/petermue/Downloads/tailor"


# # Insert Local Video File Path
# clip = mp.VideoFileClip(filename+'.mp4')

# # Insert Local Audio File Path
# clip.audio.write_audiofile(filename+'.mp3')
# # endpoint = "https://api.assemblyai.com/v2/transcript"
filename = "tailor.mp3"


def post1(name):
    def read_file(nam, chunk_size=5242880):
        with open(nam, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    # Here im looking for the url of the audio
    headers = {'authorization': "8ac213c99e23428e84bf7b0801f4dc6a"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(name))
    # upload url
    url2 = response.json()['upload_url']
    return url2

# I get that url and then send the actual post request to the api


def post2(url, num):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {"audio_url": url, "auto_chapters": True}
    headers = {
        "authorization": "8ac213c99e23428e84bf7b0801f4dc6a",
        "content-type": "application/json"
    }
    response1 = requests.post(endpoint, json=json, headers=headers)
    id_ = response1.json()["id"]

    return id_
    # a certain token is stored in something (very useful)
