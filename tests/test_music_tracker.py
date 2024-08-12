from lib.music_tracker import MusicTracker
import pytest



def test_check_lempty_list():
    music_tracker = MusicTracker()
    assert music_tracker.display() == []


def test_if_song_is_added():
    music_tracker = MusicTracker()
    music_tracker.add("song1")
    assert music_tracker.display() == ["song1"]

def test_if_song_is_not_string():
    with pytest.raises(ValueError):
        music_tracker = MusicTracker()
        assert music_tracker.add(87) == "input is not a string"

def test_if_song_is_a_boolean():
    with pytest.raises(ValueError):
        music_tracker = MusicTracker()
        assert music_tracker.add(True) == "input is not a string"

def test_if_multiple_songs_are_added():
    music_tracker = MusicTracker()
    music_tracker.add("song1")
    music_tracker.add("song2")
    assert music_tracker.display() == ["song1","song2"]


def test_check_if_song_has_been_already_added():
    with pytest.raises(ValueError):
        music_tracker = MusicTracker()
        music_tracker.add("song1")
        music_tracker.add("song1")
        assert music_tracker.add() == "This song has already been added"