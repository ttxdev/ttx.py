# CreatorRarityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | [**CreatorPartialDto**](CreatorPartialDto.md) |  | 
**rarity** | [**Rarity**](Rarity.md) |  | 

## Example

```python
from ttx_py.models.creator_rarity_dto import CreatorRarityDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorRarityDto from a JSON string
creator_rarity_dto_instance = CreatorRarityDto.from_json(json)
# print the JSON string representation of the object
print(CreatorRarityDto.to_json())

# convert the object into a dict
creator_rarity_dto_dict = creator_rarity_dto_instance.to_dict()
# create an instance of CreatorRarityDto from a dict
creator_rarity_dto_from_dict = CreatorRarityDto.from_dict(creator_rarity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


