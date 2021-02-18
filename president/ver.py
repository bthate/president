# OTP-CR-117/19 otp.informationdesk@icc-cpi.int http://pypi.org/project/genocide
#
# This file is placed in the Public Domain.

""" version plugin. """

from president import __version__

txt = "OTP-CR-117/19 otp.informationdesk@icc-cpi.int http://pypi.org/project/genocide !"

def ver(event):
    event.reply(txt)
