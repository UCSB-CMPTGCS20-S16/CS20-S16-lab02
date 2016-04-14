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


Step 1: Bring up an IDLE session
--------------------------------

Bring up an IDLE session.

Though it isn't required, it is encouraged that you do this lab on your CSIL account to learn a bit about working with Linux.

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

-   cd is the "change directory" command
-   mkdir is the "make directory" command
-   pwd is the "print working directory" command
-   Your home directory is something like
    <strong>/cs/student/jsmith</strong> or
    <strong>/engr/student/mdiaz</strong>
    </li>
-   Under that, you might have a directory cs20—that would show up as
    <strong>/cs/student/jsmith/cs20</strong>, or
    <strong>/engr/student/mdiaz/cs20</strong>

A new command for this lab is the `ls` command.

-   That's lowercase L and S as in the word LIST
-   It stands for "list files". It gives you a list of the files in the
    current working directory.

At the command prompt, type each of these commands. The part you type is
shown after the -bash-4.2\$ prompt. (Note: Your prompt may be slightly
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

Step 3: Copy some code into [lab03Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Funcs.py) under your cs20/lab03 folder
-----------------------------------------------------------------------------------------------------------------------------------------

In IDLE, select "File=&gt;New Window" to open a new "untitled" window
for Python code.

When it comes up, click and drag the window by its title bar over to the
right of your Python Shell window.

Now, open the following link: [lab03Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Funcs.py)
* You may want to "right click", or on Mac, "control-click", to open it in a new window or tab
* Here is a the same file with formatting and line numbers:  [lab03Funcs.py](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/blob/master/lab03Funcs.py)

Copy and paste this code into a new Python file with the name `lab03Funcs.py` and save it&mdash;we'd suggest storing this in the cs20/lab03 folder you created at an earlier step.

Step 4: Copy some more code into [lab03Tests.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/master/lab03Tests.py) under your cs20/lab03 folder
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
`\~/cs20/lab03` directory, you are good to move on to the next step.

Note that `\~` is a symbol that means "your home directory".

Step 5: Fixing function stubs, adding functions, adding tests
-------------------------------------------------------------

As we discussed in lecture, when writing functions along with test
cases, we often start with "stub" versions.

These allow us to "test the test" to make sure that when the function is
bogus, that the tests work correctly.

If you look through the lab03Funcs.py file, you will see several
function definitions that are "stub" versions.

Run the lab03Tests.py file, and you'll see that many of the tests are
failing, because the function in question returns the string "stub"
instead of the answer that it should.

Go through the file, and replace the stubs with correct values.

In addition, you'll also find:

-   several places in `lab03Funcs.py` where there are comments with "@@@"
    signs that tell you to add new function definitions.
-   several places in `lab03Tests.p`y where there are comments with "@@@"
    signs that tell you to add new test cases

Follow all of the instructions.

-   As you follow the instructions with the @@@ in them, it is good practice to REMOVE THE
    COMMENTS THAT HAVE THE @@@ IN THEM.

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

To use it, select the File-&gt;New option in idle, and create a new
blank Python file. Copy the code from
[testHelper.py](http://www.cs.ucsb.edu/~pconrad/cs20/14S/labs/lab03/testHelper.py)
into that file, and choose Run-&gt;Run Module (or press F5).

You should see that it runs ONLY the tests that pertain to the function
`isSimpleNumeric`. That's because the function call at the bottom of the
file, the one that is called when the file is run, specifies to only run
tests from `lab03Tests.py` that start with `test\_isSimpleNumeric`

You can edit the last line of this file to be whatever function you are
focussing on. Remember to start the second parameter with `test\_`, such as
`test\_isSimpleNumeric`, `test\_isPrimaryColor`

Step 6: Submit your assignment using the submit.cs program
----------------------------------------------------------

TODO: Add submit.cs link here.
