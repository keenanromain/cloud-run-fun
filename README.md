# cloud-run-fun
A proof-of-concept application to explore CI/CD on Google Cloud. The application gets rebuilt on every new commit to this repository and publicly exposes two endpoints; `/health` and `/hello`. 
The successful build can be affirmed via a cURL response or through the browser:

```
$ curl -i "https://no-keys-git-push-to-start-qbarc2y7rq-uc.a.run.app/hello"

HTTP/2 200
content-type: application/json
date: Sun, 23 Aug 2020 23:11:16 GMT
server: Google Frontend
content-length: 18
alt-svc: h3-29=":443"; ma=2592000,h3-27=":443"; ma=2592000,h3-T050=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

{"hello":"world"}
```

I will write a walkthrough over the next few days and build a more robust application.
