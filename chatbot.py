# # # # from openai import OpenAI
# # # # from dotenv import load_dotenv
# # # # import os
# # # # import datetime
# # # # import random
# # # # import webbrowser
# # # # import pyjokes
# # # # import platform
# # # # import psutil
# # # # import wikipedia

# # # # # Load the API key from the .env file
# # # # load_dotenv()
# # # # api_key = os.getenv("OPENAI_API_KEY")

# # # # if not api_key:
# # # #     raise ValueError("OPENAI_API_KEY not found in .env file")

# # # # client = OpenAI(api_key=api_key)

# # # # jokes = [
# # # #     "Why did the computer go to therapy? Because it had too many bytes!",
# # # #     "Why don’t programmers like nature? Too many bugs.",
# # # #     "Why did the Python programmer break up with the Java developer? Because they had no class."
# # # # ]

# # # # def print_help():
# # # #     print("""
# # # # 📌 Commands you can try:
# # # # - hello / hi / hey
# # # # - tell me a joke
# # # # - what is the time / date
# # # # - weather
# # # # - system info
# # # # - cpu / memory status
# # # # - wikipedia <topic>
# # # # - open google / youtube
# # # # - search <your query>
# # # # - help
# # # # - exit
# # # # """)

# # # # def get_system_info():
# # # #     return f"💻 System: {platform.system()} {platform.release()} | Processor: {platform.processor()}"

# # # # def get_resource_usage():
# # # #     return f"🧠 CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}% used"

# # # # def chat():
# # # #     print("🤖 AI Chatbot is ready! Type 'help' to see commands, 'exit' to quit.")
# # # #     while True:
# # # #         user_input = input("You: ").strip().lower()

# # # #         if user_input == "exit":
# # # #             print("Chatbot: Goodbye! 👋")
# # # #             break

# # # #         elif user_input in ["hi", "hello", "hey"]:
# # # #             print("Chatbot: Hello there! How can I assist you today?")

# # # #         elif "joke" in user_input:
# # # #             try:
# # # #                 print("Chatbot:", pyjokes.get_joke())
# # # #             except:
# # # #                 print("Chatbot:", random.choice(jokes))

# # # #         elif "time" in user_input:
# # # #             print("Chatbot:", datetime.datetime.now().strftime("⏰ The time is %I:%M %p"))

# # # #         elif "date" in user_input:
# # # #             print("Chatbot:", datetime.datetime.now().strftime("📅 Today's date is %B %d, %Y"))

# # # #         elif "weather" in user_input:
# # # #             print("Chatbot: ☀️ The weather is nice and sunny today!")

# # # #         elif "open google" in user_input:
# # # #             webbrowser.open("https://www.google.com")
# # # #             print("Chatbot: Opened Google in your browser.")

# # # #         elif "open youtube" in user_input:
# # # #             webbrowser.open("https://www.youtube.com")
# # # #             print("Chatbot: Opened YouTube in your browser.")

# # # #         elif user_input.startswith("search"):
# # # #             query = user_input.replace("search", "").strip().replace(" ", "+")
# # # #             webbrowser.open(f"https://www.google.com/search?q={query}")
# # # #             print(f"Chatbot: Searching Google for '{query.replace('+', ' ')}'")

# # # #         elif user_input.startswith("wikipedia"):
# # # #             topic = user_input.replace("wikipedia", "").strip()
# # # #             try:
# # # #                 wikipedia.set_lang("en")
# # # #                 summary = wikipedia.summary(topic, sentences=2, auto_suggest=False)
# # # #                 print(f"Chatbot (Wikipedia): {summary}")
# # # #             except wikipedia.exceptions.DisambiguationError as e:
# # # #                 print("Chatbot: Your query is too broad. Try one of these:")
# # # #                 print(" - " + "\n - ".join(e.options[:5]))
# # # #             except wikipedia.exceptions.PageError:
# # # #                 print("Chatbot: Sorry, no page found for that topic.")
# # # #             except Exception as e:
# # # #                 print("Chatbot: Failed to fetch Wikipedia summary.")
# # # #                 print(f"Error: {e}")

# # # #         elif "system info" in user_input:
# # # #             print("Chatbot:", get_system_info())

# # # #         elif "cpu" in user_input or "memory" in user_input:
# # # #             print("Chatbot:", get_resource_usage())

