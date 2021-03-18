# LibreRocket
## Installation
### Prerequisites 
 - Python 3.9
 - Python default modules
 - [Tkinter](#Tkinter)
### Tkinter
Tkinter is a common GUI module for python projects, and is usually included with the packages that are installed when python is. Many OS's and Linux distrobutions have the binaries for the library preinstalled, but if
~~~python
Traceback (most recent call last):
  File "/home/<USER>/librerocket/src/main.py", line 2, in <module>
    from tkinter import *
  File "/usr/lib/python3.9/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ImportError: libtk8.6.so: cannot open shared object file: No such file or directory
~~~
or a similar error occurs when running the main file, it usually means that the tkinter binaries are missing. This often happens on "minimal" versons of Linux distros. To fix this run:
With apt:
~~~sh
sudo apt-get install python3-tk
~~~
With pacman:
~~~sh
sudo pacman -S tk
~~~
With rpm:
~~~sh
rpm -ivh tkinter-2.7-90el7.x86_64.rpm
~~~
<sup>Note: I am not framiliar with RPM so this could be out of date/incorrect</sup>

