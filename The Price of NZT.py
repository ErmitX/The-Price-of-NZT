import time
import random

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.008)
    print()

def pause():
    input("\nPress ENTER to continue...")

print("=" * 65)
print("                     THE PRICE OF NZT")
print("=" * 65)
print()

health = 100
money = 1000000
confidence = 95
days = 1

type_text("Eddie has everything.")
type_text("Money.")
type_text("Power.")
type_text("Influence.")
type_text("A new life.")
print()

type_text("But NZT has a price.")
pause()

while days <= 12 and health > 0:

    print()
    print("=" * 50)
    print("DAY", days)
    print("=" * 50)
    print()
    print("Money:      $" + f"{money:,}")
    print("Health:     ", health)
    print("Confidence: ", confidence)
    print()

    print("What will Eddie do?")
    print()
    print("1. Work")
    print("2. Party")
    print("3. Make a major investment")
    print("4. Rest")

    choice = input("\n> ")

    if choice == "1":
        type_text("Eddie works for eighteen hours.")
        type_text("His mind never slows down.")
        money += random.randint(20000, 100000)
        health -= random.randint(8, 16)
        confidence = min(100, confidence + 2)

    elif choice == "2":
        type_text("Eddie enters an exclusive party.")
        type_text("Everyone wants to know him.")
        money -= random.randint(5000, 25000)
        health -= random.randint(5, 12)
        confidence = min(100, confidence + 5)

    elif choice == "3":
        type_text("Eddie studies the market.")
        type_text("He sees a huge opportunity.")
        investment = random.randint(50000, 200000)

        if random.randint(1, 100) > 30:
            profit = investment * random.randint(2, 5)
            money += profit
            type_text("The investment explodes in value.")
            type_text("Profit: $" + f"{profit:,}")
        else:
            loss = investment // 2
            money -= loss
            type_text("The market moves against Eddie.")
            type_text("Loss: $" + f"{loss:,}")

        health -= random.randint(10, 20)

    elif choice == "4":
        type_text("Eddie stays home.")
        type_text("No business.")
        type_text("No parties.")
        type_text("No pressure.")
        health = min(100, health + 20)
        confidence -= 2

    else:
        print("Invalid choice.")
        continue

    if health <= 35:
        print()
        type_text("Eddie looks into the mirror.")
        type_text("His face looks exhausted.")
        type_text("His body is sending a message.")
        print()
        type_text("The question is no longer how much money he can make.")
        type_text("The question is how long he can keep going.")

    days += 1

if health <= 0:
    print()
    print("=" * 65)
    print("                         COLLAPSE")
    print("=" * 65)
    print()
    type_text("The money meant nothing.")
    type_text("The power meant nothing.")
    type_text("Eddie pushed himself too far.")
    print()
    print("FINAL MONEY:", "$" + f"{money:,}")
    print("FINAL HEALTH:", health)
    print()
    print("ENDING: TOO FAR")

else:
    print()
    print("=" * 65)
    print("                       DAY TWELVE")
    print("=" * 65)
    print()
    type_text("Eddie wakes up.")
    type_text("He looks around his apartment.")
    type_text("Everything he ever wanted is there.")
    print()
    type_text("But now he understands something.")
    type_text("Being limitless isn't about having everything.")
    type_text("It's about knowing when enough is enough.")
    print()
    print("FINAL MONEY:", f"${money:,}")
    print("FINAL HEALTH:", health)
    print()
    print("ENDING: CONTROL")