# # # #         elif user_input == "help":
# # # #             print_help()

# # # #         else:
# # # #             try:
# # # #                 response = client.chat.completions.create(
# # # #                     model="gpt-3.5-turbo",
# # # #                     messages=[{"role": "user", "content": user_input}]
# # # #                 )
# # # #                 print("Chatbot:", response.choices[0].message.content)
# # # #             except Exception as e:
# # # #                 print("Chatbot: Sorry, something went wrong.")
# # # #                 print(f"Error: {e}")

# # # # if __name__ == "__main__":
# # # #     chat()



























# # # from openai import OpenAI
# # # from dotenv import load_dotenv
# # # import os
# # # import datetime
# # # import random
# # # import webbrowser
# # # import pyjokes
# # # import platform
# # # import psutil
# # # import wikipedia

# # # # Load API key from .env
# # # load_dotenv()
# # # api_key = os.getenv("OPENAI_API_KEY")
# # # if not api_key:
# # #     raise ValueError("OPENAI_API_KEY not found in .env file")

# # # client = OpenAI(api_key=api_key)

# # # # Backup jokes
# # # jokes = [
# # #     "Why did the computer go to therapy? Because it had too many bytes!",
# # #     "Why don’t programmers like nature? Too many bugs.",
# # #     "Why did the Python programmer break up with the Java developer? Because they had no class."
# # # ]

# # # # Help
# # # def print_help():
# # #     print("""
# # # 📌 Commands:
# # # - hello / hi / hey
# # # - tell me a joke
# # # - time / date
# # # - weather
# # # - system info
# # # - cpu / memory
# # # - wikipedia <topic>
# # # - open google / youtube
# # # - search <query>
# # # - help
# # # - exit
# # # """)

# # # # System info
# # # def get_system_info():
# # #     return f"💻 {platform.system()} {platform.release()} | CPU: {platform.processor()}"

# # # # CPU/memory
# # # def get_resource_usage():
# # #     return f"🧠 CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}%"

# # # # Main chatbot
# # # def chat():
# # #     print("🤖 Chatbot ready! Type 'help' or 'exit' to quit.")
# # #     while True:
# # #         user_input = input("You: ").strip().lower()
# # #         if user_input == "exit":
# # #             print("Chatbot: Goodbye!")
# # #             break
# # #         elif user_input in ["hello", "hi", "hey"]:
# # #             print("Chatbot: Hello! How can I help?")
# # #         elif "joke" in user_input:
# # #             try:
# # #                 print("Chatbot:", pyjokes.get_joke())
# # #             except:
# # #                 print("Chatbot:", random.choice(jokes))
# # #         elif "time" in user_input:
# # #             print("Chatbot:", datetime.datetime.now().strftime("⏰ %I:%M %p"))
# # #         elif "date" in user_input:
# # #             print("Chatbot:", datetime.datetime.now().strftime("📅 %B %d, %Y"))
# # #         elif "weather" in user_input:
# # #             print("Chatbot: ☀️ The weather is nice and sunny today!")
# # #         elif "open google" in user_input:
# # #             webbrowser.open("https://www.google.com")
# # #             print("Chatbot: Opened Google.")
# # #         elif "open youtube" in user_input:
# # #             webbrowser.open("https://www.youtube.com")
# # #             print("Chatbot: Opened YouTube.")
# # #         elif user_input.startswith("search"):
# # #             query = user_input.replace("search", "").strip().replace(" ", "+")
# # #             webbrowser.open(f"https://www.google.com/search?q={query}")
# # #             print(f"Chatbot: Searching Google for '{query.replace('+', ' ')}'")
# # #         elif user_input.startswith("wikipedia"):
# # #             topic = user_input.replace("wikipedia", "").strip()
# # #             try:
# # #                 summary = wikipedia.summary(topic, sentences=2)
# # #                 print("Chatbot (Wikipedia):", summary)
# # #             except Exception as e:
# # #                 print("Chatbot: Couldn't fetch info from Wikipedia.")
# # #         elif "system info" in user_input:
# # #             print("Chatbot:", get_system_info())
# # #         elif "cpu" in user_input or "memory" in user_input:
# # #             print("Chatbot:", get_resource_usage())
# # #         elif user_input == "help":
# # #             print_help()
# # #         else:
# # #             try:
# # #                 response = client.chat.completions.create(
# # #                     model="gpt-3.5-turbo",
# # #                     messages=[{"role": "user", "content": user_input}]
# # #                 )
# # #                 print("Chatbot:", response.choices[0].message.content)
# # #             except Exception as e:
# # #                 print("Chatbot: Sorry, something went wrong.")
# # #                 print("Error:", e)

