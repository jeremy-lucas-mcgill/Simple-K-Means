import numpy as np
class Data:
    def __init__(self,x_min,x_max,y_min,y_max,clusters,points_per_cluster,scale,offset):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.clusters = clusters
        self.points_per_cluster = points_per_cluster
        self.scale = scale
        self.offset = offset
        self.x,self.y = self.generateData()
    def generateData(self):
        x = []
        y = []
        for index in range(self.clusters):
            num_of_points = int(np.random.uniform(self.points_per_cluster[0],self.points_per_cluster[1]))
            center_x = np.random.uniform(self.x_min + self.offset[0],self.x_max - self.offset[0])
            center_y = np.random.uniform(self.y_min + self.offset[1],self.y_max - self.offset[1])
            cluster_x = np.random.normal(center_x, self.scale, num_of_points)
            cluster_y = np.random.normal(center_y, self.scale, num_of_points)
            x.extend(cluster_x)
            y.extend(cluster_y)
            print(f"Cluster {index}: {(center_x,center_y)}")
        return x,y
        