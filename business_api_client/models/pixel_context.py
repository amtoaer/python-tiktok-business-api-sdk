# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class PixelContext(object):
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
        'ad': 'PixelContextAd',
        'ip': 'str',
        'page': 'PixelContextPage',
        'user': 'PixelContextUser',
        'user_agent': 'str'
    }

    attribute_map = {
        'ad': 'ad',
        'ip': 'ip',
        'page': 'page',
        'user': 'user',
        'user_agent': 'user_agent'
    }

    def __init__(self, ad=None, ip=None, page=None, user=None, user_agent=None):  # noqa: E501
        """PixelContext - a model defined in Swagger"""  # noqa: E501
        self._ad = None
        self._ip = None
        self._page = None
        self._user = None
        self._user_agent = None
        self.discriminator = None
        if ad is not None:
            self.ad = ad
        if ip is not None:
            self.ip = ip
        if page is not None:
            self.page = page
        if user is not None:
            self.user = user
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def ad(self):
        """Gets the ad of this PixelContext.  # noqa: E501


        :return: The ad of this PixelContext.  # noqa: E501
        :rtype: PixelContextAd
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this PixelContext.


        :param ad: The ad of this PixelContext.  # noqa: E501
        :type: PixelContextAd
        """

        self._ad = ad

    @property
    def ip(self):
        """Gets the ip of this PixelContext.  # noqa: E501

        Non-hashed public IP address of the browser. To increase the probability of matching website visitor events with TikTok ads, we recommend sending both ip and user_agent.  # noqa: E501

        :return: The ip of this PixelContext.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PixelContext.

        Non-hashed public IP address of the browser. To increase the probability of matching website visitor events with TikTok ads, we recommend sending both ip and user_agent.  # noqa: E501

        :param ip: The ip of this PixelContext.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def page(self):
        """Gets the page of this PixelContext.  # noqa: E501


        :return: The page of this PixelContext.  # noqa: E501
        :rtype: PixelContextPage
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PixelContext.


        :param page: The page of this PixelContext.  # noqa: E501
        :type: PixelContextPage
        """

        self._page = page

    @property
    def user(self):
        """Gets the user of this PixelContext.  # noqa: E501


        :return: The user of this PixelContext.  # noqa: E501
        :rtype: PixelContextUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PixelContext.


        :param user: The user of this PixelContext.  # noqa: E501
        :type: PixelContextUser
        """

        self._user = user

    @property
    def user_agent(self):
        """Gets the user_agent of this PixelContext.  # noqa: E501

        Non-hashed user agent from the user’s device. To increase the probability of matching website visitor events with TikTok ads, we recommend sending both ip and user_agent.  # noqa: E501

        :return: The user_agent of this PixelContext.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this PixelContext.

        Non-hashed user agent from the user’s device. To increase the probability of matching website visitor events with TikTok ads, we recommend sending both ip and user_agent.  # noqa: E501

        :param user_agent: The user_agent of this PixelContext.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if issubclass(PixelContext, dict):
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
        if not isinstance(other, PixelContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other