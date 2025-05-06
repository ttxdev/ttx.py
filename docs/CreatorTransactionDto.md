# CreatorTransactionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**quantity** | **int** |  | 
**value** | **int** |  | 
**action** | [**TransactionAction**](TransactionAction.md) |  | 
**creator_id** | **int** |  | 
**player_id** | **int** |  | 
**player** | [**PlayerPartialDto**](PlayerPartialDto.md) |  | 

## Example

```python
from ttx_py.models.creator_transaction_dto import CreatorTransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorTransactionDto from a JSON string
creator_transaction_dto_instance = CreatorTransactionDto.from_json(json)
# print the JSON string representation of the object
print(CreatorTransactionDto.to_json())

# convert the object into a dict
creator_transaction_dto_dict = creator_transaction_dto_instance.to_dict()
# create an instance of CreatorTransactionDto from a dict
creator_transaction_dto_from_dict = CreatorTransactionDto.from_dict(creator_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


