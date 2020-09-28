import asyncio
from datetime import datetime, timedelta
import hangups
from actual_send_message import send_message
from common import run_example
import covid_data
import weather_data
import random
import name_manager


TARGET_CONVO_ID = ["UgySatjjT_zwYMjvfcl4AaABAQ", # Smol one with ash
                   "UgxDGV0wLrqmNtJl6AF4AaABAQ", # Strange Children dwell in this place
                   "UgykUAGlU7YTgn7SqDZ4AaABAQ", # Pranking
                   "Ugyh42XnZTkgwWOdSXx4AaABAQ", # spicy food
                   "Ugxbq8_Rirg4LzaJIwt4AaABAQ", # Among us thing with 8th graders
                   ]

bullied_people = [
    "1", #nobody
]

AUTHORIZED_ADMINS = [
    "107091478556168807541", #Joel
]

def getName(user_id_obj):
    name = name_manager.getName(user_id_obj.chat_id)
    if name is False:
        return user_list.get_user(user_id_obj).full_name
    else:
        return name

async def timeout(conv_id_str, length):
    send_message(conv_id_str, f'Started timeout for {int(length/60)} minutes.')
    for i in range(len(TARGET_CONVO_ID)):
        if TARGET_CONVO_ID[i] == conv_id_str:
            index = i
    TARGET_CONVO_ID[index] = ""
    await asyncio.sleep(length)
    TARGET_CONVO_ID[index] = conv_id_str
    send_message(conv_id_str, 'Timeout ended. Be good boys and girls now!')

async def receive_messages(client, args):
    print('loading conversation list...')
    global user_list
    global conv_list
    user_list, conv_list = (
        await hangups.build_user_conversation_list(client)
    )
    conv_list.on_event.add_observer(on_event)

    print('waiting for chat messages...')
    while True:
        await asyncio.sleep(1)


async def on_event(conv_event):
    if isinstance(conv_event, hangups.ChatMessageEvent):
        if conv_event.conversation_id in TARGET_CONVO_ID:
            print(user_list.get_user(conv_event.user_id).full_name+':', conv_event.text)
            return_convo_id = conv_event.conversation_id
            cmdtxt = conv_event.text.lower().strip()
            

            if conv_event.user_id.chat_id in bullied_people:
                target = "joel"
                responses = [
                    f"fuck off {target}",
                    f"REEEEEEEEE",
                    f"look its stupid head {target}",
                    f"ok {target} poopy head",
                    f"bullying {target} is my passion, fuck them",
                    f'hi {target}... jk fuck you',
                    f"still hate you {target}"
                ]
                send_message(return_convo_id, random.choice(responses))
                return 0
            
            if cmdtxt.startswith("!hi"):

                send_message(return_convo_id, f'Hi there {getName(conv_event.user_id)}.')

            elif cmdtxt == "!randomperson":
                people = conv_list.get(return_convo_id).users
                responses = [
                "Lets go with ",
                "Im thinkin ",
                "uhh idk ",
                "",
                "Imma choose ",
                "Just go with ",
                ]
                person = random.choice(people)
                received_name = getName(person.id_)
                hangouts_name = person.full_name
                if received_name == hangouts_name:
                    name = received_name
                else:
                    name = f"{received_name} ({hangouts_name})"
                send_message(return_convo_id, random.choice(responses)+name)

            elif cmdtxt == "!help":

                send_message(return_convo_id, "Some commands you can try are: !bruh, !callme, !repeat, !hi, !time, !mdcovid, !kmk, !randomperson, !uscovid, !weather, !lovecalc, !help.")

            elif cmdtxt.startswith("!repeat "):
                txt = cmdtxt.replace("!repeat ", "")
                send_message(return_convo_id, f'You said: {txt}')

            elif cmdtxt == "language":
                if conv_event.user_id.chat_id == "109838171166874380185":
                    send_message(return_convo_id, "Hello you fucking bot. My fucking name is fucking ShitPissCum1312 and I am a fucking bot fucking made by some fucking mother-fuckung-fucker who was really fucking annoyed by your fucking comments with a fucking purpose of fucking telling you to fucking shut the fuck up. What the fucking fuck are you even fucking trying to fucking achieve by fucking doing this fucking shit fucking over and over? No fucking one is fucking going to fucking stop fucking saying fucking fuck just because you fucking told them so. Fuck you all and have a nice fucking day. Fuck.")
                else:
                    send_message(return_convo_id, "Oh shit, your dumb bitch ass saying that makes me want to stop fucking cursing!!!")
            elif cmdtxt == "!time":

                the_time = conv_event.timestamp - timedelta(hours=4)
                send_message(return_convo_id, f'The time is {the_time.hour}:{the_time.minute}:{the_time.second}.')
            
            elif cmdtxt == "!mdcovid":

                send_message(return_convo_id, f'There have been {"{:,}".format(covid_data.md_covid())} reported cases in Maryland.')
            
            elif cmdtxt == "!uscovid":

                send_message(return_convo_id, f'There have been {covid_data.us_covid()} reported cases in the US.')
        
            elif cmdtxt == "!weather":

                send_message(return_convo_id, f'It is currently {weather_data.ellicott_city()}° in Ellicott City.')
        
            elif cmdtxt == "!bruh":

                    send_message(return_convo_id, 'bruh')

            elif cmdtxt.startswith("!lovecalc"):
                people = cmdtxt.replace('!lovecalc ', '')
                if people.count(' ') == 1:
                    random.seed(people)
                    amt = random.randint(1, 1400)/10
                    if amt > 99.9:
                        amt= round(amt-40, 1)
                    send_message(return_convo_id, f"{people.replace(' ', '+')}: {amt}%")
                else:
                    send_message(return_convo_id, f'Correct format is !lovecalc <person1> <person2>')

            elif cmdtxt.startswith('!kmk'):
                if cmdtxt.count(' ')==3:
                    people = cmdtxt.replace('!kmk ', ' ').split()
                    random.shuffle(people)
                    print(people)
                    send_message(return_convo_id, f"Kill {people[0]}, Kiss {people[1]}, Marry {people[2]}.")
                else:
                    send_message(return_convo_id, "Correct format is !kmk <person1> <person2> <person3>")

            elif cmdtxt.startswith('!callme'):
                if cmdtxt.count(' ')>=1 and len(cmdtxt)>8 and len(cmdtxt)<=24:
                    name = conv_event.text[8:]
                    user_id = conv_event.user_id.chat_id
                    send_message(return_convo_id, f"Set your name to {name_manager.setName(user_id, name)}" )
                elif len(cmdtxt)>24:
                    send_message(return_convo_id, f"That name is too long. Names are limited to 16 characters.")
                else:
                    send_message(return_convo_id, f"Correct Format: !callme <name>.")

            elif cmdtxt.startswith('!timeout'):
                if conv_event.user_id.chat_id in AUTHORIZED_ADMINS:
                    try:
                        amt = int(cmdtxt.replace('!timeout ', ''))
                    except ValueError:
                        send_message(return_convo_id, "Correct Format: !timeout <minutes>")
                        return 0
                    loop = asyncio.get_event_loop()
                    loop.create_task(timeout(return_convo_id, amt*60))
                else:
                    send_message(return_convo_id, "You are not authorized to use this command.")


if __name__ == '__main__':
    run_example(receive_messages)