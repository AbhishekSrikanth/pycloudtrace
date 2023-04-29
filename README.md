# pycloudtrace

The `pycloudtrace` library provides a Python function for parsing data from the Cloudflare CDN "https://1.1.1.1/cdn-cgi/trace" endpoint. This endpoint provides information about the client's network and device, such as the IP address, location, and HTTP headers.

## Installation

``` bash
pip install pycloudtrace
```

## Usage

``` python
from pycloudtrace import cdn_trace

data = cdn_trace()
```

## Contributing

Pull requests are welcome!
