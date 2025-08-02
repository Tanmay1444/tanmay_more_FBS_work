#### calculate the cost of painting the following building's walls (both interior and exterior).

area = int(input("Enter the area of one side wall(in sq meters):"))
cost1 = int(input("Enter the cost per sq meter for interior wall:"))
cost2 = int(input("Enter the cost per sq meter for exterior wall:"))


total_walls = 8

total_area = total_walls * area

interior_total_cost = total_area * cost1
exterior_total_cost = total_area * cost2

print(f'cost for interior painting is:{interior_total_cost}rs, cost for exterior painting is:{exterior_total_cost}rs.')