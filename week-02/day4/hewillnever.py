# Things are a little bit messed up
# Your job is to decode the notSoCrypticMessage by using the hashmap as a look up table
# Assemble the fragments into the out variable

out = {7: "run around and desert you", 50: "tell a lie and hurt you", 49: "make you cry,", 2: "let you down", 12: "give you up,", 1: "Never gonna", 11: "\n", 3: "say goodbye"}

print(out[11], out[1], out[12], out[1], out[2], out[11], out[1], out[7], out[11], out[49], out[1], out[3], out[11], out[1], out[50], out[11])

out = (hashmap[5] = notSoCrypticMessage[0]);
notSoCrypticMessage = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]

hashmap = [
    {7: "run around and desert you"},
    {50: "tell a lie and hurt you"},
    {49: "make you cry,"},
    {2: "let you down"},
    {12: "give you up,"},
    {1: "Never gonna"},
    {11: "\n"},
    {3: "say goodbye"}
]

print(out)
