## Follow [the link](http://grozzmaster.pythonanywhere.com) to see it in action!

### How to deploy it (for example, on your local machine):

#### First of all, clone this repository:
$ cd /your/preferred/path & git clone https://github.com/novitskiy/network.git

#### Create a new virtual environment
$ virtualenv --python=python3.6 shopenv

#### Activate the environment
$ source shopenv/bin/activate

#### Install required dependencies
$ pip install -r net/requirements.txt

#### Run test server
$ python net/manage.py runserver

#### Check localhost:8000 in your browser
And get fun!


