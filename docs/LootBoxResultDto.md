# LootBoxResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lootbox_id** | [**ModelId**](ModelId.md) |  | 
**player** | [**PlayerPartialDto**](PlayerPartialDto.md) |  | 
**result** | [**CreatorRarityDto**](CreatorRarityDto.md) |  | 
**rarities** | [**List[CreatorRarityDto]**](CreatorRarityDto.md) |  | 

## Example

```python
from ttx.models.loot_box_result_dto import LootBoxResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of LootBoxResultDto from a JSON string
loot_box_result_dto_instance = LootBoxResultDto.from_json(json)
# print the JSON string representation of the object
print(LootBoxResultDto.to_json())

# convert the object into a dict
loot_box_result_dto_dict = loot_box_result_dto_instance.to_dict()
# create an instance of LootBoxResultDto from a dict
loot_box_result_dto_from_dict = LootBoxResultDto.from_dict(loot_box_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


