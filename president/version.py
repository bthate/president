# PRESIDENT (version.py)
#
# this file is in the Public Domain

""" version plugin. """

from president import __version__

txt = "using the law to administer poison the king commits genocide"

def ver(event):
    event.reply("PRESIDENT #%s - %s" % (__version__, txt))
