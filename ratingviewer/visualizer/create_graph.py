import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime

import hashlib

def create_rating_graph(matrix):
    plt.figure()
    x_axis = []
    x_labels = []
    y_axis = []
    for m in matrix:
        x_labels.append(m["update_month"])
        x_axis.append(datetime.datetime.strptime(m["update_month"],"%Y-%m"))
        y_axis.append(int(m["rating"]))
        
    plt.plot(x_axis, y_axis)
    plt.xticks(x_axis,x_labels)
    filename = hashlib.sha224(str(datetime.datetime.now().timestamp()).encode('utf-8')).hexdigest()

    plt.savefig('visualizer/static/visualizer/images/' + filename + '.png')
    
    return filename

if __name__ == "__main__":
    print(create_rating_graph([{"update_month": '2019-05',"rating": 1800},
                         {"update_month": '2019-06',"rating": 1900},
                         {"update_month": '2019-07',"rating": 1770}]
    ))