import cowsay
import getpass
user=getpass.getuser()
cowsay.turkey(f"Salut {user} ! Je tourne dans Docker sans polluer ton Windows.")