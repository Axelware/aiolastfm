# Future
from __future__ import annotations

# Packages
import aiohttp

# My stuff
from .types.common import ResponseData


__all__ = (
    "LastFmException",
    "InvalidResponse",
    "HTTPException",
    "AuthenticationFailed",
    "InvalidAPIKey",
    "ServiceOffline",
    "ServiceUnavailable",
    "APIKeySuspended",
    "RateLimitExceeded",
)


class LastFmException(Exception):
    """Base exception for all aiolastfm exceptions."""
    pass


class InvalidResponse(LastFmException):
    pass


class HTTPException(LastFmException):

    def __init__(
        self,
        response: aiohttp.ClientResponse,
        data: ResponseData,
    ) -> None:

        self._response: aiohttp.ClientResponse = response
        self._data: ResponseData = data
        self._code: int = data["error"]
        self._message: str = data["message"]

        message: str = f"{self._response.status} ({self._response.reason})"
        if self._message:
            message += f" - {self._message}"

        super().__init__(message)

    @property
    def response(self) -> aiohttp.ClientResponse:
        return self._response

    @property
    def data(self) -> ResponseData:
        return self._data

    @property
    def code(self) -> int:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    @property
    def status(self) -> int:
        return self._response.status


class AuthenticationFailed(HTTPException):
    pass


class InvalidParameters(HTTPException):
    pass


class InvalidAPIKey(HTTPException):
    pass


class ServiceOffline(HTTPException):
    pass


class ServiceUnavailable(HTTPException):
    pass


class APIKeySuspended(HTTPException):
    pass


class RateLimitExceeded(HTTPException):
    pass


_EXCEPTION_MAPPING: dict[int, type[HTTPException]] = {
    4:  AuthenticationFailed,
    6:  InvalidParameters,
    10: InvalidAPIKey,
    11: ServiceOffline,
    16: ServiceUnavailable,
    26: APIKeySuspended,
    29: RateLimitExceeded,
}
