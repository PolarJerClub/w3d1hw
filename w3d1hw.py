# Question 1

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtlist = (list(filter(lambda x: x.strip() != "", places)))

print(filtlist)

# Question 2

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author1 = []

for name in author:
    author1.append(name.title())

final = sorted(author1, key=lambda x: x.split()[-1])

print(final)

# # Question 3

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

c_to_f = list(map(lambda x: (x[0], (x[1] * 9/5) + 32), places))

print(c_to_f)

# # Question 4

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def genre(x):
    for i in x:
        yield i

counter = 0

while True:
    if counter == 0:
        gen = genre(genres)
    if counter > 0:
        try:
            print(next(gen))
        except:
            print("There are no more genres")
            break
    counter += 1