import csv
import json
import argparse
import os

def csv_to_json(csv_file):
    """Converte um arquivo CSV em JSON, salvando com o mesmo nome."""
    data = []

    # Lê o arquivo CSV
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Gera o nome do JSON automaticamente
    json_file = os.path.splitext(csv_file)[0] + ".json"

    # Salva como JSON
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    print(f"✅ Conversão concluída! Arquivo salvo como {json_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converter CSV para JSON.")
    parser.add_argument("csv_file", help="Caminho do arquivo CSV de entrada")

    args = parser.parse_args()
    csv_to_json(args.csv_file)
