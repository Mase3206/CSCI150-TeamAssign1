import mathshiet

def tester(suite='limited', num1=87, num2=14):
	outputs = []

	if suite == 'full':
		output1 = [mathshiet.add(num1, num2), mathshiet.subtract(num1, num2), mathshiet.multiply(num1, num2), mathshiet.divide(num1, num2)]
		output2 = [mathshiet.add(num1 * 2, num2 * 3), mathshiet.subtract(num1 * 2, num2 * 3), mathshiet.multiply(num1 * 2, num2 * 3), mathshiet.divide(num1 * 2, num2 * 3)]
		output3 = [mathshiet.add(num1 * 7, num2 * 17), mathshiet.subtract(num1 * 7, num2 * 17), mathshiet.multiply(num1 * 7, num2 * 17), mathshiet.divide(num1 * 7, num2 * 17)]
		
		return output1, output2, output3

	if suite == 'limited':
		return [mathshiet.add(num1, num2), mathshiet.subtract(num1, num2), mathshiet.multiply(num1, num2), mathshiet.divide(num1, num2)]