#No 1
def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return(value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit must be 'C' or 'F'")
    
print("======= KONVERSI SUHU =======")
try:
    input_suhu = float(input("Masukkan nilai suhu: "))
    unit = input("Masukkan satuan suhu ('C' untuk Celsius atau 'F' untuk Fahrenheit): ")
    konversi = convert_temperature(input_suhu, unit)
    if unit.upper() == 'C':
        print(f"{input_suhu}°C = {konversi:.2f}°F")
    elif unit.upper() == 'F':
        print(f"{input_suhu}°F = {konversi:.2f}°C")
    else:
        print("Satuan tidak dikenal.")
except ValueError as e:
    print("Terjadi kesalahan:", e)



