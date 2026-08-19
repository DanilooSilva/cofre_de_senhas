from time import sleep
from src import Index

try:
    Index().inicio()
except FileNotFoundError as error:
    print(error)
    sleep(10)


