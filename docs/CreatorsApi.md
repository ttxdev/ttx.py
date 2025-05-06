# ttx_py.CreatorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_creator**](CreatorsApi.md#create_creator) | **POST** /creators | 
[**get_creator**](CreatorsApi.md#get_creator) | **GET** /creators/{slug} | 
[**get_creator_transactions**](CreatorsApi.md#get_creator_transactions) | **GET** /creators/{creatorSlug}/transactions | 
[**get_creators**](CreatorsApi.md#get_creators) | **GET** /creators | 


# **create_creator**
> CreatorDto create_creator(username=username, ticker=ticker)

### Example


```python
import ttx_py
from ttx_py.models.creator_dto import CreatorDto
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
    api_instance = ttx_py.CreatorsApi(api_client)
    username = 'username_example' # str |  (optional)
    ticker = 'ticker_example' # str |  (optional)

    try:
        api_response = api_instance.create_creator(username=username, ticker=ticker)
        print("The response of CreatorsApi->create_creator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreatorsApi->create_creator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **ticker** | **str**|  | [optional] 

### Return type

[**CreatorDto**](CreatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creator**
> CreatorDto get_creator(slug, step=step, after=after)

### Example


```python
import ttx_py
from ttx_py.models.creator_dto import CreatorDto
from ttx_py.models.time_step import TimeStep
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
    api_instance = ttx_py.CreatorsApi(api_client)
    slug = 'slug_example' # str | 
    step = ttx_py.TimeStep() # TimeStep |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_creator(slug, step=step, after=after)
        print("The response of CreatorsApi->get_creator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreatorsApi->get_creator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **step** | [**TimeStep**](.md)|  | [optional] 
 **after** | **datetime**|  | [optional] 

### Return type

[**CreatorDto**](CreatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creator_transactions**
> List[PlayerTransactionDto] get_creator_transactions(creator_slug, slug=slug)

### Example


```python
import ttx_py
from ttx_py.models.player_transaction_dto import PlayerTransactionDto
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
    api_instance = ttx_py.CreatorsApi(api_client)
    creator_slug = 'creator_slug_example' # str | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.get_creator_transactions(creator_slug, slug=slug)
        print("The response of CreatorsApi->get_creator_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreatorsApi->get_creator_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creator_slug** | **str**|  | 
 **slug** | **str**|  | [optional] 

### Return type

[**List[PlayerTransactionDto]**](PlayerTransactionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_creators**
> CreatorPartialDtoPaginationDto get_creators(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)

### Example


```python
import ttx_py
from ttx_py.models.creator_order_by import CreatorOrderBy
from ttx_py.models.creator_partial_dto_pagination_dto import CreatorPartialDtoPaginationDto
from ttx_py.models.order_direction import OrderDirection
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
    api_instance = ttx_py.CreatorsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    order_by = ttx_py.CreatorOrderBy() # CreatorOrderBy |  (optional)
    order_dir = ttx_py.OrderDirection() # OrderDirection |  (optional)

    try:
        api_response = api_instance.get_creators(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)
        print("The response of CreatorsApi->get_creators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreatorsApi->get_creators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **order_by** | [**CreatorOrderBy**](.md)|  | [optional] 
 **order_dir** | [**OrderDirection**](.md)|  | [optional] 

### Return type

[**CreatorPartialDtoPaginationDto**](CreatorPartialDtoPaginationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

