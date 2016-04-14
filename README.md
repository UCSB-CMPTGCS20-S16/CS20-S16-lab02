# CS20-S16-lab02

Introduction
============

Writing functions and tests
---------------------------

In this lab, we'll build on what we started in lab01---writing functions
and tests.

- You may work individually, OR in a pair.
- If you work in a pair, please "register" as a pair on submit.cs so that your submission there is recorded for both students (instructions on how to do that will be explained later in this lab.)

Step by Step
============



Step 0: Connect to CSIL (optional, but recommended)
---------------------------------------------------
Though it isn't required, it is encouraged that you do this lab on your CSIL account to learn a bit about working with Linux, in general, and the CSIL machines in particular.

As a reminder, for working on CSIL, you need:

* a CSIL/ECI account, which you set up at https://accounts.engr.ucsb.edu
* a machine name to connect to from [this list of CSIL machines](http://www.engr.ucsb.edu/eci/kb/index.php?action=artikel&cat=14&id=68) such as `pinky.cs.ucsb.edu`, `brain.cs.ucsb.edu`, `shaggy.cs.ucsb.edu`, etc.

Though the "default" machine name is `csil.cs.ucsb.edu`, it is strongly recommended to choose one of the other machines on that list, especially if you are bringing up IDLE. (It's less important if you are just doing Linux shell commands, or working at the Python `>>>` prompt.)

As for how to connect, assuming `jgaucho` is your CSIL/ECI username:

* From Windows, it is recommended that you use the free home edition of [Mobaxterm](http://mobaxterm.mobatek.net/download-home-edition.html) to create an SSH session.  Enter the machine name and username in places indicated.   For the "port number", leave the default (22) just as it is.
* From Mac OS, : use `ssh -X jgaucho@somemachine.cs.ucsb.edu` where `somemachine` is a machine from [the list of CSIL machines](http://www.engr.ucsb.edu/eci/kb/index.php?action=artikel&cat=14&id=68).  You may need to [download and install XQuartz](http://www.xquartz.org/) first to get the graphics to work. 
* From Linux, it "just works": use `ssh -X jgaucho@somemachine.cs.ucsb.edu` where `somemachine` is a machine from [the list of CSIL machines](http://www.engr.ucsb.edu/eci/kb/index.php?action=artikel&cat=14&id=68)

Assuming you've managed to log in and get a CSIL shell prompt (which may look something like this: `-bash-4.3$ `) you are ready to move on to the next step.


Step 1: Bring up an IDLE session
--------------------------------

Bring up an IDLE session.

If you do this on CSIL account, you may way to bring up two terminal windows where you are connecting to CSIL.

-   In one of them, type idle to bring up the IDLE
    development environment.
    -   In that window, you won't get a bash prompt back until you exit
        from idle, so that window isn't really of much use to you after
        type idle.    (Or, you can use `idle &` to start idle, and get back your prompt.)
    -   Don't close it though, because if you do, IDLE might crash too.
        You can minimize it though, or drag it out of the way.
-   Keep the other terminal window handy, so you'll have the bash shell
    prompt at your fingertips. That will give you a place to do file
    commands as needed.


Step 2: Creating some directories
---------------------------------

In the window with the bash shell prompt (`-bash-4.2$`), we will type
some commands to create a directory (folder) for lab03.

Here are some basics of Linux shell commands:

-   `cd` is the "change directory" command
-   `mkdir` is the "make directory" command
-   `pwd` is the "print working directory" command
-   Your home directory is something like
    `/cs/student/jsmith` or
    `/engr/student/mdiaz`
    
-   Under that, you might have a directory cs20—that would show up as
    `/cs/student/jsmith/cs20`, or
    `/engr/student/mdiaz/cs20`

-   The `ls` command is used to list files
 -   That's lowercase L and S as in the word LIST
 -   It stands for "list files". It gives you a list of the files in the
     current working directory.

At the command prompt, type each of these commands. The part you type is
shown after the `-bash-4.2$` prompt. (Note: Your prompt may be slightly
different.)

    -bash-4.2$ cd
    -bash-4.2$ pwd
    /cs/student/yourusername
    -bash-4.2$ cd cs20
    -bash-4.2$ pwd
    /cs/student/yourusername/cs20
    -bash-4.2$ ls
    lab00
    -bash-4.2$ mkdir lab03
    -bash-4.2$ ls
    lab00    lab03
    -bash-4.2$ cd lab03
    -bash-4.2$ pwd
    /cs/student/yourusername/cs20/lab03
    -bash-4.2$

Step 3: Copy some code from [lab03Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Funcs.py) 
-----------------------------------------------------------------------------------------------------------------------------------------

In IDLE, select "File=&gt;New Window" to open a new "untitled" window
for Python code.

When it comes up, click and drag the window by its title bar over to the
right of your Python Shell window.

Now, open the following link: [lab03Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Funcs.py)
* You may want to "right click", or on Mac, "control-click", to open it in a new window or tab
* Here is a the same file with formatting and line numbers:  [lab03Funcs.py](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/blob/master/lab03Funcs.py)

Copy and paste this code into a new Python file with the name `lab03Funcs.py` and save it&mdash;we'd suggest storing this in the cs20/lab03 folder you created at an earlier step.

Step 4: Copy some more code from [lab03Tests.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Tests.py)
----------------------------------------------------------------------------------------------------------------------------------------------

Now we are going to do the same thing again, with a second file of
Python code.

In IDLE, select "File=&gt;New Window" *again* to open *yet another* new
"untitled" window for Python code.

When it comes up, click and drag the window some place so that you can
get to it, your lab03Funcs.py window, and to your Python Shell window
easily by clicking.

Now, open this web link. (You may want to "right click", or on Mac,
"control-click", to open it in a new window or tab.)

Now, open the following link: [lab03Tests.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Tests.py)
* Here is a the same file with formatting and line numbers:  [lab03Tests.py](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/blob/master/lab03Tests.py)

Copy and paste this code into a new Python file with the name `lab03Tests.py` and save it&mdash;in the same folder as the lab03Funcs.py file from earlier.

If you are working on CSIL, after saving these two  files, go to your bash shell prompt window, and type
`pwd` to make sure you are still in your `cs20/lab0`3 directory under your
home directory. If not, then use `cd` `~/cs20/lab03` to get into that
directory.

    -bash-4.2$ pwd
    /cs/student/yourusername/cs20/lab03
    -bash-4.2$

Then use the `ls` to list files. You should see a result like this:

    -bash-4.2$ ls
    lab03Funcs.py      lab03Tests.py
    -bash-4.2$

If you don't, then you did something wrong. Try saving the file again,
and make sure you navigate to the `cs20` folder, then the lab03 folder, and
save the file under the name `lab03Tests.py`.

As before, upper vs. lower case matter. Save it again if you didn't get
it exactly right the first time, and use the `rm` command to remove
(delete) any files that are in the wrong place.

Once you see that you have `lab03Funcs.py` and `lab03Tests.py` under your
`~/cs20/lab03` directory, you are good to move on to the next step.

Note that `~` is a symbol that means "your home directory".

Step 5: Fixing function stubs, adding functions, adding tests
-------------------------------------------------------------

As we discussed in lecture, when writing functions along with test
cases, we often start with "stub" versions.

These allow us to "test the test" to make sure that when the function is
bogus, that the tests work correctly.

If you look through the lab03Funcs.py file, you will see several
function definitions that are "stub" versions.

Run the `lab03Tests.py` file, and you'll see that many of the tests are
failing, because the function in question returns the string `"stub"` or a weird value such as `-999.99`
instead of the answer that it should.

Go through the file, and replace the stubs with correct values.

In addition, you'll also find:

-   several places in `lab03Funcs.py` where there are comments with `@@@`
    signs that tell you to add new function definitions.
-   several places in `lab03Tests.py` where there are comments with `@@@`
    signs that tell you to add new test cases

Follow all of the instructions.

-   As you follow the instructions with the `@@@` in them, it is good practice to REMOVE the
    comments with `@@@`.  They are only there as placeholders and reminders, and don't belong in the final product.

You can always look back at the versions of the files on the web if you
want to see what the instructions originally said.


When you have:

-   fixed all the stubs, and the tests cases pass
-   added all the functions you are supposed to add
-   added all the test cases you are supposed to add

Then you are ready to submit!

### A few helpful hints

When you have a LOT of tests, it can get confusing. It may be more
convenient to focus on one function at a time.

Here is a link to a file that can do that: [testHelper.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/testHelper.py)
* Formatted version with line numbers: [testHelper.py](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/blob/master/testHelper.py)

To use it, select the File-&gt;New option in idle, and create a new
blank Python file. Copy the code from
[testHelper.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/testHelper.py)
into that file, and choose Run-&gt;Run Module (or press F5).

You should see that it runs ONLY the tests that pertain to the function
`isSimpleNumeric`. That's because the function call at the bottom of the
file, the one that is called when the file is run, specifies to only run
tests from `lab03Tests.py` that start with `test_isSimpleNumeric`

You can edit the last line of this file to be whatever function you are
focussing on. Remember to start the second parameter with `test_`, such as
`test_isSimpleNumeric`, `test_isPrimaryColor`

Step 6: Submit your assignment using the submit.cs program
----------------------------------------------------------

TODO: Add submit.cs link here.
