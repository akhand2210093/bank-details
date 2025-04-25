import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank.settings')
django.setup()

from branch.models import Bank

def load_banks():
    # Open the SQL file with UTF-8 encoding
    with open('indian_banks.sql', 'r', encoding='utf-8') as sql_file:
        banks_data = []
        for line in sql_file:
            # Skip lines until we reach the COPY command
            if line.startswith("COPY banks"):
                break

        for line in sql_file:
            # Skip empty lines and comments
            if not line.strip() or line.startswith('--'):
                continue

            # Extract data fields
            try:
                bank_name, bank_id = line.strip().split('\t')
                banks_data.append(Bank(id=int(bank_id), name=bank_name))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    # Bulk create Bank records
    Bank.objects.bulk_create(banks_data, ignore_conflicts=True)
    print("Banks data loaded successfully!")

if __name__ == "__main__":
    load_banks()