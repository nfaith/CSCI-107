# -----------------------------------------+
# Faith Nelson                             |
# CSCI 107, Assignment 4                   |
# Last Updated: ??, 2018                   |
# -----------------------------------------|
# Use loops to minimize repeated words and |
# phrases to these lyrics of "The Fox".    |
# -----------------------------------------+

call = "ding " * 3 + "dingeringeding!"
chorus = "WHAT DOES THE FOX SAY?"
ow = " OW" * 3
pa = " pa" * 5


print("Dog goes woof, cat goes meow.")
print("Bird goes tweet, and mouse goes squeak.")
print("Cow goes moo. Frog goes croak, and the elephant goes toot.")
print("Ducks say quack and fish go blub, and the seal goes"+ ow + ".")
print("But there's one sound that no one knows...")
print(chorus)

print()

print("Ring " + call)
for i in range(2):
    print("Gering " + call)
print(chorus)
for lyrics in range(3):
    print("Wa" + pa + " pow!")
