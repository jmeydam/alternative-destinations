# Alternative Destinations
Web service built with Flask.

Initial version based on *Flask Web Development*, second edition, by Miguel Grinberg (O'Reilly, 2018).

## Create virtual environment

```
virtualenv -p $(which python3.6) venv
source venv/bin/activate
pip install -r requirements.txt
```

## Set environment variables

```
export FLASK_APP=alternative-destinations.py
export FLASK_DEBUG=1
```

## Create dev database

```
python create_dev_db.py 
```

## Run tests

```
flask test
```

## Run application

```
flask run
```
