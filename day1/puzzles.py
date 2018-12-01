filename = "input.txt"

with open(filename) as input_file:
	data = [number.strip() for number in input_file]

def calibrate_sequence(sequence):
	number = 0
	frequencies = set()
	frequencies.add(number)
	duplicated = False
	while not duplicated:
		for seq in sequence:
			number = number + int(seq)
			if number in frequencies:
				duplicated = number
				return duplicated
			else:
				frequencies.add(number)
	return


if __name__ == '__main__':
	print(calibrate_sequence(data))
