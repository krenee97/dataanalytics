import statistics 

def analyze_sales(analyst, region, sales):
 mean = statistics.mean(sales)
 median = statistics.median(sales)
 mode = statistics.mode(sales)
 stdev = statistics.stdev(sales)
 total = sum(sales)
 high = max(sales)
 low = min(sales)
 return mean, median, mode, stdev, high, low

analyst = input("analyst name:Kendra")
region = input("region: East")

print("Enter daily sales for 7 days:")
sales = [float(input(f"day{1+1}:$")) for i in range(7)]

mean, median, mode = analyze_sales(analyst, region, sales)