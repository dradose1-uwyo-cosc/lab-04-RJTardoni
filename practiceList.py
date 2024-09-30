Items=["milk","bread","banannas","spinach","cheese"]
Price=[2.30,1.60,1.19,1.37,2.00]

for i in range(len(Items)):
    print(f"I bought {Items[i]} for ${Price[i]}")

total=0
for t in Price:
    total = total + t
print(f"I spent ${total} at walmart")

cheapest= Price.index(min(Price))
expensive= Price.index(max(Price))
print(f"The cheapest item was {Items[cheapest]}")
print(f"The most expensive item was {Items[expensive]}")