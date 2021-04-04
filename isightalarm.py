from isight_api_auth import config_credentials
import intersight
from intersight.api import cond_api
from intersight.api import iam_api
from intersight.model.cond_alarm_aggregation import CondAlarmAggregation
from intersight.model.error import Error
from pprint import pprint
from account_details import accounts


def isightinfo():
    #pprint(accounts)
    data_list=[]
    for acc in accounts:
        acc_result={}
        api_client = config_credentials(api_key_id = acc['keyID'], pvk_path=acc['pvk_file'])
        try:
            #read name
            api_iamapi_instance = iam_api.IamApi(api_client)
            api_iamapi_response = api_iamapi_instance.get_iam_account_list()#select="Name")
            #pprint(api_response1)
            pprint (f"account name {api_iamapi_response['results'][0]['name']} ; url https://{api_iamapi_response['results'][0]['account_moid']}.intersight.com")
            acc_result["name"] = api_iamapi_response['results'][0]['name']
            acc_result["url"] = f"https://{api_iamapi_response['results'][0]['account_moid']}.intersight.com"

        except intersight.ApiException as e:
            print("Exception when calling IAMAPI->get_iam_account_list: %s\n" % e)

        api_condapi_instance = cond_api.CondApi(api_client)
        #moid = "600764aa65696e2d3290c6ee" #"Moid_example" # str | The unique Moid identifier of a resource instance.
        
        # example passing only required values which don't have defaults set
        try:
            api_condapi_response = api_condapi_instance.get_cond_alarm_list( filter="Severity eq Warning and Acknowledge eq None" , count = True)
            pprint("Warnings:" + str(api_condapi_response["count"]))
            acc_result["warning"] = str(api_condapi_response["count"])
        # pprint(api_response)
            api_condapi_response = api_condapi_instance.get_cond_alarm_list( filter="Severity eq Critical and Acknowledge eq None" , count = True)
            pprint("Critical:" + str(api_condapi_response["count"]))
            acc_result["critical"] = str(api_condapi_response["count"])
        # pprint(api_response + api_response["count"])
        except intersight.ApiException as e:
            print("Exception when calling CondApi->get_cond_alarm_list: %s\n" % e)
        data_list.append(acc_result)
    
    return data_list

if __name__ == "__main__":
    isightinfo()