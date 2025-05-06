# PortfolioSnapshotDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **int** |  | 
**value** | **int** |  | 
**time** | **datetime** |  | 

## Example

```python
from ttx.models.portfolio_snapshot_dto import PortfolioSnapshotDto

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioSnapshotDto from a JSON string
portfolio_snapshot_dto_instance = PortfolioSnapshotDto.from_json(json)
# print the JSON string representation of the object
print(PortfolioSnapshotDto.to_json())

# convert the object into a dict
portfolio_snapshot_dto_dict = portfolio_snapshot_dto_instance.to_dict()
# create an instance of PortfolioSnapshotDto from a dict
portfolio_snapshot_dto_from_dict = PortfolioSnapshotDto.from_dict(portfolio_snapshot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


