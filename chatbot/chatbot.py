import google.generativeai as genai
genai.configure(api_key="AIzaSyAqkIvgUrL4gJEvyTp3k_KzfQt-3mdn7JM")

model = genai.GenerativeModel("gemini-1.5-flash")
while True:
    user=input("You : ")
    if user.lower()=="exit":
        print("Bye! See you again")
        break

    response = model.generate_content(user)
    print("ChatBot : ",response.text)
    