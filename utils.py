def load_data(file):
    try:
        f = open(file,'r')
    except FileNotFoundError as err:
        print(f"Maria! There is an Error: {err}")
    else:    
        data = [int(line) for line in f]
        f.close()
    return data

