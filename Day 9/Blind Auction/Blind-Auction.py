from replit import clear
from art import logo

auction_dictionary = {}
bidding_over = False

def highest_bidder(auction_dictionary) :
  highest_bidder = ""
  max_bid = 0
  for name in auction_dictionary :
    if auction_dictionary[name] > max_bid :
      max_bid = auction_dictionary[name]
      highest_bidder = name
  clear()
  print(f"The winner is {highest_bidder} with ${max_bid}")

print(logo)
print("Welcome to the secret auction program")
while not bidding_over :
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  auction_dictionary[name] = price
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if choice == "no" :
    bidding_over = True
    highest_bidder(auction_dictionary)
  elif choice == "yes" :
    clear()