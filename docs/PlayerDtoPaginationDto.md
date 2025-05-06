# PlayerDtoPaginationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayerDto]**](PlayerDto.md) |  | 
**total** | **int** |  | 

## Example

```python
from ttx.models.player_dto_pagination_dto import PlayerDtoPaginationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerDtoPaginationDto from a JSON string
player_dto_pagination_dto_instance = PlayerDtoPaginationDto.from_json(json)
# print the JSON string representation of the object
print(PlayerDtoPaginationDto.to_json())

# convert the object into a dict
player_dto_pagination_dto_dict = player_dto_pagination_dto_instance.to_dict()
# create an instance of PlayerDtoPaginationDto from a dict
player_dto_pagination_dto_from_dict = PlayerDtoPaginationDto.from_dict(player_dto_pagination_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


