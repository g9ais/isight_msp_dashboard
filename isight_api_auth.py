import datetime
import intersight
from pprint import pprint

def config_credentials(description=None, api_key_id = None, pvk_path = None, ignore_tls = False, api_url = "https://intersight.com"):
    """config_credentials configures and returns an Intersight api client
    Intersight only allows for HPPT Authentication digest. For more info consult intersight handbook.
    Returns:
        apiClient [intersight.api_client.ApiClient]: base intersight api client class
    """    
    api_key_legacy = True #if False will have error  - Signing algorithm fips-186-3 is not compatible with private key
    ignore_tls = False


    if api_key_id:
        # HTTP signature scheme.
        if api_key_legacy:
            signing_scheme = intersight.signing.SCHEME_RSA_SHA256
            signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        else:
            signing_scheme = intersight.signing.SCHEME_HS2019
            signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3

        configuration = intersight.Configuration(
            host=api_url,
            signing_info=intersight.HttpSigningConfiguration(
                key_id=api_key_id,
                private_key_path=pvk_path,
                signing_scheme=signing_scheme,
                signing_algorithm=signing_algorithm,
                hash_algorithm=intersight.signing.HASH_SHA256,
                signed_headers=[intersight.signing.HEADER_REQUEST_TARGET,
                                intersight.signing.HEADER_CREATED,
                                intersight.signing.HEADER_EXPIRES,
                                intersight.signing.HEADER_HOST,
                                intersight.signing.HEADER_DATE,
                                intersight.signing.HEADER_DIGEST,
                                'Content-Type',
                                'User-Agent'
                                ],
                signature_max_validity=datetime.timedelta(minutes=5)
            )
        )
    else:
        raise Exception('Must provide API key information to configure ' +
            'at least one authentication scheme')

    if ignore_tls:
        configuration.verify_ssl = False

    apiClient = intersight.ApiClient(configuration)
    apiClient.set_default_header('referer', api_url)
    apiClient.set_default_header('x-requested-with', 'XMLHttpRequest')
    apiClient.set_default_header('Content-Type', 'application/json')

    return apiClient


if __name__ == "__main__":
    api_client = config_credentials(api_key_id = keyID, pvk_path= pvk_file)
