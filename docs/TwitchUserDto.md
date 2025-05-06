# TwitchUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 

## Example

```python
from ttx.models.twitch_user_dto import TwitchUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of TwitchUserDto from a JSON string
twitch_user_dto_instance = TwitchUserDto.from_json(json)
# print the JSON string representation of the object
print(TwitchUserDto.to_json())

# convert the object into a dict
twitch_user_dto_dict = twitch_user_dto_instance.to_dict()
# create an instance of TwitchUserDto from a dict
twitch_user_dto_from_dict = TwitchUserDto.from_dict(twitch_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


