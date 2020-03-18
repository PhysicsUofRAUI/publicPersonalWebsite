#!/bin/bash
export SECRET_KEY='p9Bv<3Eid9%$i01'
export SQLALCHEMY_DATABASE_URI='mysql+mysqldb://pwAdmin:h0ngk0ng@localhost/pw'
export FLASK_CONFIG=development
export FLASK_APP=run.py
python3 -m flask run
