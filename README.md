# benford_flask_app

The application plots the distribution of the first digit for each population count from the 2009 US Census data. 

Benford's law states (from google): the principle that in any large, randomly produced set of natural numbers, 
such as tables of logarithms or corporate sales statistics, around 30 percent will begin with the digit 1, 18 percent with 2, and so on, with the smallest percentage beginning with 9. The law is applied in analyzing the validity of statistics and financial records.

The application tests Benford's law for the 2009 US census data and produces a validation condition, stating whether Benford's law has is observed using the census data. Validition conditions for each starting digit 1 through 9 was met if the percent difference between the observed frequency and expected frequency was less than or equal to 0.05 (5%). The expected frequencies used for validation were obtained from the Wolfram Alpha website (http://mathworld.wolfram.com/BenfordsLaw.html) and are: 

D	  P_D	      
1	  0.30103	    
2	  0.176091	  
3	  0.124939	
4	  0.09691	  
5	  0.0791812
6   0.0669468
7   0.0579919
8	  0.0511525
9	  0.0457575

In addition, the percent differences between observed and expected frequencies of leading digits are supplied in table.






Instructions for running application through Docker: 

Option 1: Pulling the docker image from docker hub

From the terminal use command:

docker pull heymanitshayden/benford_app:v.0.1.0

This command will pull the image tag "v.0.1.0" from the Docker hub repository "benford_app"

Next, from the terminal use command: 

docker run -v $(pwd):/opt -p 5001:5000 --rm heymanitshayden/benford_app:v.0.1.0  flask run --host 0.0.0.0 --port 5000

You should see some information printed that looks similar to: 
 * Serving Flask app "benfords_law_app.py" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 324-426-855

This will run the application on a Flask development server. To view the application's output travel to http://localhost:5001

Option 2: Building the docker image from the supplied directory 

If desired, make a fresh new directory to hold the benford_flask_app directory downloaded. Through the terminal travel to the downloaded directory. Confirm that all needed files and subdirectories are present by: issueing ls -a command. The following items should be present in working directory: 

2009_census.txt 
dockerfile 
requirements.txt
templates
static
benfords_law_app.py

Once confirmed that items are present, within the working directory, build the docker image by using the command: 

docker build -t benford_app . 

If image was build correctly without any errors you should see: 
Successfully build: 'ImageID' 
Successfully tagged: 'latest'

To confirm image is present before proceeding, issue command: 

docker images 

Printed will be a list of all created docker images. You should see under the REPOSITORY column the image "benford_app". Additionally, you should see the repository's image id under the column "IMAGE ID". IF the image is created successfully then proceed to running the container by issuing the command: 

docker run -v $(pwd):/opt -p 5001:5000 --rm heymanitshayden/benford_app:v.0.1.0  flask run --host 0.0.0.0 --port 5000



You should see some information printed that looks similar to: 
 * Serving Flask app "benfords_law_app.py" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 324-426-855

This will run the application on a Flask development server. To view the application's output travel to http://localhost:5001




