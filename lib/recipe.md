# {{MUSIC_TRACKER}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker():
    # User-facing properties:
    #   name: string

    def __init__(self):
     
        # Parameters:
        # music_list= []
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_(self, song):
        # Parameters:
        #   task: string representing a single song
        # Returns:
        #   Nothing
        # Side-effects
        #   add new song to list 
        pass # No code here yet
   

    def display(self):
        # Returns:
        #   A list of songs 
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Check if the list is empty - initialise the object

"""
def test_check_empty_list():
   music_tracker = MusicTracker()
   assert 
   empty list or # => []
"""
Check if the song is added

"""
def test_if_song_is_added():
   music_tracker = MusicTracker()
   assert 
   boolean # => boolean

"""
Check if song is not a string 

"""
def test_if_song_is_not_string():
   music_tracker = MusicTracker()
   assert 
   error message # =>"input is not a string"
"""
Check if multiple songs are added

"""
def test_if_multiple_songs_are_added():
   music_tracker = MusicTracker()
   assert 
   error message # => "This song has already been added"

```
