# PlayerShareDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | [**CreatorPartialDto**](CreatorPartialDto.md) |  | 
**quantity** | **int** |  | 

## Example

```python
from ttx.models.player_share_dto import PlayerShareDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerShareDto from a JSON string
player_share_dto_instance = PlayerShareDto.from_json(json)
# print the JSON string representation of the object
print(PlayerShareDto.to_json())

# convert the object into a dict
player_share_dto_dict = player_share_dto_instance.to_dict()
# create an instance of PlayerShareDto from a dict
player_share_dto_from_dict = PlayerShareDto.from_dict(player_share_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


