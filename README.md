# ttx

TTX API Wrapper

## Requirements

Python 3.9+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ttxdev/ttx.py.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ttxdev/ttx.py.git`)

Then import the package:

```python
import ttx
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import ttx
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import ttx
from ttx.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with ttx.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx.TTXClientApi(api_client)
    username = 'username_example' # str |  (optional)
    ticker = 'ticker_example' # str |  (optional)

    try:
        api_response = api_instance.create_creator(username=username, ticker=ticker)
        print("The response of TTXClientApi->create_creator:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TTXClientApi->create_creator: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TTXClientApi* | [**create_creator**](docs/TTXClientApi.md#create_creator) | **POST** /creators | 
*TTXClientApi* | [**discord_callback**](docs/TTXClientApi.md#discord_callback) | **GET** /sessions/discord/callback | 
*TTXClientApi* | [**gamba**](docs/TTXClientApi.md#gamba) | **PUT** /players/me/lootboxes/{lootBoxId}/open | 
*TTXClientApi* | [**get_creator**](docs/TTXClientApi.md#get_creator) | **GET** /creators/{slug} | 
*TTXClientApi* | [**get_creator_transactions**](docs/TTXClientApi.md#get_creator_transactions) | **GET** /creators/{creatorSlug}/transactions | 
*TTXClientApi* | [**get_creators**](docs/TTXClientApi.md#get_creators) | **GET** /creators | 
*TTXClientApi* | [**get_player**](docs/TTXClientApi.md#get_player) | **GET** /players/{username} | 
*TTXClientApi* | [**get_players**](docs/TTXClientApi.md#get_players) | **GET** /players | 
*TTXClientApi* | [**get_self**](docs/TTXClientApi.md#get_self) | **GET** /players/me | 
*TTXClientApi* | [**link_discord_twitch**](docs/TTXClientApi.md#link_discord_twitch) | **POST** /sessions/discord/link | 
*TTXClientApi* | [**place_order**](docs/TTXClientApi.md#place_order) | **POST** /transactions | 
*TTXClientApi* | [**twitch_callback**](docs/TTXClientApi.md#twitch_callback) | **GET** /sessions/twitch/callback | 

## Documentation For Models

- [CreateTransactionDto](docs/CreateTransactionDto.md)
- [CreatorDto](docs/CreatorDto.md)
- [CreatorOrderBy](docs/CreatorOrderBy.md)
- [CreatorPartialDto](docs/CreatorPartialDto.md)
- [CreatorPartialDtoPaginationDto](docs/CreatorPartialDtoPaginationDto.md)
- [CreatorRarityDto](docs/CreatorRarityDto.md)
- [CreatorShareDto](docs/CreatorShareDto.md)
- [CreatorTransactionDto](docs/CreatorTransactionDto.md)
- [DiscordTokenDto](docs/DiscordTokenDto.md)
- [LinkDiscordTwitchDto](docs/LinkDiscordTwitchDto.md)
- [LootBoxDto](docs/LootBoxDto.md)
- [LootBoxResultDto](docs/LootBoxResultDto.md)
- [ModelId](docs/ModelId.md)
- [OrderDirection](docs/OrderDirection.md)
- [PlayerDto](docs/PlayerDto.md)
- [PlayerDtoPaginationDto](docs/PlayerDtoPaginationDto.md)
- [PlayerOrderBy](docs/PlayerOrderBy.md)
- [PlayerPartialDto](docs/PlayerPartialDto.md)
- [PlayerShareDto](docs/PlayerShareDto.md)
- [PlayerTransactionDto](docs/PlayerTransactionDto.md)
- [PlayerType](docs/PlayerType.md)
- [PortfolioSnapshotDto](docs/PortfolioSnapshotDto.md)
- [Rarity](docs/Rarity.md)
- [StreamStatusDto](docs/StreamStatusDto.md)
- [TimeStep](docs/TimeStep.md)
- [TokenDto](docs/TokenDto.md)
- [TransactionAction](docs/TransactionAction.md)
- [TwitchUserDto](docs/TwitchUserDto.md)
- [VoteDto](docs/VoteDto.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Endpoints do not require authorization.

## Author

[NathanRoberts55](https://github.com/nathanroberts55)