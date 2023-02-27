
import time

class Message:

    def __init__(self, src, dest,  data):

        self.src = src
        self.dest = dest
        self.data = data
        self.timestamp = time.ctime()


    def __str__(self):

        return f'({self.timestamp})  {self.src} --> {self.dest}  :  "{self.data}" '



    
