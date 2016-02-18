##------------------------------------------------------------
##
## beer_text_clustering.py: Cluster Beer Styles by Review Text
##
## Purpose: Load a csv of about 75,000 beer reviews with
##          corresponding beer styles, and cluster based on
##          text features created from reviews of such beers
##          via the SVD principle components.
##
## Created: Feb, 2016
##
##------------------------------------------------------------
# Load libraries
import logging
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.font_manager import FontProperties
from importlib import reload
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
import text_clustering_funs


def main(input_file, text, target, output_file=None, num_components=2, plot_output=False):
    # Check 2d for plotting:
    if plot_output:
        assert(num_components == 2)

    # Load Data
    logging.info('Loading data file: ' + input_file)
    review_data = text_clustering_funs.csv_to_lists(input_file)

    # Extract Reviews and Styles
    reviews = [d[text] for d in review_data]
    styles = [d[target] for d in review_data]

    # Perform text normalization
    logging.info('Starting Analysis') # All the user really needs to know.
    logging.debug('Performing Text Normalization') # But we need to know where we are and how long we are taking
    reviews = text_clustering_funs.normalize(reviews, ['punctuation', 'numbers', 'stopwords', 'whitespace', 'lower'])

    # Create text features from reviews (straight from scikit documentation here)
    logging.debug('Creating Text Features')
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(reviews)

    # Transform data by SVD, store first X components
    logging.debug('Performing SVD and returning ' + str(num_components) + ' components.')
    svd_algo = TruncatedSVD(n_components=num_components, random_state=42)
    X_transformed = svd_algo.fit_transform(X_train_counts)

    # Plot average for each group
    if plot_output:
        logging.info('Plotting data')
        fontP = FontProperties()
        fontP.set_size('small')
        unique_styles = list(set(styles))
        colors = cm.rainbow(np.linspace(0, 1, len(unique_styles)))
        for i, style in enumerate(unique_styles):
            points = [val for ix, val in enumerate(X_transformed) if styles[ix] == style]
            avg_x = np.mean([p[0] for p in points])
            avg_y = np.mean([p[1] for p in points])
            col = colors[i]
            plt.plot(avg_x, avg_y, color=col, marker='o', ls='', label=style, markersize=20)
            plt.text(avg_x, avg_y, s=style, size='x-small')
            # And because 'old ale' is an outlier...
            plt.ylim([-0.6,-0.1])
            plt.xlim([0.6,1.3])
        plt.show()

    # Output Results:
    if output_file:
        logging.info('Saving results to output: ' + output_file)
        np.savetxt(output_file, X_transformed, delimiter=',')

if __name__ == "__main__":
    # Setup Logging
    today = datetime.date.today().strftime("%Y_%m_%d")
    log_file_name = 'log_' + today + '.log'

    logging.shutdown()
    reload(logging)
    logger = logging.getLogger()
    log_format = logging.Formatter("%(asctime)s - [%(levelname)-5.5s] %(message)s")

    # Setup file logging
    log_file_handle = logging.FileHandler(log_file_name)
    log_file_handle.setFormatter(log_format)
    log_file_handle.setLevel(logging.DEBUG)
    logger.addHandler(log_file_handle)
    # Setup screen logging
    log_screen_handle = logging.StreamHandler()
    log_screen_handle.setFormatter(log_format)
    log_screen_handle.setLevel(logging.DEBUG)
    logger.addHandler(log_screen_handle)

    # To-do:  Make the following inputs into system arguments:
    input_file = 'beer_reviews.csv'
    text = 'review'
    target = 'style'
    output_file = 'my_results.csv'
    num_components = 2
    plot_logical = True

    # Run analysis
    main(input_file, text, target, output_file, num_components, plot_logical)
