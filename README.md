MenubarNotifier
===

menubarnotifier.py

Alex Glasser
September 30, 2014

This is a simple script to display a message in the Mac OS X menubar using 
PyObjC. Make sure you have PyObjC installed - you can do this using MacPorts 
or Homebrew.

Call the script with the desired notification as the first and only argument:

``$ ./menubarnotifier.py "Notification Text"``

You may have to add executable permissions to the file first:

``$ chmod +x ./menubarnotifier.py``

~~This does use NSLog which writes to stderr by default. The way to bypass the 
logging is to redirect stderr to /dev/null with:~~

~~``$ ./menubarnotifier.py "Notification Text" 2>/dev/null``~~

_This script no longer logs using NSLog, so redirecting stderr to /dev/null is not required._

You will also want to run this in the background so it does not require 
Ctrl+C to allow you to continue using your shell:

``$ ./menubarnotifier.py "Notification Text" &``

Highly recommended:

Open your ~/.bash_profile and add/rename the following function:

```
mn () {
    /path/to/menubarnotifier.py "$*" &
}
```

Restart your Terminal. This will allow the script to be run like this:

``$ mn "Notification Text"``

...and will not require any redirection or the ampersand. 

===
_Feel free to use this code for whatever you want._
