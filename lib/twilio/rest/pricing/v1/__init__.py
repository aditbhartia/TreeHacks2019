# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.pricing.v1.messaging import MessagingList
from twilio.rest.pricing.v1.phone_number import PhoneNumberList
from twilio.rest.pricing.v1.voice import VoiceList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Pricing

        :returns: V1 version of Pricing
        :rtype: twilio.rest.pricing.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._messaging = None
        self._phone_numbers = None
        self._voice = None

    @property
    def messaging(self):
        """
        :rtype: twilio.rest.pricing.v1.messaging.MessagingList
        """
        if self._messaging is None:
            self._messaging = MessagingList(self)
        return self._messaging

    @property
    def phone_numbers(self):
        """
        :rtype: twilio.rest.pricing.v1.phone_number.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self)
        return self._phone_numbers

    @property
    def voice(self):
        """
        :rtype: twilio.rest.pricing.v1.voice.VoiceList
        """
        if self._voice is None:
            self._voice = VoiceList(self)
        return self._voice

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1>'
