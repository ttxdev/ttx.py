import ttx_py
from ttx_py.models.creator_dto import CreatorDto
from ttx_py.models.time_step import TimeStep
from ttx_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ttx_py.Configuration(host="http://api.ttx.gg")


# Enter a context with an instance of the API client
with ttx_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ttx_py.CreatorsApi(api_client)
    slug = "hasanabi"  # str |
    step = ttx_py.TimeStep("FiveMinute")  # TimeStep |  (optional)
    after = "2025-05-06T19:18:30+01:00"  # datetime |  (optional)

    try:
        api_response = api_instance.get_creator(slug, step=step, after=after)
        print("The response of CreatorsApi->get_creator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreatorsApi->get_creator: %s\n" % e)
