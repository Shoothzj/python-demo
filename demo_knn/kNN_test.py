from demo_knn import kNN
import operator

group, labels = kNN.create_data_set()
classify = kNN.classify0([0, 0], group, labels, 3)
print(classify)

# datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
# print(datingDataMat)
# print("labels is ")
# print(datingLabels)

ho_ratio = 0.10
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minVals = kNN.auto_norm(datingDataMat)
m = normMat.shape[0]
numTestVecs= int(m * ho_ratio)
errorCount = 0.0
for i in range(numTestVecs):
    classifier_result = kNN.classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
    print("the classifier came back with: %d, the real answer is: %d" , classifier_result, datingLabels[i])
    if (classifier_result != datingLabels[i]):
        errorCount += 1.0
print("the total error rate is: %f", errorCount/float(numTestVecs))