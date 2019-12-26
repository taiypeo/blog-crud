# Setting up
```
pip install -r requirements.txt
export SECRET_KEY="YOUR SECRET KEY"
flask db init
flask db migrate
flask db upgrade
```

# Mocking data
```
source tools/mock.sh
```

# Running
```
python main.py
```
