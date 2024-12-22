import numpy as np
class KMeans:
    def __init__(self,num_clusters):
        self.num_clusters = num_clusters
    def fit(self,data,iterations):
        #randomly initialize the clusters
        self.clusters = [(np.random.uniform(data.x_min,data.x_max),np.random.uniform(data.y_min,data.y_max)) for _ in range(self.num_clusters)]
        for _ in range(iterations):
            #create a list to store assignments 
            self.cluster_list = [[] for _ in range(self.num_clusters)]
            #assign each point to a cluster
            for (x,y) in zip(data.x,data.y):
                distance = float('inf')
                index = -1
                for i in range(self.num_clusters):
                    distance_to_cluster_center = (x - self.clusters[i][0])**2 + (y - self.clusters[i][1])**2
                    if distance_to_cluster_center < distance:
                        distance = distance_to_cluster_center
                        index = i
                if index > -1:
                    self.cluster_list[index].append((x,y))
            #move clusters based on the points
            new_clusters = []
            for j in range(self.num_clusters):
                if len(self.cluster_list[j]) > 0:
                    list_x,list_y = zip(*self.cluster_list[j])
                    center_x = sum(list_x) / len(list_x)
                    center_y = sum(list_y) / len(list_y)
                    new_clusters.append((center_x,center_y))
                else:
                    new_clusters.append((np.random.uniform(data.x_min,data.x_max),np.random.uniform(data.x_min,data.x_max)))
            self.clusters = new_clusters
        return self.clusters, self.cluster_list
    def initalize(self,data):
        self.clusters = [(np.random.uniform(data.x_min,data.x_max),np.random.uniform(data.y_min,data.y_max)) for _ in range(self.num_clusters)]
        #create a list to store assignments 
        self.cluster_list = [[] for _ in range(self.num_clusters)]
        #assign each point to a cluster
        for (x,y) in zip(data.x,data.y):
            distance = float('inf')
            index = -1
            for i in range(self.num_clusters):
                distance_to_cluster_center = (x - self.clusters[i][0])**2 + (y - self.clusters[i][1])**2
                if distance_to_cluster_center < distance:
                    distance = distance_to_cluster_center
                    index = i
            if index > -1:
                self.cluster_list[index].append((x,y))
        return self.clusters,self.cluster_list
    def single_iteration_fit(self,data):
        #create a list to store assignments 
        self.cluster_list = [[] for _ in range(self.num_clusters)]
        #assign each point to a cluster
        for (x,y) in zip(data.x,data.y):
            distance = float('inf')
            index = -1
            for i in range(self.num_clusters):
                distance_to_cluster_center = (x - self.clusters[i][0])**2 + (y - self.clusters[i][1])**2
                if distance_to_cluster_center < distance:
                    distance = distance_to_cluster_center
                    index = i
            if index > -1:
                self.cluster_list[index].append((x,y))
        #move clusters based on the points
        new_clusters = []
        for j in range(self.num_clusters):
            if len(self.cluster_list[j]) > 0:
                list_x,list_y = zip(*self.cluster_list[j])
                center_x = sum(list_x) / len(list_x)
                center_y = sum(list_y) / len(list_y)
                new_clusters.append((center_x,center_y))
            else:
                new_clusters.append((np.random.uniform(data.x_min,data.x_max),np.random.uniform(data.y_min,data.y_max)))
        self.clusters = new_clusters
        return self.clusters, self.cluster_list

            



