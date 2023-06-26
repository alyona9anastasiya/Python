# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# Optional: Make a function that can calculate hats with any amount of rounds and cats.

def cats_in_hat(cats, round):
    cats_inhat = []
    for rou in range(1, round + 1):
        for c in range(1, cats + 1):
            if c % rou == 0:
                if c in cats_inhat:
                    cats_inhat.remove(c)
                else:
                    cats_inhat.append(c)
    print(cats_inhat)

def test_cats_in_hat(number_cats, number_round):
    cats_in_hat(number_cats, number_round)

test_cats_in_hat(100, 100)
