from models.BanAccount import BanAccount
my_account = BanAccount(1000)
your_account = BanAccount(500)
our_ace = my_account + your_account
our_ace -= your_account
print(our_ace)