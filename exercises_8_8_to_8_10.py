# this is me practicing Python with exercises from the book "Python Crash Course" by Eric Matthes.
# Exercises 8-8 to 8-10 on the topic of "Lists and Functions".

# -----------------------------------------------------------------------------
# listed bullets of the logic to implement:
# 1a. Make a list containing a series of short text messages.
# 1b. Pass the list to a function called show_messages(), which prints each text message.
# 2a. Write a function called send_messages() that prints each text message and moves each message
# to a new list called sent_messages as it’s printed.
# 3a. After calling the function, print both of your lists to make sure the messages were moved correctly.
# 4a. Call the function send_messages() with a copy of the list of messages.
# 4b. print both of your lists to show that the original list has retained its messages.

# -----------------------------------------------------------------------------
from icecream import ic

# -----------------------------------------------------------------------------

# ic.disable()

# 1a.
li_short_messages = [
    "This is a short message",
    "This is a 2nd short message",
    "This is a third short message",
]


def show_messages(list):  # 1b.
    for message in list:
        print(message)


show_messages(li_short_messages)  # 1b.

li_sent_messages = []


def send_messages(list):  # 2a. ...
    while list:
        for _ in list:
            # ...to a new list called sent_messages as it’s printed.
            message_out = list.pop()
            print(message_out)
            li_sent_messages.append(message_out)
    return li_sent_messages


# send_messages(li_short_messages)  # 3a. ...
# 3a. ...print both of your lists to make sure the messages were moved correctly.
# ic(li_short_messages, li_sent_messages)

send_messages(li_short_messages[:])  # 4a.
ic(li_short_messages, li_sent_messages)  # 4b.
