import ngtpy
import random

dim = 10
objects = []
for i in range(0, 100) :
    vector = random.sample(range(100), dim)
    objects.append(vector)

query = objects[0]

ngtpy.create(b"tmp", dim)
index = ngtpy.Index(b"tmp")
index.batch_insert(objects)
index.save()

result = index.search(query, 3)

for i, o in enumerate(result) :
    print(str(i) + ": " + str(o[0]) + ", " + str(o[1]))
    object = index.get_object(o[0])
    print(object)
