import time

print("🎤 Namaskar Deviyon aur Sajjano, swagat hai aapka Kaun Banega Crorepati mein!")
time.sleep(2)
print("Main hoon aapka host, Amitabh Bachchan.\n")
time.sleep(2)
print("Spnsored by  : Realiance jio \n")
print("Produced by : Sony Entertainment Telivision ....\n")
time.sleep(2)
print("Chaliye shuru karte hain aaj ka khel...\n")
time.sleep(2)


questions = [
    {
        "question": "Which of these is not a part of the human body?",
        "options": {"A": "Liver", "B": "Heart", "C": "Kidney", "D": "Laptop"},
        "answer": "D",
        "prize": 100000
    },
    {
        "question": "Which of these is a means of sending messages on a mobile phone?",
        "options": {"A": "SMS", "B": "MMS", "C": "Email", "D": "Postcard"},
        "answer": "D",
        "prize": 1000000
    },
    {
        "question": "Which of these will you not normally find in a kitchen?",
        "options": {"A": "Frying Pan", "B": "Spatula", "C": "Pillow", "D": "Gas Stove"},
        "answer": "C",
        "prize": 5000000
    },
    {
        "question": "If you mix red and yellow colours, which colour do you get?",
        "options": {"A": "Green", "B": "Orange", "C": "Blue", "D": "Pink"},
        "answer": "B",
        "prize": 9000000
    },
    {
        "question": "Which of these is used to call someone on the phone?",
        "options": {"A": "Ringtone", "B": "Dialer", "C": "Charger", "D": "Cover"},
        "answer": "B",
        "prize": 10000000
    }
]

winnings = 0

for q in questions:
    print("\n🕹️ Agla prashna aapke saamne hai...")
    print(f"\nQ: {q['question']}")
    for key, value in q["options"].items():
        print(f"{key}: {value}")

    print("\n👉 Aapke paas 10 second hain jawab dene ke liye!")
    
    # Countdown 10 sec
    for i in range(10, 0, -1):
        print(f"⏳ {i}...", end="\r")
        time.sleep(1)
    
    choice = input("\nEnter your answer (A/B/C/D) or type 'quit' to exit: ").upper()

    if choice == "QUIT":
        print(f"\n🙌 Aapne game chhodne ka faisla kiya.")
        print(f"Aap jeet kar jaa rahe hain ₹{winnings}\n")
        break
    
    if choice == q["answer"]:
        winnings = q["prize"]
        print(f"🎉 Bilkul sahi jawab! Aap jeet gaye ₹{winnings}\n")
    else:
        print(f"❌ Afsos, yeh galat jawab hai. Sahi jawab tha: {q['answer']}")
        print(f"👉 Aap ghar le jaa rahe hain ₹{winnings}\n")
        break
else:
    print(f"\n🏆 Mubarak ho! Aapne saare sawaalon ka sahi jawab diya aur jeet gaye ₹{winnings} 🎊")