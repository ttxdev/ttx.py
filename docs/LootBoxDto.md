# LootBoxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_open** | **bool** |  | 
**result** | [**CreatorPartialDto**](CreatorPartialDto.md) |  | 
**player** | [**PlayerPartialDto**](PlayerPartialDto.md) |  | 

## Example

```python
from ttx_py.models.loot_box_dto import LootBoxDto

# TODO update the JSON string below
json = "{}"
# create an instance of LootBoxDto from a JSON string
loot_box_dto_instance = LootBoxDto.from_json(json)
# print the JSON string representation of the object
print(LootBoxDto.to_json())

# convert the object into a dict
loot_box_dto_dict = loot_box_dto_instance.to_dict()
# create an instance of LootBoxDto from a dict
loot_box_dto_from_dict = LootBoxDto.from_dict(loot_box_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


