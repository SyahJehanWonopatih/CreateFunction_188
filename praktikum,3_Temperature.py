#No 1
def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return(value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit must be 'C' or 'F'")
    
print(" convert temperature " )
try: 
        input_temperature = float(input("enter the temperature value: "))
        unit = input("Enter temperature units ('C' for celcius and 'F' for Fahrenhit): ")
        convert = convert_temperature(input_temperature, unit)
        if unit.upper() == 'C':
            print(f"{input_temperature}C = {convert: 2f} F")
        elif unit.upper() == 'F':
            print(f"{input_temperature} F = {convert:.2f} C")
        else:
            print("invalid option.")
except ValueError as e:
        print("error", e)

