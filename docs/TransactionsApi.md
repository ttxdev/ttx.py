# ttx_py.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_order**](TransactionsApi.md#place_order) | **POST** /transactions | 


# **place_order**
> CreatorTransactionDto place_order(create_transaction_dto=create_transaction_dto)

### Example


```python
import ttx_py
from ttx_py.models.create_transaction_dto import CreateTransactionDto
from ttx_py.models.creator_transaction_dto import CreatorTransactionDto
from ttx_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx_py.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx_py.TransactionsApi(api_client)
    create_transaction_dto = ttx_py.CreateTransactionDto() # CreateTransactionDto |  (optional)

    try:
        api_response = api_instance.place_order(create_transaction_dto=create_transaction_dto)
        print("The response of TransactionsApi->place_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->place_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transaction_dto** | [**CreateTransactionDto**](CreateTransactionDto.md)|  | [optional] 

### Return type

[**CreatorTransactionDto**](CreatorTransactionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

