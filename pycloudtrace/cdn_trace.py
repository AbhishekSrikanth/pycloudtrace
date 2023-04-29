"""
This module contains functions for parsing data from the "https://1.1.1.1/cdn-cgi/trace"
endpoint. The endpoint provides information about the client's network and device, such as
the IP address, location, and HTTP headers.
"""

import requests


def _get_trace_from_cl() -> str:
    trace_response = requests.get("https://1.1.1.1/cdn-cgi/trace", timeout=10)
    return trace_response.text


def _parse_trace(trace_response: str) -> dict:
    trace = {}
    lines = trace_response.splitlines()

    for line in lines:

        key, value = line.split("=")
        trace[key] = value

    return trace


def cdn_trace() -> dict:
    """
    Sends a GET request to the "https://1.1.1.1/cdn-cgi/trace" endpoint and
    parses the plaintext response to extract relevant information about the client's network
    and device.

    Returns:
    A dictionary containing the parsed data. The dictionary has the following keys:
    - "fl": a string representing the Cloudflare data center that served the request
    - "h": a string representing the client's IP address
    - "proto": a string representing the HTTP protocol version used in the request
    - "tls": a string representing the TLS version and cipher suite being used
    - "sni": a string representing the server name indication (SNI) sent by the client, if any
    - "http": a string representing any HTTP headers sent by the client
    - "loc": a string representing the approximate location of the client's IP address, if available
    - "ip": a string representing the IP address of the client's outgoing interface, if available

    Raises:
    - RequestsException: if the GET request to the endpoint fails
    - ValueError: if the plaintext response from the endpoint cannot be parsed
    """
    trace_response = _get_trace_from_cl()
    return _parse_trace(trace_response=trace_response)
