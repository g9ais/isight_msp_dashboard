import intersight
from intersight.intersight_api_client import IntersightApiClient
import account_details
from intersight.api import cond_api
from intersight.model.cond_alarm_aggregation import CondAlarmAggregation

api_instance = IntersightApiClient(
    host=account_details.baseurl,
    private_key=account_details.pvk_file,
    api_key_id=account_details.keyID
)

cond_handle = cond_api.condApi(api_instance)
moid = "600764aa65696e2d3290c6ee" #"Moid_example" # str | The unique Moid identifier of a resource instance.
print ("created API instance")
    # example passing only required values which don't have defaults set
api_response = cond_handle.get_cond_alarm_by_moid(moid)
pprint(api_response)


