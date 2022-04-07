# Future
from __future__ import annotations

# Standard Library
from typing import Literal, Optional, TypedDict

# Packages
from typing_extensions import NotRequired


##########
# Common #
##########

ImageData = TypedDict(
    "ImageData",
    {
        "size":  str,
        "#text": str
    }
)

TagData = TypedDict(
    "TagData",
    {
        "url":  str,
        "name": str
    }
)

WikiData = TypedDict(
    "WikiData",
    {
        "published": str,
        "summary":   str,
        "content":   str,
    }
)

TrackStreamableData = TypedDict(
    "TrackStreamableData",
    {
        "fulltrack": str,
        "#text":     str
    }
)

TrackArtistData = TypedDict(
    "TrackArtistData",
    {
        "url":  str,
        "name": str,
        "mbid": str
    }
)

#########
# Album #
#########

AlbumTrackPayload = TypedDict(
    "AlbumTrackPayload",
    {
        "streamable": TrackStreamableData,
        "duration":   Optional[int],
        "url":        str,
        "name":       str,
        "@attr":      dict[Literal["rank"], int],
        "artist":     TrackArtistData
    }
)

AlbumPayload = TypedDict(
    "AlbumPayload",
    {
        "artist":        str,
        "mbid":          str,
        "tags":          dict[Literal["tag"], list[TagData]],
        "playcount":     str,
        "image":         list[ImageData],
        "tracks":        dict[Literal["track"], list[AlbumTrackPayload]],
        "url":           str,
        "name":          str,
        "listeners":     str,
        "wiki":          WikiData,
        "userplaycount": NotRequired[int],
        # Same warnings on TrackPayload apply here.
    }
)

#########
# TRACK #
#########

TrackAlbumData = TypedDict(
    "TrackAlbumData",
    {
        "artist": str,
        "title":  str,
        "url":    str,
        "image":  list[ImageData]
    }
)

TrackPayload = TypedDict(
    "TrackPayload",
    {
        "name":          str,
        "url":           str,
        "duration":      str,
        "streamable":    TrackStreamableData,
        "listeners":     str,
        "playcount":     str,
        "artist":        TrackArtistData,
        "album":         TrackAlbumData,
        "toptags":       dict[Literal["tag"], TagData],
        "wiki":          WikiData,
        "userplaycount": NotRequired[str],
        "userloved":     NotRequired[str]
        # This payload can apparently contain "corrected" artist
        # and name fields however I couldn't get these to be
        # returned in my testing.
    }
)

########
# User #
########

UserRegisteredData = TypedDict(
    "UserRegisteredData",
    {
        "unixtime": str,
        "#text":    int
    }
)

UserPayload = TypedDict(
    "UserPayload",
    {
        "country":    str,
        "age":        str,
        "playcount":  str,
        "subscriber": str,
        "realname":   str,
        "playlists":  str,
        "bootstrap":  str,
        "image":      list[ImageData],
        "registered": UserRegisteredData,
        "url":        str,
        "gender":     str,
        "name":       str,
        "type":       str,
    }
)
