from pytube import YouTube

link = input('Link: ')
print()

yt = YouTube(link)
print('Tittle: ' + str(yt.title))
print('Author: ' + str(yt.author))
print('Publish date: ' + str(yt.publish_date))
print()

streams = yt.streams

def print_streams(streams):
    for st in streams:
        print('ID: ' + str(st.itag))
        print('Type: ' + str(st.mime_type))
        if st.type == 'video':
            print('Resolution: ' + str(st.resolution))
            print('FPS: ' + str(st.fps))
            print('Vcodec: ' + str(st.video_codec))
        else:
            print('Resolution: ' + 'NO VIDEO')
            print('FPS: ' + 'NO VIDEO')
            print('Vcodec: ' + 'NO VIDEO')
        if st.audio_codec != None:
            print('Acodec: ' + str(st.audio_codec))
        else:
            print('Acodec: ' + 'NO AUDIO')
        print('File size: ' + str(round(st.filesize / 1024 / 1024, 2)) + ' Mb')
        print('----------------------------------------')

print_streams(streams)
print()
try:
    yt.streams.get_by_itag(int(input('Choose by ID to download: '))).download(input("Enter path to directory for saving: ").replace('\\', '/'))
    print('File was successfully saved! :)')
except:
    print('UNCORRECT INPUT')