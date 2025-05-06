# ttx.TTXApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_creator**](TTXApi.md#create_creator) | **POST** /creators | 
[**discord_callback**](TTXApi.md#discord_callback) | **GET** /sessions/discord/callback | 
[**gamba**](TTXApi.md#gamba) | **PUT** /players/me/lootboxes/{lootBoxId}/open | 
[**get_creator**](TTXApi.md#get_creator) | **GET** /creators/{slug} | 
[**get_creator_transactions**](TTXApi.md#get_creator_transactions) | **GET** /creators/{creatorSlug}/transactions | 
[**get_creators**](TTXApi.md#get_creators) | **GET** /creators | 
[**get_player**](TTXApi.md#get_player) | **GET** /players/{username} | 
[**get_players**](TTXApi.md#get_players) | **GET** /players | 
[**get_self**](TTXApi.md#get_self) | **GET** /players/me | 
[**link_discord_twitch**](TTXApi.md#link_discord_twitch) | **POST** /sessions/discord/link | 
[**place_order**](TTXApi.md#place_order) | **POST** /transactions | 
[**twitch_callback**](TTXApi.md#twitch_callback) | **GET** /sessions/twitch/callback | 


# **create_creator**
> CreatorDto create_creator(username=username, ticker=ticker)

### Example


```python
import ttx
from ttx.models.creator_dto import CreatorDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    username = 'username_example' # str |  (optional)
    ticker = 'ticker_example' # str |  (optional)

    try:
        api_response = api_instance.create_creator(username=username, ticker=ticker)
        print("The response of TTXApi->create_creator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->create_creator: %s\n" % e)
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

# **discord_callback**
> DiscordTokenDto discord_callback(code=code)

### Example


```python
import ttx
from ttx.models.discord_token_dto import DiscordTokenDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        api_response = api_instance.discord_callback(code=code)
        print("The response of TTXApi->discord_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->discord_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 

### Return type

[**DiscordTokenDto**](DiscordTokenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gamba**
> LootBoxResultDto gamba(loot_box_id)

### Example


```python
import ttx
from ttx.models.loot_box_result_dto import LootBoxResultDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    loot_box_id = 56 # int | 

    try:
        api_response = api_instance.gamba(loot_box_id)
        print("The response of TTXApi->gamba:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->gamba: %s\n" % e)
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

# **get_creator**
> CreatorDto get_creator(slug, step=step, after=after)

### Example


```python
import ttx
from ttx.models.creator_dto import CreatorDto
from ttx.models.time_step import TimeStep
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    slug = 'slug_example' # str | 
    step = ttx.TimeStep() # TimeStep |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_creator(slug, step=step, after=after)
        print("The response of TTXApi->get_creator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_creator: %s\n" % e)
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
import ttx
from ttx.models.player_transaction_dto import PlayerTransactionDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    creator_slug = 'creator_slug_example' # str | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.get_creator_transactions(creator_slug, slug=slug)
        print("The response of TTXApi->get_creator_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_creator_transactions: %s\n" % e)
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
import ttx
from ttx.models.creator_order_by import CreatorOrderBy
from ttx.models.creator_partial_dto_pagination_dto import CreatorPartialDtoPaginationDto
from ttx.models.order_direction import OrderDirection
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    order_by = ttx.CreatorOrderBy() # CreatorOrderBy |  (optional)
    order_dir = ttx.OrderDirection() # OrderDirection |  (optional)

    try:
        api_response = api_instance.get_creators(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)
        print("The response of TTXApi->get_creators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_creators: %s\n" % e)
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

# **get_player**
> PlayerDto get_player(username, step=step, after=after)

### Example


```python
import ttx
from ttx.models.player_dto import PlayerDto
from ttx.models.time_step import TimeStep
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    username = 'username_example' # str | 
    step = ttx.TimeStep() # TimeStep |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_player(username, step=step, after=after)
        print("The response of TTXApi->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_player: %s\n" % e)
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
import ttx
from ttx.models.order_direction import OrderDirection
from ttx.models.player_dto_pagination_dto import PlayerDtoPaginationDto
from ttx.models.player_order_by import PlayerOrderBy
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    order_by = ttx.PlayerOrderBy() # PlayerOrderBy |  (optional)
    order_dir = ttx.OrderDirection() # OrderDirection |  (optional)

    try:
        api_response = api_instance.get_players(page=page, limit=limit, search=search, order_by=order_by, order_dir=order_dir)
        print("The response of TTXApi->get_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_players: %s\n" % e)
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
import ttx
from ttx.models.player_dto import PlayerDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)

    try:
        api_response = api_instance.get_self()
        print("The response of TTXApi->get_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->get_self: %s\n" % e)
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

# **link_discord_twitch**
> TokenDto link_discord_twitch(link_discord_twitch_dto=link_discord_twitch_dto)

### Example


```python
import ttx
from ttx.models.link_discord_twitch_dto import LinkDiscordTwitchDto
from ttx.models.token_dto import TokenDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    link_discord_twitch_dto = ttx.LinkDiscordTwitchDto() # LinkDiscordTwitchDto |  (optional)

    try:
        api_response = api_instance.link_discord_twitch(link_discord_twitch_dto=link_discord_twitch_dto)
        print("The response of TTXApi->link_discord_twitch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->link_discord_twitch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_discord_twitch_dto** | [**LinkDiscordTwitchDto**](LinkDiscordTwitchDto.md)|  | [optional] 

### Return type

[**TokenDto**](TokenDto.md)

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

# **place_order**
> CreatorTransactionDto place_order(create_transaction_dto=create_transaction_dto)

### Example


```python
import ttx
from ttx.models.create_transaction_dto import CreateTransactionDto
from ttx.models.creator_transaction_dto import CreatorTransactionDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    create_transaction_dto = ttx.CreateTransactionDto() # CreateTransactionDto |  (optional)

    try:
        api_response = api_instance.place_order(create_transaction_dto=create_transaction_dto)
        print("The response of TTXApi->place_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->place_order: %s\n" % e)
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

# **twitch_callback**
> TokenDto twitch_callback(code=code)

### Example


```python
import ttx
from ttx.models.token_dto import TokenDto
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        api_response = api_instance.twitch_callback(code=code)
        print("The response of TTXApi->twitch_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TTXApi->twitch_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 

### Return type

[**TokenDto**](TokenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

