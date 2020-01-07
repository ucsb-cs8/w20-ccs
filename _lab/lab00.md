---
assigned: 2020-01-07 15:00
desc: Getting Started
due: 2020-01-12 00:00
layout: lab
num: lab00
ready: false

---

# Introduction

This lab is an introduction to Python programming.  You will write your first Python program that will print a specific text output on your computer display. 

## Goals for this lab

By the time you have completed this lab, you should be able to:

* perform basic management of directories and files
* create Python progams in IDLE 
* submit an assignment using the gradescope system
   
This assignment is designed to make sure you are comfortable working in the 
computing environment and know how to submit your work. It is mostly about
mechanics, not concepts. As a result, this assignment is not particularly intellectually
challenging. Future labs will require quite a bit more thought!

# Step by Step Instructions



## Step 1: Bring up a "terminal" 
 
On Mac or Linux, use the terminal app to bring up a command line.

On Windows, use "git bash here".
* This assumes you have already installed "Git for Windows" and "Python for Windows", with adding Python into the path.

<div style="float:right; width:100px; border: 1px solid #063;" markdown="1">
![terminal icon](Terminal.png)
</div>

Here's how:

* Find the Applications Menu at the top left of the screen.
* Select System Tools, then Terminal (the icon should look like the image shown at right).
* A Terminal Window should pop up.

## Step 2: Create some directories

At the command prompt, we are going to type several commands to create folders
(called &quot;directories&quot;) on Linux in which you can store your programs.The
commands are shown in the box below&mdash;but first, a little explanation.

Each of the <strong>cd</strong> commands shown below is a command to &quot;change
directory&quot;&mdash;that is to move into a different folder on the hard drive.


*  When you type <strong>cd</strong> by itself, it takes you to your
   'home directory'.
*  cd followed by a directory name (e.g. <strong>cd cs8</strong>)
   moves you into
   a directory under the current one
   
Each of the <strong>mkdir</strong> commands &quot;makes a new directory&quot;
(i.e. a new folder).

* For example,<strong> mkdir cs8</strong> creates a new directory called cs8 inside the current directory.

Each of the pwd commands &quot;prints the working directory&quot;,
i.e. it tells you where you are on the hard drive.

*  Your home directory is something like <strong>/cs/student/jsmith</strong>
   or <strong>/engr/student/mdiaz</strong>
*  Under that, you might have a directory cs8&mdash;that would show up as
   <strong>/cs/student/jsmith/cs8</strong>, or <strong>/engr/student/mdiaz/cs8</strong>


At the command prompt, type each of these commands. What you type is shown in bold.
You should get back exactly the output shown, (except that the part in italics may be different&mdash;each user will have something different show up there.)

NOTE: your prompt may not be exactly like the one shown here.  Instead of `-bash-4.2$ `, you might have something like `[cgaucho@cstl-15 ~]$ `.    The `cgaucho` here is your username, the `cstl-15` is where you are logged in, and the `~` is your current directory.    Don't be distracted by this detail.

<pre>-bash-4.2$ <strong>cd</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>
-bash-4.2$ <strong>mkdir cs8</strong>
-bash-4.2$ <strong>cd cs8</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/cs8
-bash-4.2$ <strong>mkdir lab00</strong>
-bash-4.2$ <strong>cd lab00</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/cs8/lab00
-bash-4.2$ <strong>cd</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>
</pre>

## Step 3: Checking if it worked

To see if it worked, you can use the file manager on the desktop. Drag
any windows that might be covering up the &quot;Home&quot; icon on
your desktop&mdash;it should be near the upper left hand corner of the
screen.  When you double click on this icon, it will bring up your
home directory. You should see inside a folder called cs8. If you
double click on that, you should see inside of it, a folder called
{{page.num}}.

Note that you could also use mouse clicks and menu options to create
these folders, instead of the command line. If you have trouble with
the command line, then for today, it is ok to do it that way.
 
Eventually, though, we want you to learn some of the Unix commands
also&mdash;the reasons it is important to know both will become more
clear as you move deeper into the study of programming and Computer
Science.

## Step 4: Bring up the program called IDLE

