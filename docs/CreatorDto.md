# CreatorDto


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
**transactions** | [**List[CreatorTransactionDto]**](CreatorTransactionDto.md) |  | 
**shares** | [**List[CreatorShareDto]**](CreatorShareDto.md) |  | 

## Example

```python
from ttx.models.creator_dto import CreatorDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorDto from a JSON string
creator_dto_instance = CreatorDto.from_json(json)
# print the JSON string representation of the object
print(CreatorDto.to_json())

# convert the object into a dict
creator_dto_dict = creator_dto_instance.to_dict()
# create an instance of CreatorDto from a dict
creator_dto_from_dict = CreatorDto.from_dict(creator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


