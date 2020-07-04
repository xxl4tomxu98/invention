from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import matplotlib.pyplot as plt
import scipy.stats as ss
import random
import numpy as np


def distance(x, y):
    """find the distance between points x and y in geometry coordinate"""
    return np.sqrt(np.sum(np.power(y - x, 2)))


distance(np.array([1, 1]), np.array([4, 4]))


def majority_vote(votes):
    """find the key to the majority vote from sequence votes"""
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)


def majority_vote_fast(votes):
    """ return the most common element in a seq"""
    mode, count = ss.mstats.mode(votes)
    return mode


votes = [2, 3, 5, 6, 3, 4, 5, 7, 8, 3, 2, 1]

winner = majority_vote_fast(votes)


points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [
                  2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])

p = np.array([2.5, 2])


plt.plot(points[:, 0], points[:, 1], 'ro')
plt.plot(p[0], p[1], 'bo')
plot.axis([0.5, 3.5], [0.5, 3.5])


def find_nearest_neighbor(p, points, k=5):
    """function find the k nearest neighbors to p from points"""
    distances = np.zeros(points.shape[0])
    for index in range(len(points)):
        distances[index] = distance(points[index], p)
    ind = np.argsort(distances)
    return ind[0:k]


points[find_nearest_neighbor(p, points, 2)]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbor(p, points, k)
    return majority_vote(outcomes[ind])


outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

knn_predict(p, points, outcomes, 2)


ss.norm(0, 1).rvs((5, 2))

ss.norm(1, 1).rvs((5, 2))


def generate_synth_data(n=50):
    """ create 2 sets of points from bivariant normal distribution"""
    points = np.concatenate(
        (ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)


n = 20

(points, outcomes) = generate_synth_data(n)
plt.figure()
plt.plot(points[0:n, 0], points[0:n, 1], 'ro')
plt.plot(points[n:, 0], points[n:, 1], 'bo')
plt.savefig('bivardata.pdf')


def make_prediction_grid(predictors, outcomes, limits, h, k):
    """classify each point on prediction grid"""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return(xx, yy, prediction_grid)


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

for index, season in enumerate(seasons):
    print(index, season)


def plot_prediction_grid(xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap(
        ["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(10, 10))
    plt.pcolormesh(xx, yy, prediction_grid,
                   cmap=background_colormap, alpha=0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1],
                c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.xticks(())
    plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))
    plt.savefig(filename)


(predictors, outcomes) = generate_synth_data()

k = 2
filename = 'knn_synth_5.pdf'
limits = (-3, 4, -3, 4)
h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(
    predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_grid, filename)


iris = datasets.load_iris()
iris[:5, :]
predictors = iris.data[:, 0:2]
outcomes = iris.target

plt.plot(predictors[outcomes == 0][:, 0],
         predictors[outcomes == 0][:, 1], 'ro')
plt.plot(predictors[outcomes == 1][:, 0],
         predictors[outcomes == 1][:, 1], 'go')
plt.plot(predictors[outcomes == 2][:, 0],
         predictors[outcomes == 2][:, 1], 'bo')
plt.savefig('iris.pdf')

k = 5
filename = 'iris_grid.pdf'
limits = (4, 8, 1.5, 4.5)
h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(
    predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_grid, filename)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

my_predictions = np.array(
    [knn_predict(p, predictors, outcomes, 5) for p in predictors])

print(100*np.mean(my_predictions == sk_predictions))

print(100*np.mean(my_predictions == outcomes))
print(100*np.mean(sk_predictions == outcomes))
