# CreatorPartialDto


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
**ticker** | **str** |  | 
**value** | **int** |  | 
**stream_status** | [**StreamStatusDto**](StreamStatusDto.md) |  | 
**history** | [**List[VoteDto]**](VoteDto.md) |  | 

## Example

```python
from ttx_py.models.creator_partial_dto import CreatorPartialDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorPartialDto from a JSON string
creator_partial_dto_instance = CreatorPartialDto.from_json(json)
# print the JSON string representation of the object
print(CreatorPartialDto.to_json())

# convert the object into a dict
creator_partial_dto_dict = creator_partial_dto_instance.to_dict()
# create an instance of CreatorPartialDto from a dict
creator_partial_dto_from_dict = CreatorPartialDto.from_dict(creator_partial_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


