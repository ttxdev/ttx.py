# CreatorPartialDtoPaginationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreatorPartialDto]**](CreatorPartialDto.md) |  | 
**total** | **int** |  | 

## Example

```python
from ttx.models.creator_partial_dto_pagination_dto import CreatorPartialDtoPaginationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorPartialDtoPaginationDto from a JSON string
creator_partial_dto_pagination_dto_instance = CreatorPartialDtoPaginationDto.from_json(json)
# print the JSON string representation of the object
print(CreatorPartialDtoPaginationDto.to_json())

# convert the object into a dict
creator_partial_dto_pagination_dto_dict = creator_partial_dto_pagination_dto_instance.to_dict()
# create an instance of CreatorPartialDtoPaginationDto from a dict
creator_partial_dto_pagination_dto_from_dict = CreatorPartialDtoPaginationDto.from_dict(creator_partial_dto_pagination_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


