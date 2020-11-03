from twitter import Twitter
import time

# ISHAMASHI MENFESS TEST

tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                # I take sender_id just in case you want to know who's sent the message
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    # [RF!] is the keyword
                    # if you want to turn off the case sensitive like: priktiw, [RF!], [RF!]
                    # just use lower(message) and check it, but please remove the replace function line
                    if "[RF!]" in message:
                        # message = message.replace("[RF!]", "")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                tw.delete_dm(id)
                        else:
                            print("DM deleted because its empty..")
                            tw.delete_dm(id)
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0 or dms is None:
                time.sleep(60)

# Notifies the DM sender. Modify your message here.
def senddm(self, i, dmsender, status, postid=None, rttime=None):
    api = self.api
    url = 'https://twitter.com/'+self.me.screen_name+'/status/'+str(postid)
    if status == 'sent':
        message = {'sent': 'Post was successfully sent at '+rttime.astimezone(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M")+' WIB. Check your post here: '+url}
    elif status == 'notsent':
        message = {'notsent' : 'Post was not sent. Use the trigger prikitiw to send post.'}
    else: message = {'wrong attachment' : 'Post was not sent. Send only picture attachment (not gif/video).'}

    notifdm = api.send_direct_message(recipient_id=dmsender, text=message[status])
    #api.destroy_direct_message(int(notifdm.id))
    logging.info(f'DM No {i+1} was sent. Status = {status}')
    time.sleep(10)
    
    return

if __name__ == "__main__":
    start()