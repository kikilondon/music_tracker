class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        self.music_list= []
        # Side effects:
        #   Sets the name property of the self object
        return 

    def add(self, song):
        if not isinstance(song,str):
            raise ValueError("input is not a string")
        if song in self.music_list:
            raise ValueError("This song has already been added")
        return  self.music_list.append(song)

    def display(self):
        # Returns:
        #   A list of songs 
        # Side-effects:
        #   Throws an exception if no task is set
        return self.music_list