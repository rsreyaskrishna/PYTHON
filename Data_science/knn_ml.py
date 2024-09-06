
from sklearn.neighbors import KNeighborsClassifier
x1=[7,7,3,1]
y1=[7,4,4,4]
target=['BAD','BAD','GOOD','GOOD']
print(x1)
print(y1)
#zip-to combine x and y
feature=list(zip(x1,y1))
print(feature)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(feature,target)

print(model.predict([[3,7]]))