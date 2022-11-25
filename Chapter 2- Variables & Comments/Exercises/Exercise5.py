## Exercise 5: USB Shopper :ballot_box_with_check:

# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

total_amount=50
price_per_piece = 6
pieces_buyed=total_amount/price_per_piece
rounded_pieces_buyed=round(pieces_buyed)
print("USB Sticks buyed:",rounded_pieces_buyed )
amount_mul=rounded_pieces_buyed*price_per_piece
amount_left = total_amount - amount_mul
print("Amount left:", amount_left,"pounds")