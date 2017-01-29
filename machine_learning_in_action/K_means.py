from __future__ import division
import numpy as np

class kMeans:
    '''
    a K-means clustering algorithm implemenration with user defined minkowski distance
    '''
    #
    import numpy as np

    #Helper functions
    #1. read in text data, separate each line by \t, output list of list of numeric numbers
    def loadDataSet(self, fileName):
        '''
        :param fileName: input data file directory + name
        :return: data_mat, matrix format (list of list) float data
        '''
        data_mat = []
        with open(self.fileName, 'w') as infile:
            for line in infile.readlines():
                curLine = line.strip.split('\t')
                fltLine = map(lambda x: float(x), curLine)
                data_mat.append(fltLine)
        return data_mat


    #2. calculate Minkoswki distance
    def minkowski_distance(self, vecX, vecY, p):
        '''
        :param vecX: vector X to compute with vector Y for  minkowski distance
        :param vecY: vector Y to compute with vector X for  minkowski distance
        :param p: minkowski p for (|vecX - vecY|^p)^(1/p)
        :return: distance: the calculated minkowski distance
        '''
        np.power(np.sum(np.power(np.abs(vecX - vecY),p)), 1/p)
        return distance



    #K-means algorithm
    def kMeans(self, data_mat, k):
        '''
        :param data_mat:
        :param k:
        :return: classAssign: a matrix
        '''
        classAssign = []
        return classAssign