The preliminaries are done&mdash;now we are ready to start saving files
for Python!

IDLE is a piece of software that you use to interact with the Python programming language. As we are using Python version 3 in this class, we also use IDLE version 3.

Type the following at the command prompt:

<pre>-bash-4.2$ <strong>idle3</strong>
</pre>

The window that appears should have the Python Command prompt (&gt;&gt;&gt;)
in it.

* This is sometimes called the &quot;Python Command Prompt&quot; window.
* This is also called the &quot;Python Shell&quot; window.

When you have the IDLE window up, you are ready for the next step.

## Step 5: Save a file in IDLE

In IDLE, select "File=&gt;New File" to open a new "untitled" window for Python code.

When it comes up, click and drag the window by its title bar over to the right
of your Python Shell window.
 
For this lab, there is one goal: write a Python 3 program that prints the string `Hello, World!` as its output.


In this sense, we are following a long tradition: for [more than 40 years](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) it has been a tradition to make printing `Hello, World!` be the first thing you do when learning a new programming language.

In Python 3, this program is very short.  It looks like this:

```python
print ('Hello, World!')
```

We will save the file under the name `hello.py`&mdash;it is <strong>very important</strong> that is has exactly that name, or the gradescope system will not run your program correctly.

That's it!   Now, you can also add, on the first line, a *comment* with your name, and information about the course, for example:

```python
# Chris Gaucho, for CMPSC 8, Winter 2018
print ('Hello, World!')
```

You are encouraged to do that, because it helps someone looking at your code know that *you* wrote it.  But, other than that, it isn't necessary.  In general, in computer programming, a *comment* is something that is intended only for human readers of the code, and is otherwise "ignored by the system".   Nearly every programming language has some way to express comments, though the exact rules for formatting of comments--that is, the *syntax* of comments--differs from one language to another.

In Python, a `#` starts a comment.  Everything from the `#` to the end of that line is part of the comment.

Enter this program in IDLE, then save it under the name `hello.py`

## Step 6: Running your program.

To run your program, select the "Run=>Run Module" option from the menu. You should see the "Hello World!" message.

I'll demonstrate the use of Idle in lecture, since its much easier to just follow along than to try to explain everything in a text document. If you need a further demonstration, you can find one on YouTube. For example: 
[This video starting at 4:53](https://www.youtube.com/watch?v=kXbpB5_ywDw&t=4m53s)  (That video is for Python 3.1, but the stuff shown in the video is the same across all versions of Python 3.x).

## Step 7: Uploading your program to Gradescope

<div style="width:350px; text-align:center; float:right;" markdown="1">

![Gradescope upload](Gradescope_upload.png)

</div>

Next, we'll try submitting our program to Gradescope.  You'll get some immediate feedback on whether you did it properly.

If you are registered for the course, you are should also be registered at Gradescope.com (via your @umail.ucsb.edu account) Look in your @umail account for an email from the Gradescope system inviting you to create a password. Follow the instructions to set your password; then you should see "CMPSC 8" in your courses for this term.

The lab assignment "Lab00" should appear in your Gradescope dashboard under CMPSC 8. If you haven't submitted anything for this assignment yet, Gradescope will prompt you to upload your files. This prompt is shown below:

You either can navigate to your file(s) or "drag-and-drop" them into the "Submit Programming Assignment" window.

After you submit something on Gradescope, you will have access to the "Autograder Results" page. There is a "Resubmit" button on the bottom right that will allow you to update the files for your submission.   For this lab, if everything is correct, you'll see a successful submission passing all of the autograder tests shown below.

<div style="clear:both;" markdown="1">
  
![Gradescope results](Gradescope_results.png)

</div>

If the tests don't pass, you may get some error message that may or may not be obvious at this point. Don't worry - if the tests didn't pass, take a minute to think if your print statement is <strong>EXACTLY</strong> like stated in the lab instructions (including the same capitalization, spaces, punctuation, etc.) and the file name is <strong>EXACTLY</strong> `hello.py`. If your tests didn't pass and you're still not sure why you're getting the error, feel free to ask one of the course helpers. 

