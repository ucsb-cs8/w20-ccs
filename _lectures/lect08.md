---
num: "lect08"
lecture_date: 2019-01-31
desc: "Flask"
ready: true
---

* [Flask](http://flask.pocoo.org/) is a Python framework for building webapps.
* Python Web apps built with Flask can be deployed to the web at no cost via the free tier of [Heroku](https://heroku.com).
* [Bootstrap](https://getbootstrap.com/) is a framework that allows you to quickly make websites that look professional

Today, we'll dive into building sites with Flask and Bootstrap on Heroku.

# Two Alternatives

* Dive into the deep end with this comprehensive tutorial: <https://github.com/pallets/flask/tree/master/examples/tutorial/>
* Go slow approach, going a little at a time through this: <http://flask.pocoo.org/docs/1.0/quickstart/>

# Very Slow Approach

1. Create a github.com account and verify your email address
2. Create a heroku.com account and verify your email address
3. Create a repo called `try_flask`; the exact name is not important
4. Go into some folder where you do your work for this course.
5. Copy the URL from the green button for "Clone with HTTPS"
6. Type `git clone ` followed by the URL that you copied
7. Create a new file on the website for your repo called `hello.py`
8. Paste into that file the contents from here: <http://flask.pocoo.org/docs/1.0/quickstart/>
9. Back at your command line, type `git pull origin master` and you should see the `hello.py` file come into
   your local directory.
10. Then, type this to define an environment variable `FLASK_APP`:
   ```
   export FLASK_APP=hello.py
   ```
   
   On Windows Powershell, instead use:
   
   ```
   $env:FLASK_APP="hello.py"
   ```
   
 11. Use this command to be sure flask is installed in your local Python:
   ```
   pip install flask
   ```
   
   If you normally use `pip3` instead, do that here:
   
   ```
   pip3 install flask
   ```
   
 12. Use this command to start your server:
   ```
   flask run
   ```
   
# Troubleshooting

If you get this warning:

```
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
```

Here's how to fix it:

```
export FLASK_ENV=development
```

# Getting it running on Heroku

1. If you didn't already, create an account at <https://heroku.com> and verify your email address.
2. Go to <https://dashboard.heroku.com>
3. Click "New", then select "Create new app" to create a new heroku app.  Give it a name such as `chris-try-flask` or `try-flask-chris`.  The name has to be
   unique in all the world, so it's helpful to put your own personal name into the name somehow.   The name will 
   eventually be your url, i.e. `https://try-flask-chris.herokuapp.com`
   
4. At the webpage of your github.com repo, click "Create new file" and make a new file called `Procfile`.  It must be
   called exactly that, with exactly that sequence of upper and lowercase: capital `P`, lowercase `rocfile`.

   In the file, put this:
   ```
   web: gunicorn hello:app
   ```

5. Use this command to be sure `gunicorn` is installed in your local Python 3 system:
   ```
   pip install gunicorn
   ```
   
   If you normally use `pip3` instead, do that here:
   
   ```
   pip3 install gunicorn
   ```
   
 6. Create a new file called `requirements.txt` (exactly that spelling, and all lowercase).  
    It should have the following in it.
  
    ```
    Flask
    gunicorn
    ```

7.  Go back to the heroku dashboard, and select your app.  For example, if you called your app `phill-try-heroku`,
    you should be able to click on `phill-try-heroku`and end up at this url: 

    * `https://dashboard.heroku.com/apps/phill-try-heroku`
    
    From there, there should be an option to click where it says "Deploy". Click on that.
    
    
