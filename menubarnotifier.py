#!/usr/bin/python

'''
menubarnotifier.py

Alex Glasser
September 23, 2014

Simple script to display a message in the Mac OS X menubar using PyObjC.
Make sure you have PyObjC installed - you can do this using MacPorts or Homebrew.

Call the script with the desired notification as argv[1]:
  ./menubarnotifier.py "Notification Text"
Suggested: Redirect stderr to /dev/null and run the script in the background:
  ./menubarnotifier.py "Notification Text" 2>/dev/null &
'''

from sys import argv
try:
    from PyObjCTools import AppHelper
    from Foundation import *
    from AppKit import *
except ImportError:
    print "Failed to import from PyObjC."
    exit(-1)    

start_time = NSDate.date()

class MenubarNotifier(NSObject):
    state = 'ok'

    def applicationDidFinishLaunching_(self, sender):
        NSLog("Loaded successfully.")
        # Get notification text from argv[1], if possible.
        try:
            display_text = " ".join(argv[1:])
        except IndexError:
            display_text = "Default Text"
        NSLog("Notification is '{}'".format(display_text))

        self.statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        self.statusItem.setTitle_(display_text)          # argv[1] or "Default Text"
        self.statusItem.setEnabled_(TRUE)                # item is enabled for clicking
        self.statusItem.setAction_('statusItemClicked:') # method called when statusItem is clicked
        self.statusItem.setHighlightMode_(TRUE)          # highlight the item when clicked

        # Get the timer going
        self.timer = NSTimer.alloc().initWithFireDate_interval_target_selector_userInfo_repeats_(start_time, 5.0, self, 'tick:', None, True)
        NSRunLoop.currentRunLoop().addTimer_forMode_(self.timer, NSDefaultRunLoopMode)
        self.timer.fire()

    def tick_(self, notification):
        NSLog("state is {}".format(self.state))

    def statusItemClicked_(self, notification):
        ''' Closes the application when clicked '''
        NSLog("Notification was clicked. Goodbye.")
        AppHelper.stopEventLoop()


def main():
    # Hide the dock icon
    info = NSBundle.mainBundle().infoDictionary()
    info["LSBackgroundOnly"] = "1"

    app = NSApplication.sharedApplication()
    delegate = MenubarNotifier.alloc().init()
    app.setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print e
        exit(-1)
