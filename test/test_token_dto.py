# coding: utf-8

"""
    TTX.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ttx.models.token_dto import TokenDto

class TestTokenDto(unittest.TestCase):
    """TokenDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenDto:
        """Test TokenDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenDto`
        """
        model = TokenDto()
        if include_optional:
            return TokenDto(
                access_token = ''
            )
        else:
            return TokenDto(
                access_token = '',
        )
        """

    def testTokenDto(self):
        """Test TokenDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
