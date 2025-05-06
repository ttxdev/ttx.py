# PlayerDto


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
**transactions** | [**List[PlayerTransactionDto]**](PlayerTransactionDto.md) |  | 
**loot_boxes** | [**List[LootBoxDto]**](LootBoxDto.md) |  | 
**shares** | [**List[PlayerShareDto]**](PlayerShareDto.md) |  | 
**history** | [**List[PortfolioSnapshotDto]**](PortfolioSnapshotDto.md) |  | 

## Example

```python
from ttx_py.models.player_dto import PlayerDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerDto from a JSON string
player_dto_instance = PlayerDto.from_json(json)
# print the JSON string representation of the object
print(PlayerDto.to_json())

# convert the object into a dict
player_dto_dict = player_dto_instance.to_dict()
# create an instance of PlayerDto from a dict
player_dto_from_dict = PlayerDto.from_dict(player_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


