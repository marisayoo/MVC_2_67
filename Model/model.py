import csv

class SuitModel:
    def __init__(self):
        self.suits = ['Suitcode', 'SuitType', 'Durability']
        self.filename = 'data.csv'

    def read_csv_file(self):
        data = []
        try:
            with open(self.filename, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        row['SuitCode'] = int(row['SuitCode'])
                        row['Durability'] = int(row['Durability'])
                    except (KeyError, ValueError):
                        pass
                    data.append(row)
        except FileNotFoundError:
            print(f"cannot find: {self.filename}")
        except Exception as e:
            print(f"error {self.filename}: {e}")
        return data
    
    def check_suit_code(self, suit_code):
        return suit_code.isdigit() and len(suit_code) == 6 and suit_code[0] != '0'

    def get_suit_by_code(self, suit_code):
        data = self.read_csv_file()
        for suit in data:
            if suit.get('SuitCode') == int(suit_code):
                return suit
        return None

    def is_durability_ok(self, suit):
        suit_type = suit.get('SuitType', '')
        durability = suit.get('Durability', 0)
        if suit_type == 'Power Suit':
            return durability >= 70
        elif suit_type == 'Stealth Suit':
            return durability >= 50
        elif suit_type == 'Incognito Suit':
            last_digit = durability % 10
            return last_digit not in (3, 7)
        else:
            return False

    def repair_suit(self, suit):
        current = suit.get('Durability', 0)
        new_durability = current + 25
        if new_durability > 100:
            new_durability = 100
        suit['Durability'] = new_durability
        return suit