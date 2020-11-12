# TP SVM - OBT : Machine learning - CentraleSupélec 2020
# Antoine Bourgoin et Benoit Charmettant
library("kernlab")

bTrain <- read.table("Banana_train.txt")
bTest <- read.table("Banana_test.txt")

plot(bTrain$X1, bTrain$X2, col=bTrain$Y+2)
plot(bTest$X1, bTest$X2, col=bTest$Y+2)


gaussian.fit <- ksvm(Y~., data=bTrain, C=5, sigma=5)

plot(predict(gaussian.fit, bTrain))