def separate_tokens(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    tokens = []

    for line in lines:
        line = line.strip()
        if line:
            email, password, token = line.split(':')
            tokens.append(token)

    with open(output_file, 'w') as f:
        for token in tokens:
            f.write(token + '\n')

    print("Tokens separated and written to output.txt")

separate_tokens('token.txt', 'output.txt')
