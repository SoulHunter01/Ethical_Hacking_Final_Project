This is a Simple Python Keylogger that mails you all the captured keys it captures after a specific time interval.

This python if executed as it is on Windows will be detected. To protect it from being detected by Windows,
A third party software Nuitka has to be downloaded to convert the .py file to .exe file.
Follow these instructions to execute this keylogger Successfully.

Installing Nuitka on Windows:

1. Go to https://nuitka.net/
2. Go to the Downloads Section of the website https://nuitka.net/doc/download.html
3. Download the most recent version of Nuitka from the Packages Section.
4. Run the Downloaded installer
5. If you get a prompt warning you about the software, click on More Info and Click on 'Run Anyway' option.
6. Click on Install for All Users and then Click Next
7. Specify the Python 3.9 compiler you want to use. Might be easiest to just use the Python 3.9 from registry
8. Do you want to allow app to make changes (Select Yes)
9. Click on Finish to Install the software.
10. Open your Windows terminal and verify your installation by entering this command:
      nuitka --version

How to convert the keylogger into .exe format:

1. Open the terminal in the folder containing the keylogger.
2. Run the following command:
      py -m nuitka --mingw64 filename.py --standalone --onefile
3. An executable file will be generated in the same folder which can be copied easily to the victim computer.
