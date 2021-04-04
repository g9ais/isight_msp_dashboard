#
#   Just TEST FILES not important
#


# import requests
# import urllib3

# def isight_api():
#     endpoint = "intersight.com"
#     path = "/api/v1/"+"AlarmAggregations"
#     url = f"https://{endpoint}"
    

#     headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     }
#     try:
#         response = requests.request("GET", url + path, headers=headers, data = payload, auth = HTTPBasicAuth(nsx_m_user,nsx_m_passwd), verify = False )
    
#         response.raise_for_status()
#     except requests.exceptions.HTTPError as errh:
#         print ("Http Error:",errh)
#         print("exiting...")
#         sys.exit(1)
#     except requests.exceptions.ConnectionError as errc:
#         print ("Error Connecting:",errc)
#         print("exiting...")
#         sys.exit(1)
#     except requests.exceptions.Timeout as errt:
#         print ("Timeout Error:",errt)
#         print("exiting...")
#         sys.exit(1)
#     except requests.exceptions.RequestException as err:
#         print ("OOps: Something Else",err)
#         print("exiting...")
#         sys.exit(1)

#     return response.json()



import time
import datetime
import intersight
from intersight.api import aaa_api
from intersight.model.aaa_audit_record import AaaAuditRecord
from intersight.api import cond_api
from intersight.model.cond_alarm_aggregation import CondAlarmAggregation
from intersight.model.error import Error
from pprint import pprint
from account_details import keyID


# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
# configuration = intersight.Configuration(
#     host = "https://intersight.com"
# )
# print ("first intersight config")
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
# configuration.api_key['cookieAuth'] = keyID #'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See intersight.signing for a list of all supported parameters.
configuration = intersight.Configuration(
    host = "https://intersight.com",
    signing_info = intersight.signing.HttpSigningConfiguration(
        key_id = keyID, #'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = None,
        signing_scheme = intersight.signing.SCHEME_RSA_SHA256,
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15,
        hash_algorithm = intersight.signing.HASH_SHA256,
        signed_headers = [
                            intersight.signing.HEADER_REQUEST_TARGET,
                            intersight.signing.HEADER_CREATED,
                            intersight.signing.HEADER_EXPIRES,
                            intersight.signing.HEADER_HOST,
                            intersight.signing.HEADER_DATE,
                            intersight.signing.HEADER_DIGEST,
                            'Content-Type',
                            #'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)
print ("second intersight config")
# Configure OAuth2 access token for authorization: oAuth2
# configuration = intersight.Configuration(
#     host = "https://intersight.com"
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oAuth2
# configuration = intersight.Configuration(
#     host = "https://intersight.com"
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with intersight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    print ("will create API instance")
    #api_client.set_default_header('referer', args.url)
    api_client.set_default_header('x-requested-with', 'XMLHttpRequest')
    api_client.set_default_header('Content-Type', 'application/json')
    api_instance = cond_api.CondApi(api_client)
    moid = "600764aa65696e2d3290c6ee" #"Moid_example" # str | The unique Moid identifier of a resource instance.
    print ("created API instance")
    # example passing only required values which don't have defaults set
    try:
        # Read a 'aaa.AuditRecord' resource.
        api_response = api_instance.get_cond_alarm_list(filter="Severity eq Critical")
        pprint(api_response)
    except intersight.ApiException as e:
        print("Exception when calling CondApi->get_cond_alarm_aggregation_by_moid: %s\n" % e)






