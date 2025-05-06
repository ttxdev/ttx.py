# CreatorShareDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**PlayerPartialDto**](PlayerPartialDto.md) |  | 
**quantity** | **int** |  | 

## Example

```python
from ttx_py.models.creator_share_dto import CreatorShareDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorShareDto from a JSON string
creator_share_dto_instance = CreatorShareDto.from_json(json)
# print the JSON string representation of the object
print(CreatorShareDto.to_json())

# convert the object into a dict
creator_share_dto_dict = creator_share_dto_instance.to_dict()
# create an instance of CreatorShareDto from a dict
creator_share_dto_from_dict = CreatorShareDto.from_dict(creator_share_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


