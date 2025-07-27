camelcase = input("camelCase: ").strip()
index = 0
snake_case = []
for i in range(len(camelcase)):
    if camelcase[index].isupper() and index > 0:
        add_dash = "_" + camelcase[index]
        snake_case +=  [add_dash]
    else:
        snake_case +=  [camelcase[index]]
    index += 1
output = "".join(snake_case).lower()
print(f"snake_case: {output}")
