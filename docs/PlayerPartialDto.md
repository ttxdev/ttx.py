# PlayerPartialDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**twitch_id** | **str** |  | 
**url** | **str** |  | [readonly] 
**avatar_url** | **str** |  | 
**credits** | **int** |  | 
**portfolio** | **int** |  | 
**value** | **int** |  | 
**type** | [**PlayerType**](PlayerType.md) |  | 

## Example

```python
from ttx.models.player_partial_dto import PlayerPartialDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPartialDto from a JSON string
player_partial_dto_instance = PlayerPartialDto.from_json(json)
# print the JSON string representation of the object
print(PlayerPartialDto.to_json())

# convert the object into a dict
player_partial_dto_dict = player_partial_dto_instance.to_dict()
# create an instance of PlayerPartialDto from a dict
player_partial_dto_from_dict = PlayerPartialDto.from_dict(player_partial_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


