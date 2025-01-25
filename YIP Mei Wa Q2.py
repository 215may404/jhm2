snacks = input("Do you want some snacks?(yes/no)")
if snacks == "no":
  print("Good!Let's play games instead.")
elif snacks == "yes":
  choices = input("Enter your choice (ice-cream/cookies/candies):")
  if choices == "ice-cream":
    print("Remember to wash your hands.")
  elif choices == "cookie":
    print("Can you share with your friends?")
  elif choices == "candies":
    print("Don't eat too much.")
  else:
    print("Invalid choice.")
else:
  print("Invalid choice.")
