class Bank:
    def __init__(self, clients=None, deposits=None):
        self.clients = clients if clients is not None else {}
        self.deposits = deposits if deposits is not None else {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Client was registered before")
        self.clients[client_id] = name

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError("Client was not registered")
        if client_id in self.deposits:
            raise ValueError("Deposit was already opened for this client")
        self.deposits[client_id] = {
            'start_balance': start_balance,
            'years': years,
            'current_balance': start_balance
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("No deposit found for this client")
        deposit = self.deposits[client_id]
        start_balance = deposit['start_balance']
        years = deposit['years']
        monthly_rate = 0.10 / 12
        months = years * 12
        current_balance = start_balance
        for i in range(months):
            current_balance *= (1 + monthly_rate)
        final_balance = current_balance
        deposit['current_balance'] = final_balance
        return final_balance

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("There's no deposit for this client")
        del self.deposits[client_id]
