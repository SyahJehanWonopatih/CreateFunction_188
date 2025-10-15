def konversi_temperature(value, unit):
    if unit.upper() == 'C':
        return(value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("suhu tidak valid gunakan 'C' or 'F'")
    print(konversi_suhu(200, 'C'))
    print(konversi_suhu(38, 'F'))
    
