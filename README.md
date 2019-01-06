# Alternative Destinations
Web service built with Flask.

Initial version based on *Flask Web Development*, second edition, by Miguel Grinberg (O'Reilly, 2018).

## Create Virtual Environment

```
virtualenv -p $(which python3.6) venv
source venv/bin/activate
pip install -r requirements.txt
```

## Set Environment Variables

```
export FLASK_APP=alternative-destinations.py
export FLASK_DEBUG=1
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
