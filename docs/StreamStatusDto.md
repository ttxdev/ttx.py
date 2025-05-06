# StreamStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_live** | **bool** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from ttx_py.models.stream_status_dto import StreamStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of StreamStatusDto from a JSON string
stream_status_dto_instance = StreamStatusDto.from_json(json)
# print the JSON string representation of the object
print(StreamStatusDto.to_json())

# convert the object into a dict
stream_status_dto_dict = stream_status_dto_instance.to_dict()
# create an instance of StreamStatusDto from a dict
stream_status_dto_from_dict = StreamStatusDto.from_dict(stream_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


