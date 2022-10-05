#%%

i = 0

while i <= 4:
    print("Hello everybody")
    i = i + 1
# %%

beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"
]

print(type(beatles))

print(beatles[2])

numbers = [0, 3, -11, 99]

mixed_values = [1, True, 0.4, "abcd"]

# %%

## Practice - Exercise 2 

beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"
]

def print_list(list):
    n = 0

    while n <= len(list) -1:
        print(beatles[n])
        n = n + 1 

print_list(beatles)

# %%

# With lists you  can use + and *

ramones = [
    "Johnnie",
    "Joey",
    "Markee",
    "Dee-dee"
]

phillippes = ["Phillippe", "Pepe"]

print(ramones + phillippes)
print(phillippes * 4)

# %%

# Change elements of lists

beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"
]

beatles[3] = "Pepe"
print(beatles)

# %%

# Add elements to the end of the  list

coding_club = []
coding_club.append("Karmele")
coding_club.append("Phillippe")

print(coding_club)

# %%

# For loops are an easier way of iterating through a list

beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"
]

def print_list(list):
    for element in list:
        print(element)

print_list(beatles)

# %%
