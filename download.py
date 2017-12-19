#! /usr/bin/python3

r"""download youtube-dl supported site's video from csv

thats all, what you think of
"""


from __future__ import unicode_literals
import csv
import youtube_dl


class CSVDownloader():
    r"""that the main logic for downloding videos

    hell yeah!!!
    """

    def __init__(self, filename):
        self.filename = filename

    def get_videos(self):
        r"""get video from csv file

        open a csv file and add unique video url into list

        Returns:
            list -- list of videos
        """

        videos = []
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                for col in row:
                    videos.append(col)
        videos = list(filter(None, list(set(videos))))
        return videos

    def save_file(self, videos):
        r"""save list of videos in file

        thats it

        Arguments:
            videos {list} -- list of videos
        """

        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
            for video in videos:
                writer.writerow([video])


    def start(self):
        r"""here we start the downloading

        cool
        """

        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            while True:
                videos = self.get_videos() # getting list of all videos from file
                print('{} videos to go'.format(len(videos))) # print no. of video remaining
                video = get_first_item(videos) # get next video for downloading
                if video is None: # check if video is there or not
                    break

                ydl.download([video]) # downloading video
                videos.remove(video) # remove video from list
                self.save_file(videos) # save updated list to file

        print('All downloaded')


def get_first_item(videos):
    r"""return first item from list if found otherwise none

    okk

    Arguments:
        videos {list} -- list of videos

    Returns:
        str|None -- first url of video from list or none
    """

    return next(iter(videos or []), None)

def main():
    r"""nothing just run the code

    bcz of make sure it is run from terminal directly
    """

    handler = CSVDownloader('download.csv')
    handler.start()

if __name__ == '__main__':
    main()
