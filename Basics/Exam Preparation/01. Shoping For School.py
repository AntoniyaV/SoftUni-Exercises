pencils_num = int(input())
markers_num = int(input())
drawing_papers_num = int(input())
notebooks_num = int(input())

total_price = pencils_num * 4.75 + markers_num * 1.80 + drawing_papers_num * 6.50 + notebooks_num * 2.50
discount = total_price * 0.05

total_price -= discount

print(f"Your total is {total_price:.2f}lv")