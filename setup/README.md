##Setup

Please read carefully the instructions below which will tell you what you need to prepare prior the bootcamp.

###Required Software

To complete the entire workshop you need several things:   
* a Bash shell,   
* [Git](http://git-scm.com/),   
* a code editor (though any plain text editor will work in a pinch),   
* Python 2.7 or higher and [IPython](http://ipython.org/install.html) 0.13 or higher,   
* a scientific Python installation that includes the IPython Notebook, [NumPy](http://numpy.scipy.org/), [SciPy](http://scipy.org) and [matplotlib](ttp://matplotlib.org/); we recommend that you use [Anaconda]((http://continuum.io/downloads.html)) - as explained below,      
* Python [nose](https://nose.readthedocs.org/en/latest/)  framework for Testing.  

With these tools, your computer will be ready for a wide variety of scientific computing tasks. One of our goals in this workshop is to help you get these cutting-edge programs installed so you can focus on science in the future, not installation.

Please do your best to install all the required software and potentially the virtual machine (explained below) prior to the start of the boot camp. If you have any issues, please email Aleksandra (aleksandra.n.pawlik {at remove-this} gmail {dot remove-this} com) for help.


###Installation instructions

__Even if you plan to install things yourself please download VirtualBox and the virtual machine as a backup. It can be extremely difficult to get everything set up correctly.
Virtual Machine.__

The simplest way to install all the requirements is to use a virtual machine. To get that, please install [VirtualBox](https://www.virtualbox.org/) and download [this virtual machine image](http://files.software-carpentry.org/swc_lubuntu.ova). Load the VM into VirtualBox by doing Import Appliance and loading the .ova file.

####Bash
Bash is a commonly-used shell. Using a shell gives you more power to do more tasks more quickly with your computer.   

___Mac___   

The default shell in all versions of Mac OS X is bash, so no need to install anything. You access bash from the Terminal (found in `/Applications/Utilities`). You may want to keep Terminal in your dock for this workshop.    

___Windows___

Install [Git Bash](http://msysgit.github.com/) following the instructions [here](https://openhatch.org/missions/windows-setup/install-git-bash). Git bash gives you the bash shell plus git. Two birds with one stone!

___Linux___

The default shell is usually bash but if not you can get to bash by opening a terminal and typing bash. No need to install anything.

####Git
Git is a state-of-the-art version control system. It lets you track who made changes to what when and has options for easily updating a shared or public version of your code on [github.com](https://github.com/).

___Mac___

For git, for the Anacoda version of Python (see below), and for a lot of other scientific computing software, Mac users need a C compiler on their computer. The way to get that is to install [Xcode](https://developer.apple.com/xcode/).

___For Mac OS X 10.7 and 10.8:___

Go to the [Xcode website](https://developer.apple.com/xcode/). Get XCode from the App Store making certain to install the command line tools (from the Download preferences pane). Git is included in the command line tools.

___For Mac OS X 10.6___

If you have Mac OS X 10.6, first get XCode by going to [the Apple developer site](https://developer.apple.com/downloads/). You have to sign in with an Apple ID linked to a Developer account. If you don't have one, you can register and create one. (It's lame, I know, that's why it's done through the App Store now.) Then, once you log in, go to page 8 and find "XCode 3.2.6 and iOS SDK 4.3 for Snow Leopard" near the top. Click to open that section, and then download the .dmg file. It's 4.14 Gb, so leave some time to download this one. But it's worth it! Then, [install just git](http://code.google.com/p/git-osx-installer/downloads/list?can=3).

___Windows___

Install [Git Bash](http://msysgit.github.com/) following the instructions [here](https://openhatch.org/missions/windows-setup/install-git-bash) if you haven't already.

___Linux___

If git is not already available on your machine you can try to install it via your distro's package manager (e.g. `apt-get`).

####Python

Python is becoming more and more popular in scientific computing, and it's a great language for teaching general programming concepts due to its easy-to-read syntax. Installing all the scientific packages for Python individually can be a bit difficult, so we recommend using an all-in-one installer.

___Mac & Linux___

We recommend the all-in-one scientific Python installer [Anaconda](http://continuum.io/downloads.html). Installation requires using the shell and if you aren't comfortable doing the installation yourself just download the installer and we'll help you at the boot camp. If you want to give it a try, do the following:

1.Download the installer that matches your operating system and save it in your home folder.
    Open a terminal window. On the Mac, the Terminal is in `/Applications/Utilities`. Type

         Anaconda-

 and then press tab. The name of the file you just downloaded  should appear.
    
2.Press enter. You will follow the text-only prompts. When there is a colon at the bottom of the screen press the down arrow to move down through the text. Type `yes` and press enter to approve the license. Press `enter` to approve the default location for the files. Type yes and press enter to prepend Anaconda to your `PATH` (this makes the Anaconda distribution the default Python).
    Done!

___Windows___

For Windows we recommend the [Enthought Canopy](https://www.enthought.com/downloads/) distribution since it seems to work well with Git Bash.

For other options check the Python4Astronomers page on [installing scientific Python](http://python4astronomers.github.com/installation/python_install.html).



