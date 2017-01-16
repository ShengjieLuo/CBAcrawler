export CBA_HOME=/root/CBAcrawler

apt-get install -y python python-pip python-lxml
pip install requests
cd $CBA_HOME/sql-connector-python-1.0.11
python setup.py install
