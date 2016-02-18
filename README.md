# Beer Style Clustering
### Nick McClure, February, 2016.

## Summary

We want to cluster beer styles based on ~100K reviews from a popular beer review site.  We know the review text and style of beer (approx 31 styles in data).  To accomplish this, we will normalize the review text, create features, and create 2 principle components via SVD and plot the average of the beers in each style.

## Software
This runs on Python3.X.
Libraries needed: numpy, scipy, sklearn, matplotlib, nltk (with stopword corpus).

## Data
Data is available here: https://www.dropbox.com/s/3jlokbq7tjnbyr2/beer_reviews.csv?dl=0

## Unit testing
With the python packages: 'nose' and 'coverage' installed, navigate to main directory and run:

    nosettests --with-coverage --cover-package=text_clustering_funs.py

To get the following outputs:

    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    test_beer.py                 13      0   100%
    text_clustering_funs.py      25      0   100%
    -------------------------------------------------------
    TOTAL                        38      0   100%
    -------------------------------------------------------
    Rand 3 tests in 1.789s
    
    OK

## Results

The following is a graph of the two larges principle components from the text features created.

[<img src="http://fromdata.org/wp-content/uploads/2016/02/BeerStyles.png">](http://fromdata.org/)
