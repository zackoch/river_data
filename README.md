```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# running manually (if venv is activated)
`python main.py`

# cron job example
`5 * * * * ~/river_data/venv/bin/python3 ~/river_data/main.py`
