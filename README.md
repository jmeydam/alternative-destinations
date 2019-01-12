# Alternative Destinations
Web service built with Flask.

Initial version based on *Flask Web Development*, second edition, by Miguel Grinberg (O'Reilly, 2018).

## Create Virtual Environment

```
virtualenv -p $(which python3.6) venv
# also works on most systems:
# python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Set Environment Variables

```
export FLASK_APP=alternative_destinations.py
export FLASK_DEBUG=1
```

## Create .env File

Example:

```
cat .env
```

```
SECRET_KEY=a_secret_key
PASSWORD_USER_01=password_for_user_01
PASSWORD_USER_02=password_for_user_02
```

## Create Dev Database

```
python create_dev_db.py 
```

## Run Tests

```
flask test
```

## Run Application

```
flask run
```
