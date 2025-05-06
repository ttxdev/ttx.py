# ttx_py.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discord_callback**](SessionsApi.md#discord_callback) | **GET** /sessions/discord/callback | 
[**link_discord_twitch**](SessionsApi.md#link_discord_twitch) | **POST** /sessions/discord/link | 
[**twitch_callback**](SessionsApi.md#twitch_callback) | **GET** /sessions/twitch/callback | 


# **discord_callback**
> DiscordTokenDto discord_callback(code=code)

### Example


```python
import ttx_py
from ttx_py.models.discord_token_dto import DiscordTokenDto
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
    api_instance = ttx_py.SessionsApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        api_response = api_instance.discord_callback(code=code)
        print("The response of SessionsApi->discord_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->discord_callback: %s\n" % e)
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

# **link_discord_twitch**
> TokenDto link_discord_twitch(link_discord_twitch_dto=link_discord_twitch_dto)

### Example


```python
import ttx_py
from ttx_py.models.link_discord_twitch_dto import LinkDiscordTwitchDto
from ttx_py.models.token_dto import TokenDto
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
    api_instance = ttx_py.SessionsApi(api_client)
    link_discord_twitch_dto = ttx_py.LinkDiscordTwitchDto() # LinkDiscordTwitchDto |  (optional)

    try:
        api_response = api_instance.link_discord_twitch(link_discord_twitch_dto=link_discord_twitch_dto)
        print("The response of SessionsApi->link_discord_twitch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->link_discord_twitch: %s\n" % e)
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

# **twitch_callback**
> TokenDto twitch_callback(code=code)

### Example


```python
import ttx_py
from ttx_py.models.token_dto import TokenDto
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
    api_instance = ttx_py.SessionsApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        api_response = api_instance.twitch_callback(code=code)
        print("The response of SessionsApi->twitch_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->twitch_callback: %s\n" % e)
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

