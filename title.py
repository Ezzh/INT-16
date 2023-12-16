def title(input: str) -> str:
    input = list(input)
    input[0] = input[0].upper()
    for i in range(1, len(input)-1):
        if input[i] == " ":
            input[i+1] = input[i+1].upper()
    return "".join(input)

print(title("тесТОвое задание для   pt".title()))