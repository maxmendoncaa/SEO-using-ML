import numpy as np
import csv
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import pairwise_distances

def sum1forline(filename):#count rows in csv
    with open(filename) as f:
        return sum(1 for line in f)


def k_means(file_path, num_clusters):
    rs=[]
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)[1:] #skip header row
        for xc in rows:
            rs.append(xc[1:-1])     
        distances = pairwise_distances(rs, metric='cosine') # calculate cosine similarity
        kmeans = KMeans(n_clusters=num_clusters).fit(distances)
        labels = kmeans.labels_
        clusters = {}
        for i, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(i)
        return clusters

def aglo(file_path, num_clusters):
    rs=[]
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)[1:] #skip header row
        for xc in rows:
            rs.append(xc[1:-1])
        
        distances = pairwise_distances(rs, metric='euclidean') # calculate cosine similarity
        agglom = AgglomerativeClustering(n_clusters=num_clusters, affinity='precomputed', linkage='average')
        labels = agglom.fit_predict(distances)
        clusters = {}
        for i, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(i)
        return clusters


def divisive(file_path, num_clusters):
    rs=[]
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)[1:] #skip header row
        for xc in rows:
            rs.append(xc[1:-1])
        n = len(rs)
        distances = pairwise_distances(rs, metric='euclidean')  # calculate cosine similarity
        clusters = {0: list(range(n))}  # start with a single cluster containing all rows
        curr_label = 1
        while len(clusters) < num_clusters:
            cluster_to_divide = max(clusters, key=lambda k: len(clusters[k]))  # get the largest cluster to divide
            indices = clusters[cluster_to_divide]
            sub_distances = distances[np.ix_(indices, indices)]
            sub_clusters = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='single').fit_predict(sub_distances)
            left_indices = [indices[i] for i in range(len(sub_clusters)) if sub_clusters[i] == 0]
            right_indices = [indices[i] for i in range(len(sub_clusters)) if sub_clusters[i] == 1]
            del clusters[cluster_to_divide]
            clusters[curr_label] = left_indices
            clusters[curr_label+1] = right_indices
            curr_label += 2
        return clusters

# Example usage
ctr=sum1forline("trimmed2.csv")-1 #count entries

dclusters =divisive("trimmed2.csv", int(0.7*ctr))
#print("Divisive:", dclusters)

aclusters = aglo("trimmed2.csv", int(0.7*ctr))
#print("Agglomerative:", aclusters)

kclusters = k_means("trimmed2.csv", int(0.7*ctr))
# print("K-Means:", kclusters)




rs=[]
with open("trimmed2.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    rows = list(reader)[1:] #skip header row
    for xc in rows:
        rs.append(xc[1:-1])

def sort_clusters_by_values(clusters, rs):
    cluster_values = {}
    for label, indices in clusters.items():
        values = [float(rs[i][-1]) for i in indices]
        cluster_values[label] = np.mean(values)
    sorted_clusters = sorted(cluster_values.items(), key=lambda x: x[1])
    sorted_labels = [label for label, _ in sorted_clusters]
    sorted_clusters_dict = {i: clusters[label] for i, label in enumerate(sorted_labels)}
    return sorted_clusters_dict


# Example usage
sorted_dclusters = sort_clusters_by_values(dclusters, rs)   
print("Divisive:", sorted_dclusters)

sorted_aclusters = sort_clusters_by_values(aclusters, rs)
print("Agglomerative:", sorted_aclusters)

sorted_kclusters = sort_clusters_by_values(kclusters, rs)
print("K-Means:", sorted_kclusters)


# URL,FirstContentfulPaint,FirstInteractive,LargestContentfulPaint,SpeedIndex,CumulativeLayoutShift
# https://www.gec.ac.in/,7.0,8.4,19.2,20.1,0.007
# https://pccegoa.edu.in/,5.6,38.8,28.5,14.3,0.321
# https://maxunivfadsadadersity.edu.gg/,0,0,0,0,0
# https://dbcegoa.ac.in/,4.1,24.9,14.8,19.4,0.62
# http://www.xavierscollege-goa.com,200.1,400.5,200.1,400.5,100.3
# https://aitdgoa.edu.in/,4.8,31.6,22.2,21.1,0.018
# https://paruluniversity.ac.in/,3.2,72.0,32.1,35.5,0
# https://maxuniversity.edu.gg/,0,0,0,0,0
# http://www.obfhadbihbadca.com,150.1,400.5,200.1,400.5,100.3
# https://maxuniversity.edu.gg/,0,0,0,-90,-60


# URL,FirstContentfulPaint,FirstInteractive,LargestContentfulPaint,SpeedIndex,CumulativeLayoutShift,FisrtMeaningfulPaint,TotalBlockingTime,MaxPotentialFID
# https://pccegoa.edu.in/,0,0,0,0,0,0,0,0
# https://dbcegoa.ac.in/,20,20,20,20,20,20,20,20
# https://aitdgoa.edu.in/,80,80,80,80,80,80,80,80
# https://paruluniversity.ac.in/,40,40,40,40,40,40,40,40
# https://KEKW.in/,60,60,60,60,60,60,60,60
# https://hahalol.in/,100,100,100,100,100,100,100,100