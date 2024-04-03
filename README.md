

```bash
git pull https://github.com/zackoch/river_data .
cd river_data
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# running manually (if venv is activated)
`python3 main.py`

# cron job example
`5 * * * * ~/river_data/venv/bin/python3 ~/river_data/main.py`
