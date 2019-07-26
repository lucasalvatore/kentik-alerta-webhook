# kentik-alerta-webhook
Custom webhook to send alerts from Kentik to Alerta <br>

copy setup.py and alerta_kentik.py into /opt/alerta directory <br>
activate venv if you installed alerta into one <br>
run `pip install -e .` or `python3 setup.py install` (i find pip works better)<br>
confirm your new webhook endpoint shows up in http://alerta-sample/api
