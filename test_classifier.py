from app.classifier import classify_amounts

raw_text = "TOTAL: 661.50 PAID: 500.00 DUE: 161.50"
numbers = [661.5, 500.0, 161.5]

print(classify_amounts(raw_text, numbers))
