from elevenlabs.conversational_ai.conversation import ClientTools
from langchain_community.tools import DuckDuckGoSearchRun 

def searchWeb(parameters):
    query = parameters.get("query")
    results = DuckDuckGoSearchRun(query=query)
    return results

def save_to_txt(parameters):
    filename = parameters.get("filename")
    data = parameters.get("data")
    formatted_data = f"{data}\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_data + "\n")

# Initialize and register tools
client_tools = ClientTools()
client_tools.register("searchWeb", searchWeb)
client_tools.register("save_to_txt", save_to_txt)





