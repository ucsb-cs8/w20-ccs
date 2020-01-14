---
assigned: 2020-02-05 12:30
csxx: cs20
desc: min/max, index vs. value
due: 2020-02-14 12:30
layout: lab
num: lab06
prev_lab: lab05
ready: true
starter_code_repo: https://github.com/ucsb-cs8-s18/cs8-s18-lab06-starter-code

---

# You may pair or work alone on this lab.

If you choose to pair, please start by registering your pair on Gradescope in the normal way.

# Instructions

This lab proceeds in an identical fashion to {{page.prev_lab}}.  The topics are different,
but the way of working is the same.

For this lab, you will create two files:

* <tt>{{page.num}}.py</tt>, a file containing some function definitions
* <tt>{{page.num}}_tests.py</tt>, a file containing some test cases

There is starter code for each of these (`.py` files) at the following link:

* <{{page.starter_code_repo}}>

I suggest you proceed as follows:

1.  Create a directory called <tt>~/{{page.csxx}}/{{page.num}}</tt> (using the <tt>mkdir</tt> command) and <tt>cd</tt> into that directory.
2.  Use <tt>idle3</tt> (you might try <tt>idle3 &</tt> if you want to keep your prompt handy) to bring up `idle3`.
3.  Use `New File` to create empty files called <tt>{{page.num}}.py</tt> and <tt>{{page.num}}_tests.py</tt> in that <tt>~/{{page.csxx}}/{{page.num}}</tt> directory.
4.  ONE AT A TIME, copy the function definitions from the starter code, and the tests that go along with those, and get the tests to pass.
   * By one a a time, what I mean is, at your first step, copy ONLY the first function definition from  the starter code <tt>{{page.num}}.py</tt> and copy only the test cases from <tt>{{page.num}}_tests.py</tt> that go with that function definition.
   * Then, before you move on to the next function definition and <em>its</em> tests, get all of the tests from the one you just copied to pass.
   * Then, and only then, copy the next function definition and its tests into your files.
   * Repeat this until you have ALL of the function definitions and their tests, and all of them pass.
   
Note that what you are given differs from function to function: either a complete function definitions 
* In some cases you are given a function definition that is complete, but contains a bug.  In this case, you 
   need to fix the function definition.
* In some cases you are given a function definition that is correct. In this case, the code is there for you as an example&mdash;it is code that may be helpful to you in writing the other function definitions in the lab.   There is nothing you need to do other than study the code to learn how it works.
* In some cases, you are given a stub.

When you've done that, you are ready to try submitting to submit.cs for a final grade.  HOWEVER, you are encouraged to try submitting to submit.cs earlier, for several reasons:

* You can get partial credit if some of your tests pass for some of your functions
* You will have a backup of your file in case you accidentally delete yours from CSIL, or in case your laptop dies
* You can move code between your laptop and CSIL by downloading your code from the submit.cs submission
* You can ask the instructor or TA questions about your code on Piazza in a private instructor post.

# A Useful tip

As you know, this Unix shell command runs the tests in {{page.num}}_tests.py


<p markdown="1">
<tt>python3 -m pytest {{page.num}}_tests.py</tt>
</p>


If you have LOTS of tests in your file, and you ONLY want to run some of them, you can use <tt>-k string</tt> to run ONLY the tests that contain a certain string.  For example, suppose you want to focus ONLY on the tests for <tt>isList</tt>.  You can run:

<p markdown="1">
python3 -m pytest {{page.num}}_tests.py -k isList
</p>

Change <tt>isList</tt> to any function that you want, and only the tests that contain that string will be run.  The others will be "de-selected".


# Submission

Submit your code by going to Gradescope and finding the submission link for
{{page.num}}.

Navigate to that page, and upload your <tt>{{page.num}}.py</tt> file.

