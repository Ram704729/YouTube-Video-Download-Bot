import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("8203070075:AAHIF6x7U6ONS0y_syq1P9wpBGvpp32Yihk", "")
    API_ID = int(os.environ.get("20136843", ))
    API_HASH = os.environ.get("87002b82eb56b8e980a5d61d68e5fe07", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
