### 14 ###
# str indexing - [start:end:step]

credit_card = "9876-5432-1098-7654"

num = 4
start = 10
end = 14
fromIdx = 15
fromEndIdx = -6
stepNum = 2
reverseIdx = -1

idx = credit_card[num]
startEnd = credit_card[start:end] # an example when 0 is at the start position is: [:4]
untilTheEnd = credit_card[fromIdx:]
fromEnd = credit_card[fromEndIdx]
step = credit_card[::stepNum] # from start to the end
reverse = credit_card[::reverseIdx]

print(f"Credit card: {credit_card}")
print(f"# Index[{num}]: {idx}")
print(f"# Start-End[{start}:{end}]: {startEnd}")
print(f"# Until the End[{fromIdx}:]: {untilTheEnd}")
print(f"# From End[{reverseIdx}]: {fromEnd}")
print(f"# Step[::{stepNum}]: {step}")
print(f"# Reverse[::{reverseIdx}]: {reverse}")