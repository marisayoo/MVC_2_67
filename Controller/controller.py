from Model.model import SuitModel

class SuitController:
    def __init__(self, main_window):
        self.model = SuitModel()
        self.main_window = main_window
        self.data = self.model.read_csv_file()

    def code_submitted(self, suit_code):
        if not self.model.check_suit_code(suit_code):
            self.main_window.show_error("Invalid suit code! Must be 6 digits and not start with 0.")
            return

        suit = self.get_suit_by_code(suit_code)
        if suit is None:
            self.main_window.show_error("Suit code not found in the database.")
            return

        self.main_window.show_suit_view(suit)

    def get_suit_by_code(self, suit_code):
        for suit in self.data:
            if suit.get('SuitCode') == int(suit_code):
                return suit
        return None

    def repair_suit(self, suit):
        updated_suit = self.model.repair_suit(suit)
        for i, s in enumerate(self.data):
            if s.get('SuitCode') == updated_suit.get('SuitCode'):
                self.data[i] = updated_suit
                break
        return updated_suit