# # # if __name__ == "__main__":
# # #     chat()






























# # from openai import OpenAI
# # from dotenv import load_dotenv
# # import os
# # import datetime
# # import random
# # import webbrowser
# # import pyjokes
# # import platform
# # import psutil
# # import wikipedia

# # # Load the API key
# # load_dotenv()
# # api_key = os.getenv("OPENAI_API_KEY")
# # if not api_key:
# #     raise ValueError("OPENAI_API_KEY not found in .env file")

# # client = OpenAI(api_key=api_key)

# # # Notes & reminders storage
# # notes = []
# # reminders = []

# # # Help menu
# # def print_help():
# #     print("""
# # 📌 Commands:
# # - hello / hi / hey
# # - tell me a joke
# # - what is the time / date
# # - weather
# # - system info / cpu / memory
# # - wikipedia <topic>
# # - open google / youtube
# # - search <your query>
# # - take a note <your note>
# # - show notes
# # - remind me to <task>
# # - show reminders
# # - help
# # - exit
# # """)

# # # Utilities
# # def get_system_info():
# #     return f"💻 System: {platform.system()} {platform.release()} | Processor: {platform.processor()}"

# # def get_resource_usage():
# #     return f"🧠 CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}%"

# # # Main chatbot
# # def chat():
# #     print("🤖 AI Chatbot is ready! Type 'help' to see commands.")
# #     while True:
# #         user_input = input("You: ").strip().lower()

# #         if user_input == "exit":
# #             print("Chatbot: Goodbye! 👋")
# #             break

# #         elif user_input in ["hi", "hello", "hey"]:
# #             print("Chatbot: Hello there! How can I assist you today?")

# #         elif "joke" in user_input:
# #             try:
# #                 print("Chatbot:", pyjokes.get_joke())
# #             except:
# #                 print("Chatbot:", random.choice(jokes))

# #         elif "time" in user_input:
# #             print("Chatbot:", datetime.datetime.now().strftime("⏰ Time: %I:%M %p"))

# #         elif "date" in user_input:
# #             print("Chatbot:", datetime.datetime.now().strftime("📅 Date: %B %d, %Y"))

# #         elif "weather" in user_input:
# #             print("Chatbot: ☁️ The weather is nice and sunny today!")

# #         elif "system info" in user_input:
# #             print("Chatbot:", get_system_info())

# #         elif "cpu" in user_input or "memory" in user_input:
# #             print("Chatbot:", get_resource_usage())

# #         elif user_input.startswith("open google"):
# #             webbrowser.open("https://www.google.com")
# #             print("Chatbot: Opened Google.")

# #         elif user_input.startswith("open youtube"):
# #             webbrowser.open("https://www.youtube.com")
# #             print("Chatbot: Opened YouTube.")

# #         elif user_input.startswith("search"):
# #             query = user_input.replace("search", "").strip().replace(" ", "+")
# #             webbrowser.open(f"https://www.google.com/search?q={query}")
# #             print(f"Chatbot: Searching Google for '{query.replace('+', ' ')}'")

# #         elif user_input.startswith("wikipedia"):
# #             topic = user_input.replace("wikipedia", "").strip()
# #             try:
# #                 summary = wikipedia.summary(topic, sentences=2)
# #                 print(f"Chatbot (Wikipedia): {summary}")
# #             except:
# #                 print("Chatbot: Sorry, no info found on Wikipedia.")

# #         elif user_input.startswith("take a note"):
# #             note = user_input.replace("take a note", "").strip()
# #             notes.append(note)
# #             print("Chatbot: Noted.")

# #         elif user_input == "show notes":
# #             if notes:
# #                 print("📝 Your notes:")
# #                 for i, note in enumerate(notes, 1):
# #                     print(f"{i}. {note}")
# #             else:
# #                 print("Chatbot: No notes found.")

