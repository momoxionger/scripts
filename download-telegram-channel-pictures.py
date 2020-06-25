from telethon import TelegramClient,sync
import socks #如果你不需要通过代理连接Telegram，可以删掉这一行
from telethon.tl.types import InputMessagesFilterPhotos
proxy = None
# =============需要被替换的值=================
'''
api_id 你的api id
api_hash 你的api hash
channel_link 要下载图片的频道链接
proxy 将localhost改成代理地址,12345改成代理端口
picture_storage_path 图片下载到的路径
'''
api_id = 1567248
api_hash = "c1b4ab69dbb4f815bdd25b6c0451915a"
channel_link = "https://t.me/manyhotgirls"
proxy =(socks.SOCKS5,"192.168.0.2",1080) #不需要代理的话删掉该行
picture_storage_path = "/mnt/sda1/secret/Pictures"
# ==========================================
client = TelegramClient('my_session',api_id=api_id,api_hash=api_hash,proxy=proxy).start()
    
photos = client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)
    
total = len(photos)
index = 0
for photo in photos:
    filename = picture_storage_path + "/" +str(photo.id) + ".jpg"
    index = index + 1
    print("downloading:", index, "/", total, " : ", filename)
    client.download_media(photo, filename)
    
client.disconnect()
print("Done.")
