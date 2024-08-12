class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.music_list= []
        return 

    def add(self, song):
        if not isinstance(song,str):
            raise ValueError("input is not a string")
        if song in self.music_list:
            raise ValueError("This song has already been added")
        return  self.music_list.append(song)

    def display(self):
        return self.music_list