# LinkDiscordTwitchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**twitch_id** | **str** |  | 

## Example

```python
from ttx.models.link_discord_twitch_dto import LinkDiscordTwitchDto

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDiscordTwitchDto from a JSON string
link_discord_twitch_dto_instance = LinkDiscordTwitchDto.from_json(json)
# print the JSON string representation of the object
print(LinkDiscordTwitchDto.to_json())

# convert the object into a dict
link_discord_twitch_dto_dict = link_discord_twitch_dto_instance.to_dict()
# create an instance of LinkDiscordTwitchDto from a dict
link_discord_twitch_dto_from_dict = LinkDiscordTwitchDto.from_dict(link_discord_twitch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


