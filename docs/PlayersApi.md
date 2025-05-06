# ttx_py.PlayersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gamba**](PlayersApi.md#gamba) | **PUT** /players/me/lootboxes/{lootBoxId}/open | 
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{username} | 
[**get_players**](PlayersApi.md#get_players) | **GET** /players | 
[**get_self**](PlayersApi.md#get_self) | **GET** /players/me | 


# **gamba**
> LootBoxResultDto gamba(loot_box_id)

### Example


```python
import ttx_py
from ttx_py.models.loot_box_result_dto import LootBoxResultDto
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
    api_instance = ttx_py.PlayersApi(api_client)
    loot_box_id = 56 # int | 

    try:
        api_response = api_instance.gamba(loot_box_id)
        print("The response of PlayersApi->gamba:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->gamba: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loot_box_id** | **int**|  | 

### Return type

[**LootBoxResultDto**](LootBoxResultDto.md)

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

# **get_player**
> PlayerDto get_player(username, step=step, after=after)

### Example


```python
import ttx_py
from ttx_py.models.player_dto import PlayerDto
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
    api_instance = ttx_py.PlayersApi(api_client)
    username = 'username_example' # str | 
    step = ttx_py.TimeStep() # TimeStep |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_player(username, step=step, after=after)
        print("The response of PlayersApi->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **step** | [**TimeStep**](.md)|  | [optional] 
 **after** | **datetime**|  | [optional] 

### Return type

[**PlayerDto**](PlayerDto.md)

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

# **get_players**
> PlayerDtoPaginationDto get_players(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)

### Example


```python
import ttx_py
from ttx_py.models.order_direction import OrderDirection
from ttx_py.models.player_dto_pagination_dto import PlayerDtoPaginationDto
from ttx_py.models.player_order_by import PlayerOrderBy
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
    api_instance = ttx_py.PlayersApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    order_by = ttx_py.PlayerOrderBy() # PlayerOrderBy |  (optional)
    order_dir = ttx_py.OrderDirection() # OrderDirection |  (optional)

    try:
        api_response = api_instance.get_players(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)
        print("The response of PlayersApi->get_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **order_by** | [**PlayerOrderBy**](.md)|  | [optional] 
 **order_dir** | [**OrderDirection**](.md)|  | [optional] 

### Return type

[**PlayerDtoPaginationDto**](PlayerDtoPaginationDto.md)

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

# **get_self**
> PlayerDto get_self()

### Example


```python
import ttx_py
from ttx_py.models.player_dto import PlayerDto
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
    api_instance = ttx_py.PlayersApi(api_client)

    try:
        api_response = api_instance.get_self()
        print("The response of PlayersApi->get_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PlayerDto**](PlayerDto.md)

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

