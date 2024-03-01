# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class AdAcoBodyLandingPageUrls(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'landing_page_url': 'str'
    }

    attribute_map = {
        'landing_page_url': 'landing_page_url'
    }

    def __init__(self, landing_page_url=None):  # noqa: E501
        """AdAcoBodyLandingPageUrls - a model defined in Swagger"""  # noqa: E501
        self._landing_page_url = None
        self.discriminator = None
        if landing_page_url is not None:
            self.landing_page_url = landing_page_url

    @property
    def landing_page_url(self):
        """Gets the landing_page_url of this AdAcoBodyLandingPageUrls.  # noqa: E501

        Landing page URL.  # noqa: E501

        :return: The landing_page_url of this AdAcoBodyLandingPageUrls.  # noqa: E501
        :rtype: str
        """
        return self._landing_page_url

    @landing_page_url.setter
    def landing_page_url(self, landing_page_url):
        """Sets the landing_page_url of this AdAcoBodyLandingPageUrls.

        Landing page URL.  # noqa: E501

        :param landing_page_url: The landing_page_url of this AdAcoBodyLandingPageUrls.  # noqa: E501
        :type: str
        """

        self._landing_page_url = landing_page_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdAcoBodyLandingPageUrls, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdAcoBodyLandingPageUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
