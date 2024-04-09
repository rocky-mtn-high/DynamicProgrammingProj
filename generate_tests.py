import random

def generate_random_array():
    length = random.randint(1, 2000)
    array = [random.randint(1, 1000) for _ in range(length)]
    return array

def save_array_to_file(array, filename):
    with open(filename, 'w') as f:
        f.write(str(len(array)) + '\n')
        f.write(' '.join(map(str, array)))

def gen_tests():
    for i in range(50):  # Generate 10 arrays
        array = generate_random_array()
        filename = f"./arrays/array_{i + 1}.txt"  # Naming the files array_1.txt, array_2.txt, ...
        save_array_to_file(array, filename)
        print(f"Array {i + 1} saved to {filename}")