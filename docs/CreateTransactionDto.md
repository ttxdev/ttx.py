# CreateTransactionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** |  | 
**action** | [**TransactionAction**](TransactionAction.md) |  | 
**amount** | **int** |  | 

## Example

```python
from ttx_py.models.create_transaction_dto import CreateTransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionDto from a JSON string
create_transaction_dto_instance = CreateTransactionDto.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionDto.to_json())

# convert the object into a dict
create_transaction_dto_dict = create_transaction_dto_instance.to_dict()
# create an instance of CreateTransactionDto from a dict
create_transaction_dto_from_dict = CreateTransactionDto.from_dict(create_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


