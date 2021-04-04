# isight_msp_dashboard

This project means to be a demo for an MSP to be able to check the alarms of every one of its managed customer.
For this, the MSP has to have an account in customer intersight and need to generate an API Key + Private key certificate.
The MSP needs to generate a simple json file with a list of dicts representing each customer, with its API key and private key file location.
All keys are currently on the former v2 legacy format.
This script uses intersight python API downloadable from https://intersight.com/apidocs/downloads/

I added a Flask fronted to the script with a simple page that periodically refreshes and gets the current unacknowledged Alarms (Critical and Warning) as well as a link to the direct intersight page.
Nothing fancy.

Current:
- api keys supported are only  RSA keys with 2048 bits, RSA SSA PKCS1 v1.5 signature algorithm, and SHA256 cryptographic hash


To do:
- add support to new API key generation based in FIPS 186-4 P256 elliptic curve key, ECDSA signature algorithm, and SHA256 cryptographic hash
- add web based way to add clients to page
- add secure storage to fetch private keys in Vault
- cosmetics

Lessons Learned:
- Intersight is tricky in regards to HTTP Auth, only supports HTTP Digest Auth, where body of message is digested and added to header. 
- Intersight Handbook is an **excellent** reference to start.

Basically this made all the difference while trying to access isight.
```
    Legacy API (2k,PKCSv1.5,SHA256)
        signing_scheme = intersight.signing.SCHEME_RSA_SHA256
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
    New API (FIPS 186-4 P256 Elliptic, ECDSA, SHA256)
        signing_scheme = intersight.signing.SCHEME_HS2019
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3
```
