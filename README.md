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
6	 `0.0669468
7  `0.0579919
8	  0.0511525
9	  0.0457575

In addition, the percent differences between observed and expected frequencies of leading digits are supplied in table. 
