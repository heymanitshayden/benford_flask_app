#!/usr/bin/env/ python3

import re 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from flask import Flask, render_template

import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

pop = [] 

file = "/users/haydenthomas/desktop/flask_app/2009_census.dms"

f = open(file, 'r')

if f.mode == 'r': 

	for line in f: 
		line = line.rstrip()
		if line.startswith ("State"):
			next 
		else: 
			p = re.search(r'(\t(\d+)\s*)',line)
			if p: 
				pop.append(p.group(2))
				
one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0 
six_count = 0
seven_count = 0
eight_count = 0
nine_count = 0

for i in pop: 
	if i.startswith(str(1)):
		one_count = one_count + 1
	elif i.startswith(str(2)):
		two_count = two_count + 1
	elif i.startswith(str(3)):
		three_count = three_count + 1
	elif i.startswith(str(4)):
		four_count = four_count + 1
	elif i.startswith(str(5)): 
		five_count = five_count + 1
	elif i.startswith(str(6)):
		six_count = six_count + 1
	elif i.startswith(str(7)):
		seven_count = seven_count + 1 
	elif i.startswith(str(8)):
		eight_count = eight_count + 1
	elif i.startswith(str(9)):
		nine_count = nine_count + 1

def freq (count): 
	f = float(count/float(len(pop)))
	return f 
	
one_freq = freq(one_count)
two_freq = freq(two_count)
three_freq = freq(three_count)
four_freq = freq(four_count)
five_freq = freq(five_count)
six_freq = freq(six_count)
seven_freq = freq(seven_count)
eight_freq = freq(eight_count)
nine_freq = freq(nine_count)

x = [1,2,3,4,5,6,7,8,9]
y_o = [one_freq, two_freq, three_freq, four_freq, five_freq, six_freq, seven_freq, eight_freq, nine_freq]
y_e = [0.30103, 0.176091, 0.124939, 0.09691, 0.0791812, 0.0669468, 0.0579919, 0.0511525, 0.0457575]

x_array = np.array(x)
y_array = np.array(y_e)

xnew = np.linspace(x_array.min(), x_array.max(), 300)
spl = make_interp_spline(x_array, y_array, k = 3)
y_e_smooth = spl(xnew)

#plt.bar(x,y_o,label = "Observed Dist.")
#plt.plot(xnew, y_e_smooth, color = 'black', label = "Benford's Law")
#plt.xlabel('First Number')
#plt.ylabel('Frequency')
#plt.title("2009 Census Data vs. Benford's Law")
#plt.legend()

#my_plot = plt.show()

validated_count = 0
validated_list = []
validation_statement = ()

for i, f in zip(y_o,y_e): 
	pd = (abs(i - f)/f) 
	if pd <= float(0.05):
		validated_count = validated_count + 1
	validated_list.append(pd)
		
if validated_count == 9: 
	validation_statement = ("Benford's assertion is validated using the 2009 census data ")
		
else: 
	validation_statement = ("Benford's assertion is NOT validated using the 2009 census data ")
		
#val = (str(validation_statement))

app = Flask(__name__)

@app.route("/")
def home():
	plt.bar(x,y_o,label = "Observed Dist.", color = 'orange')
	plt.plot(xnew, y_e_smooth, color = 'black', label = "Benford's Law")
	plt.xlabel('Starting Number of City Population')
	plt.ylabel('Frequency')
	plt.title("2009 Census Data vs. Benford's Law")
	plt.legend()
	plt.savefig('/users/haydenthomas/desktop/flask_app/static/images/benford_plot.png')
	return render_template(
							'plot.html', name = '2009 Census Data: Distribution of Starting Number for Population', 
							url ='/static/images/benford_plot.png',
							condition = validation_statement)


	
	
	


if __name__ == '__main__':
	app.run(debug=True)