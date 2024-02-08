class upper:
    def __init__(self):
        self.a=""
    def get_string(self):
        self.a=input()
    def print_string(self):
        print(self.a.upper())

a = upper()
a.get_string()
a.print_string()