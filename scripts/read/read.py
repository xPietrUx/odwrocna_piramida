def read_file(file_path) -> list:
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            data = []
            for line in lines:
                data.append(line.strip())
            return data
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
