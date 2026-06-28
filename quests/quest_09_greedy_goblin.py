# Author: Gatete Irene Hodali
# Quest 9: The Greedy Goblin
# Concept: The Modulo Operator (%) - gives the remainder of a division

gold_pieces = 27
friends = 4

each_friend_gets = gold_pieces // friends  # integer division: how many each friend gets
goblin_keeps = gold_pieces % friends       # remainder: what the goblin keeps

print(f"The goblin has {gold_pieces} gold pieces to share among {friends} friends.")
print(f"Each friend gets: {each_friend_gets} gold pieces.")
print(f"The goblin keeps: {goblin_keeps} gold piece(s).")
