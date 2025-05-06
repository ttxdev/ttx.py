# PlayerTransactionDto


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
**creator** | [**CreatorPartialDto**](CreatorPartialDto.md) |  | 

## Example

```python
from ttx_py.models.player_transaction_dto import PlayerTransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTransactionDto from a JSON string
player_transaction_dto_instance = PlayerTransactionDto.from_json(json)
# print the JSON string representation of the object
print(PlayerTransactionDto.to_json())

# convert the object into a dict
player_transaction_dto_dict = player_transaction_dto_instance.to_dict()
# create an instance of PlayerTransactionDto from a dict
player_transaction_dto_from_dict = PlayerTransactionDto.from_dict(player_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


