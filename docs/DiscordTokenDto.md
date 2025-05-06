# DiscordTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**link_token** | **str** |  | 
**twitch_users** | [**List[TwitchUserDto]**](TwitchUserDto.md) |  | [readonly] 

## Example

```python
from ttx_py.models.discord_token_dto import DiscordTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordTokenDto from a JSON string
discord_token_dto_instance = DiscordTokenDto.from_json(json)
# print the JSON string representation of the object
print(DiscordTokenDto.to_json())

# convert the object into a dict
discord_token_dto_dict = discord_token_dto_instance.to_dict()
# create an instance of DiscordTokenDto from a dict
discord_token_dto_from_dict = DiscordTokenDto.from_dict(discord_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


