def write_html(data, output_file) -> None:
    try:
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Raport</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class="piramid">
                <h1>Wynik raportu dla - "Odwrócona Piramida":</h1>

        """

        for item in data:
            html_content += f"<div>{item}</div>\n"

        html_content += """

            </div>
            <div class="footer">
                Piotr Dusiński
            </div>
        </body>
        </html>
        """
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
            print("Raport zapisano pomyślnie w /out/index.html")
    except Exception as e:
        print(f"Wystąpił bład: {e}")
