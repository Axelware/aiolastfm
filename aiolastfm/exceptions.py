# Future
from __future__ import annotations

# Packages
import aiohttp

# Local
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

        self.response: aiohttp.ClientResponse = response
        self.data: ResponseData = data

        self.status: int = response.status

        self.error_code: int = data["error"]
        self.error_message: str = data["message"]

        self.message: str = f"{response.status} ({response.reason}) - {self.error_message}"

    def __str__(self) -> str:
        return self.message


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
