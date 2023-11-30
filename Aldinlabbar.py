from LivsmedelsDB4 import DB as DB

ing = str(input("ingrediends")).lower()
alling = []
for i in DB:
    if ing in i[0].lower():
        alling.append(i)

for j in alling:
    print(j[0])
val = int(input("Välj rätt nedan med index"))
print(alling[val])