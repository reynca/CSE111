import math
m_items = int(input("\nHow many manufactured items are there? "))
box_items = int(input("What is the number of items that the you will pack per box? "))
answer = math.ceil(m_items / box_items)

print(f"\nThere will be {answer} manufactured items per box.\n")