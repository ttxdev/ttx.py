# VoteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_id** | **int** |  | 
**value** | **int** |  | 
**time** | **datetime** |  | 

## Example

```python
from ttx_py.models.vote_dto import VoteDto

# TODO update the JSON string below
json = "{}"
# create an instance of VoteDto from a JSON string
vote_dto_instance = VoteDto.from_json(json)
# print the JSON string representation of the object
print(VoteDto.to_json())

# convert the object into a dict
vote_dto_dict = vote_dto_instance.to_dict()
# create an instance of VoteDto from a dict
vote_dto_from_dict = VoteDto.from_dict(vote_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


