# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Deploying Your Models with Flask

> Unit 4: Flex

***NOTE: This flex lesson is a WIP. Please reach out to Jeff Boykin before using these materials in your cohort.***

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Deploying your models | [Here](./deploying-your-models.ipynb) |
| Data | Titanic and SMS Spam/Ham datasets | [Here](./data/) |
| Extra Materials  | Lesson code for Flask apps| [Here](./app/) |

---

## Learning Objectives

After this lesson, students will be able to:
- **Identify** use cases for *deploying* your ML models
- **Stand up** a Flask server and API endpoint
- **Respond** to an HTTP request with model predictions
- **Pickle** your trained models for later use
- **Pass arguments** to an endpoint via a simple web form

---

## Student Requirements

Before this lesson(s), students should already be able to:
- Use Anaconda for package management
- Build and evaluate predictive models using scikit-learn
- Recognize the role of HTTP requests and HTML

---

## Lesson Guide

> 180 mins

- Productionalizing and deploying
- Pickling
- Setting up a Flask server
- Designing your API
- Using an HTML form
- Takehome exercises
- Further reading


---

## Installation Notes
For this lesson, first install `pickle` and `flask`:

1. `conda install pickle`
1. `conda install flask`

---

## Additional Resources

For more information on this topic, check out:

- [The Flask Documentation](http://flask.pocoo.org/docs/0.11/)
- [A Flask tutorial to follow along with](https://github.com/miguelgrinberg/flask-pycon2014)
- [Another tutorial that gets into CSS styling](https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822)
- [The Flask mega tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [Flask's development server is not for production](https://stackoverflow.com/questions/12269537/is-the-server-bundled-with-flask-safe-to-use-in-production)
- [Setting up Flask on AWS EC2](http://bathompso.com/blog/Flask-AWS-Setup/). This should be your next step if you want to share your model with the world!
- [A great guide to those weird "decorators"](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).

### Production coding

- Add [logging](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) to your code; you'll be very glad you did.
- Think ahead and include [error handling](https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/), via [try/except clauses](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
- Get more comfortable with git, including [feature branching](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).
- Include [unit tests](http://www.diveintopython.net/unit_testing/index.html); the [pytest module](http://pythontesting.net/framework/pytest/pytest-introduction/) is great.
- [Integrate databases](http://zetcode.com/db/sqlitepythontutorial/)!
- Beware technical debt, especially [machine learning technical debt](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43146.pdf).
