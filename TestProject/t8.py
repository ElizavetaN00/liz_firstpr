def display_field(size = 5):
    field = [[" " for i in range(size)] for i in range(size)]
    for row in field:
        print(" | ".join(row))
        print("-" * 15)

def winner(field, user):
    for row in field:


display_field()