#No 2
import math

# mendefinisi Lambda function untuk menghitung luas jari-jari lingkaran = π * r^2
circle_area = lambda r: math.pi * r**2

# Get radius from user input
print(" Konversi Lingkaran ")
r = float(input("Masukkan Jari-Jari Lingkaran: "))

# menghitung luas
area = circle_area(r)

print(f"Luas Lingkaran {r} adalah: {area}")