# president/version.py
#
#

from president import __version__, __txt__

def version(event):
    event.reply("PRESIDENT #%s - %s" % (__version__, __txt__))
