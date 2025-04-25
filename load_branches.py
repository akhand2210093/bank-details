import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank.settings')
django.setup()

from branch.models import Bank, Branch

def load_branches():
    # Open the CSV file with UTF-8 encoding
    with open('bank_branches.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        branches_data = []
        for row in reader:
            try:
                # Get the bank object using bank_id
                bank = Bank.objects.get(id=row[1])
                # Append the branch data to the list
                branches_data.append(Branch(
                    ifsc=row[0],
                    bank=bank,
                    branch=row[2],
                    address=row[3],
                    city=row[4],
                    district=row[5],
                    state=row[6]
                ))
            except Bank.DoesNotExist:
                print(f"Bank with ID {row[1]} does not exist. Skipping line: {row}")
            except Exception as e:
                print(f"Error processing line {row}: {e}")

        # Bulk create Branch records
        Branch.objects.bulk_create(branches_data, ignore_conflicts=True)
        print("Branches data loaded successfully!")

if __name__ == "__main__":
    load_branches()