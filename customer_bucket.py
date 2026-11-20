invoices = [("C01", 12, 40000), ("C02", 75, 15000), ("C01", 45, 22000), ("C03", 5, 8000),
            ("C02", 120, 30000), ("C01", 20, 10000), ("C03", 95, 12000), ("C02", 61, 5000)]

buckets = ["0-30", "31-60", "61-90", "90+"]

def bucket_of(dpd):
    if dpd<=30:
        return "0-30"
    if dpd <= 60:
        return "31-60"
    if dpd <= 90:
        return "61-90"
    else:
        return "90+"

flat = {}
for cust, dpd, amt in invoices:
    key =(cust,bucket_of(dpd))
    if key not in flat:
        flat[key] = [0,0]
    flat[key][0] += 1
    flat[key][1] += amt

for key in sorted(flat):
    print(key,flat[key])

nested = {}

for (cust, b), (cnt, amt) in flat.items():
    if cust not in nested:
        nested[cust] = {bk: 0 for bk in buckets}
    nested[cust][b] += amt

print()
print(f"{'cust':6}" + "".join(f"{b:>8}" for b in buckets) + f"{'total':>8}")
for cust in sorted(nested):
    row = nested[cust]
    print(f"{cust:<6}" + "".join(f"{row[b]:>8}" for b in buckets) + f"{sum(row.values()):>8}")