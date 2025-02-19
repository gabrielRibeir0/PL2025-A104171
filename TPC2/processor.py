def read_csv():
    with open("obras.csv", 'r', encoding='utf-8') as file:
        file.readline()
        data_str = file.read().strip().split(';')

    data = {}
    count = 0
    while True:
        try:
            if '\n' in data_str[count]:
                name = data_str[count].split('\n')[1]
            else:
                name = data_str[count]
            count += 1
            desc = data_str[count]
            count += 1
            year = int(data_str[count])
            count += 1
            period = data_str[count]
            count += 1
            if ", " in data_str[count]:
                temp_str = data_str[count].split(", ")
                composer = f"{temp_str[1]} {temp_str[0]}"
            else:
                composer = data_str[count]
            count += 1
            duration = tuple(int(x) for x in data_str[count].split(':'))
            count += 1
            id = data_str[count].split('\n')[0]

            data[id] = {"name": name, "desc": desc, "year": year, "period": period, "composer": composer, "duration": duration}
        except Exception:
            break
    
    return data

def sorted_composers(data):
    composers = set(piece['composer'] for piece in data.values())
    return sorted(composers)

def period_distribution(data):
    periods = {}
    for piece in data.values():
        period = piece['period']
        if period in periods:
            periods[period] += 1
        else:
            periods[period] = 1
    
    return periods

def sorted_pieces_by_period(data):
    result = {}
    
    for piece in data.values():
        period = piece['period']
        name = piece['name']
        
        if period not in result:
            result[period] = []
        
        result[period].append(name)
    
    for period in result:
        result[period] = sorted(result[period])
    
    return result

def main():
    data = read_csv()

    composers = sorted_composers(data)
    print("=== Compositores ordenados alfabeticamente ===")
    for composer in composers:
        print(composer)
    print("\n")
    
    distribution = period_distribution(data)
    print("=== Distribuição das obras por período ===")
    for period, count in distribution.items():
        print(f"{period}: {count} obras")
    print("\n")
    
    pieces_by_period = sorted_pieces_by_period(data)
    print("=== Lista alfabética das obras por período ===")
    for period, titles in pieces_by_period.items():
        print(f"\n{period}:")
        for title in titles:
            print(f"  - {title}")

if __name__ == "__main__":
    main()