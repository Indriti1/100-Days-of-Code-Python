# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Turn both names lowercase
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

# Set count of true to 0
true_count = 0

# Find count for each letter of true : t, r, u, e
t_count = name1_lowercase.count("t") + name2_lowercase.count("t")
r_count = name1_lowercase.count("r") + name2_lowercase.count("r")
u_count = name1_lowercase.count("u") + name2_lowercase.count("u")
e_count = name1_lowercase.count("e") + name2_lowercase.count("e")

# Add all counts for word true together
true_count = t_count + r_count + u_count + e_count

# Set count of love to 0
love_count = 0

# Find count for each letter of love : l, o, v, e
l_count = name1_lowercase.count("l") + name2_lowercase.count("l")
o_count = name1_lowercase.count("o") + name2_lowercase.count("o")
v_count = name1_lowercase.count("v") + name2_lowercase.count("v")
e_count = name1_lowercase.count("e") + name2_lowercase.count("e")

# Add all counts for word love together
love_count = l_count + o_count + v_count + e_count

# Set score to 0
score = 0

# Concatenating word counts and evaluating score
if true_count == 0 and love_count == 0:
    score = 0
else:
    if true_count != 0:
        score = int(str(true_count) + str(love_count))
    else:
        score = int(str(love_count))

# Returning correct message based on the result
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")