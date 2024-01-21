import asyncio
import socket
from urllib.parse import urljoin

import aiohttp
import async_timeout

from .const import API_URL


class EmeraldApiClientError(Exception):
    """Exception to indicate a general API error."""


class EmeraldApiClientCommunicationError(EmeraldApiClientError):
    """Exception to indicate a communication error."""


class EmeraldApiClientAuthenticationError(EmeraldApiClientError):
    """Exception to indicate an authentication error."""


class EmeraldApiClient:
    def __init__(
        self,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
    ) -> None:
        self._username = username
        self._password = password
        self._session = session

    async def sign_in(self) -> str:
        """Sign-in using username & password and return the access token."""
        return await self._api_wrapper(
            method="post", url=urljoin(API_URL, "/customers/sign-in")
        )

    async def get_properties(self) -> any:
        """Get data from the API."""
        return await self._api_wrapper(
            method="get", url=urljoin(API_URL, "/customers/s")
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                if response.status in (401, 403):
                    raise EmeraldApiClientAuthenticationError(
                        "Invalid credentials",
                    )
                response.raise_for_status()
                return await response.json()

        except asyncio.TimeoutError as exception:
            raise EmeraldApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise EmeraldApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            raise EmeraldApiClientError(
                "Something really wrong happened!"
            ) from exception