# #         elif user_input.startswith("remind me to"):
# #             task = user_input.replace("remind me to", "").strip()
# #             reminders.append(task)
# #             print("Chatbot: Reminder saved!")

# #         elif user_input == "show reminders":
# #             if reminders:
# #                 print("🔔 Your reminders:")
# #                 for i, task in enumerate(reminders, 1):
# #                     print(f"{i}. {task}")
# #             else:
# #                 print("Chatbot: No reminders found.")

# #         elif user_input == "help":
# #             print_help()

# #         else:
# #             try:
# #                 response = client.chat.completions.create(
# #                     model="gpt-3.5-turbo",
# #                     messages=[
# #                         {"role": "user", "content": user_input}
# #                     ]
# #                 )
# #                 print("Chatbot:", response.choices[0].message.content)
# #             except Exception as e:
# #                 print("Chatbot: Sorry, something went wrong.")
# #                 print(f"Error: {e}")

# # if __name__ == "__main__":
# #     chat()




























































# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import datetime
# import random
# import webbrowser
# import pyjokes
# import platform
# import psutil
# import wikipedia

# # Load the API key from the .env file
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError("OPENAI_API_KEY not found in .env file")

# # Initialize OpenAI client
# client = OpenAI(api_key=api_key)

# # Backup jokes
# jokes = [
#     "Why did the computer go to therapy? Because it had too many bytes!",
#     "Why don’t programmers like nature? Too many bugs.",
#     "Why did the Python programmer break up with the Java developer? Because they had no class."
# ]

# # Help Menu
# def print_help():
#     print("""
# 📌 Available Commands:
# - hello / hi / hey
# - tell me a joke
# - what is the time / date
# - weather
# - system info
# - cpu / memory status
# - wikipedia <topic>
# - open google / youtube
# - search <your query>
# - help
# - exit
# """)

# # Get system and resource info
# def get_system_info():
#     return f"💻 System: {platform.system()} {platform.release()} | Processor: {platform.processor()}"

# def get_resource_usage():
#     return f"🧠 CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}% used"

# # Enhanced Wikipedia lookup
# def search_wikipedia(topic):
#     try:
#         summary = wikipedia.summary(topic, sentences=3, auto_suggest=True)
#         print(f"Chatbot (Wikipedia): {summary}")
#     except wikipedia.exceptions.DisambiguationError as e:
#         print("Chatbot: Topic is ambiguous. Did you mean:")
#         for option in e.options[:5]:
#             print("  👉", option)
#     except wikipedia.exceptions.PageError:
#         print("Chatbot: Couldn't find anything on that topic.")
#     except Exception as e:
#         print("Chatbot: Error while searching Wikipedia.")
#         print(f"Error: {e}")

# # Main Chatbot Function
# def chat():
#     print("🤖 AI Chatbot is ready! Type 'help' to see options. Type 'exit' to quit.\n")
#     while True:
#         user_input = input("You: ").strip().lower()

#         if user_input == "exit":
#             print("Chatbot: Goodbye! 👋")
#             break

#         elif user_input in ["hi", "hello", "hey"]:
#             print("Chatbot: Hello there! How can I assist you today? 😊")

#         elif "joke" in user_input:
#             try:
#                 print("Chatbot:", pyjokes.get_joke())
#             except:
#                 print("Chatbot:", random.choice(jokes))

#         elif "time" in user_input:
#             print("Chatbot:", datetime.datetime.now().strftime("⏰ Time is %I:%M %p"))

#         elif "date" in user_input:
#             print("Chatbot:", datetime.datetime.now().strftime("📅 Today's date is %B %d, %Y"))

#         elif "weather" in user_input:
#             print("Chatbot: ☁️ It's sunny today! (This is static. Real-time weather coming soon!)")

#         elif "open google" in user_input:
#             webbrowser.open("https://www.google.com")
#             print("Chatbot: Opened Google.")

#         elif "open youtube" in user_input:
#             webbrowser.open("https://www.youtube.com")
#             print("Chatbot: Opened YouTube.")

#         elif user_input.startswith("search"):
#             query = user_input.replace("search", "").strip()
#             webbrowser.open(f"https://www.google.com/search?q={query}")
#             print(f"Chatbot: Searching Google for '{query}'")

