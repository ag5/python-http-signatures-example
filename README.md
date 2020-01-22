# HTTP Signatures example

AG5 utilizes HTTP Signatures authentication for some of its APIs. HTTP signature authentication is implemented according to the following specification https://tools.ietf.org/html/draft-cavage-http-signatures-12.

This repository contains an example in Python to help you get started with HTTP signature authentication. The project makes use of the popular `request` package, and the `requests-http-signature` package to provide HTTP signature authentication for requests.

AG5 requires you to provide the following headers when signing a request:
  * `(request-target)`
  * `date`
  * `host`

Additionally, when making a POST or PUT request you have to provide these headers as well:
  * `digest`
  * `content-type`

The `digest` header is the SHA256 hash of the request payload and is automatically calculated for you by the `requests-http-signature` package. When implementing the digest yourself, make sure it is calculated using SHA256 and the header is formatted as follows:

```
Digest: SHA256=[base64(sha256(request-payload))]
```

For more information see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Digest.

## Installing
 
Setup the environment using `pipenv`:
 
```
 $ pipenv install
```
 
Then change the variables at the beginning in `main.py` with an actual key and url. And run it like so:
 
```
$ pipenv run python main.py
```
