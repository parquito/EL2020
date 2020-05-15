#!/usr/bin/python
from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json
import RPi.GPIO as GPIO
import time

con = sql.connect('smokeLog.db')
cur = con.cursor()

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/sqlData")
def chartData():
	con = sql.connect('smokeLog.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, Smoke FROM smokeLog")
	dataset = cur.fetchall()
	print (dataset)
	chartData = []
	for row in dataset:
		chartData.append({"Date": row[0], "Smoke": row[1]})
	return Response(json.dumps(chartData), mimetype='application/json')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=2020, debug=True, use_reloader=False)