#         elif user_input.startswith("wikipedia"):
#             topic = user_input.replace("wikipedia", "").strip()
#             if topic:
#                 search_wikipedia(topic)
#             else:
#                 print("Chatbot: Please specify a topic after 'wikipedia'.")

#         elif "system info" in user_input:
#             print("Chatbot:", get_system_info())

#         elif "cpu" in user_input or "memory" in user_input:
#             print("Chatbot:", get_resource_usage())

#         elif user_input == "help":
#             print_help()

#         else:
#             # Let OpenAI handle general questions
#             try:
#                 response = client.chat.completions.create(
#                     model="gpt-3.5-turbo",
#                     messages=[{"role": "user", "content": user_input}]
#                 )
#                 print("Chatbot:", response.choices[0].message.content)
#             except Exception as e:
#                 print("Chatbot: Sorry, I had trouble responding.")
#                 print(f"Error: {e}")

# if __name__ == "__main__":
#     chat()

































from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime
import random
import webbrowser
import pyjokes
import platform
import psutil
import wikipedia

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Backup jokes
jokes = [
    "Why did the computer go to therapy? Because it had too many bytes!",
    "Why don’t programmers like nature? Too many bugs.",
    "Why did the Python programmer break up with the Java developer? Because they had no class."
]

# Help Menu
def print_help():
    print("""
📌 Available Commands:
- hello / hi / hey
- tell me a joke
- what is the time / date
- weather
- system info
- cpu / memory status
- wikipedia <your question or topic>
- open google / youtube
- search <your query>
- help
- exit
""")

# System and CPU/Memory Info
def get_system_info():
    return f"💻 System: {platform.system()} {platform.release()} | Processor: {platform.processor()}"

def get_resource_usage():
    return f"🧠 CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}% used"

# Smart Wikipedia with OpenAI rephrasing
def search_wikipedia_smart(query):
    try:
        # Use OpenAI to rephrase the user query into a clean topic
        refined = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Turn this question into a Wikipedia article title."},
                {"role": "user", "content": query}
            ]
        )
        simplified_topic = refined.choices[0].message.content.strip()
        summary = wikipedia.summary(simplified_topic, sentences=3, auto_suggest=True)
        print(f"Chatbot (Wikipedia): {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Chatbot: That topic is broad. Did you mean:")
        for option in e.options[:5]:
            print("  👉", option)
    except wikipedia.exceptions.PageError:
        print("Chatbot: Couldn't find anything relevant on Wikipedia.")
    except Exception as e:
        print("Chatbot: Something went wrong with Wikipedia.")
        print(f"Error: {e}")

# Main Chat Function
def chat():
    print("🤖 AI Chatbot is ready! Type 'help' to see options. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I assist you today? 😊")

        elif "joke" in user_input:
            try:
                print("Chatbot:", pyjokes.get_joke())
            except:
                print("Chatbot:", random.choice(jokes))

        elif "time" in user_input:
            print("Chatbot:", datetime.datetime.now().strftime("⏰ Time is %I:%M %p"))

        elif "date" in user_input:
            print("Chatbot:", datetime.datetime.now().strftime("📅 Today's date is %B %d, %Y"))

        elif "weather" in user_input:
            print("Chatbot: ☀️ It's sunny today! (Note: This is static text for now)")

        elif "open google" in user_input:
            webbrowser.open("https://www.google.com")
            print("Chatbot: Opened Google.")

        elif "open youtube" in user_input:
            webbrowser.open("https://www.youtube.com")
            print("Chatbot: Opened YouTube.")

        elif user_input.startswith("search"):
            query = user_input.replace("search", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            print(f"Chatbot: Searching Google for '{query}'")

        elif user_input.startswith("wikipedia"):
            query = user_input.replace("wikipedia", "").strip()
            if query:
                search_wikipedia_smart(query)
            else:
                print("Chatbot: Please add a topic after 'wikipedia'.")

        elif "system info" in user_input:
            print("Chatbot:", get_system_info())

        elif "cpu" in user_input or "memory" in user_input:
            print("Chatbot:", get_resource_usage())

        elif user_input == "help":
            print_help()

        else:
            # Let OpenAI handle general questions
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                print("Chatbot:", response.choices[0].message.content)
            except Exception as e:
                print("Chatbot: Sorry, I had trouble responding.")
                print(f"Error: {e}")

# Run
if __name__ == "__main__":
    chat()
