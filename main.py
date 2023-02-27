from caesar import Caesar
from message import Message


def main():
     message = input('Enter your message here: ')
     shift = int(input('Enter what shift to use in the Caesar cipher: '))

     caesar = Caesar(shift)

     encrypted = caesar.encrypt(message)

     source = input('Who is the message from?: ')
     dest = input('Who is the reciever?: ')
     new_message = Message(source, dest, encrypted)

     print(f'{new_message}')

     decrypted_message = caesar.decrypt(new_message.data)

     print(f'{decrypted_message}')



if __name__ == '__main__':

    main()
