import radatools

import imp
try:
    imp.find_module('igraph')
    import plot_igraph
    can_plot_igraph = True

except ImportError:
    can_plot_igraph = False
    
