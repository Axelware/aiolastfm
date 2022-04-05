# Future
from __future__ import annotations

# Standard Library
from typing import Literal, Optional, TypedDict


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

#########
# Album #
#########

AlbumTrackStreamableData = TypedDict(
    "AlbumTrackStreamableData",
    {
        "fulltrack": str,
        "#text":     str
    }
)

AlbumTrackArtistData = TypedDict(
    "AlbumTrackArtistData",
    {
        "url":  str,
        "name": str,
        "mbid": str
    }
)

AlbumTrackPayload = TypedDict(
    "AlbumTrackPayload",
    {
        "streamable": AlbumTrackStreamableData,
        "duration":   Optional[int],
        "url":        str,
        "name":       str,
        "@attr":      dict[Literal["rank"], int],
        "artist":     AlbumTrackArtistData

    }
)

AlbumWikiData = TypedDict(
    "AlbumWikiData",
    {
        "published": str,
        "summary":   str,
        "content":   str,
    }
)

AlbumPayload = TypedDict(
    "AlbumPayload",
    {
        "artist":    str,
        "mbid":      str,
        "tags":      dict[Literal["tag"], list[TagData]],
        "playcount": str,
        "image":     list[ImageData],
        "tracks":    dict[Literal["track"], list[AlbumTrackPayload]],
        "url":       str,
        "name":      str,
        "listeners": str,
        "wiki":      AlbumWikiData
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
        "bootstrap":  str,
        "image":      list[ImageData],
        "registered": UserRegisteredData,
        "url":        str,
        "gender":     str,
        "name":       str,
        "type":       str,
    }
)
