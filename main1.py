business_name = "X Saloon"
service = {"haircut": 100, "head massage": 80,
           "hairdying": 150, "shaving": 50}

leads = []


def reply (message):
     message = message.lower()

     #booking logic
     if "book" in message:
          for item in service:
               if item in message:
                    name = input("Enter your name: ")
                    phone_number = input("Enter your Phone number: ")
                    leads.append({"name": name, "phone_number": phone_number, "service": service})
                    return f"Booked {item} for {name}"
               return "Mention a valid service"
          for item in service:
               if item in message:
                    return f"{item} - rs {service[item]}"
               return "Invalid request."
          
print("Welcome to", business_name)

while True:
    msg = input("Customer: ")

    if msg == "exit":
                    break
    if msg == "show":
                    continue
    
    print("Chatpal: ", reply(msg))
    


               