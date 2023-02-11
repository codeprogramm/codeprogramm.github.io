# Flask - библиотека для создания веб-сервера
from flask import Flask, request, render_template
from datetime import datetime
import json


warrning_vocabulare=["Дебил","Дурак"]
app = Flask(__name__)
DATA_FILE = "data_001.json"
DATA_FILE1 = "data_002.json"
#

# Загружаем сообщения из файла
def load_messages():
  # json_file = open(DATA_FILE, "r")
  # json_file.close()
  with open(DATA_FILE, "r") as json_file:
    data = json.load(json_file)  # data = {"all_messages":  [] }
    return data["all_messages"]

def load_messages_warrning():
  # json_file = open(DATA_FILE, "r")
  # json_file.close()
  with open(DATA_FILE1, "r") as json_file1:
    data1 = json.load(json_file1)  # data = {"all_messages":  [] }
    return data1["all_messages"]


all_messages = load_messages()  # При старте сервера, загружаем сообщения из файла в переменную
all_messages_warrning= load_messages_warrning()


# Сохраняем сообщения в файл
def save_messages():
  with open(DATA_FILE, "w") as json_file:
    data = {"all_messages": all_messages}
    json.dump(data, json_file)

def save_messages_warrning():
  with open(DATA_FILE1, "w") as json_file:
    data = {"all_messages": all_messages_warrning}
    json.dump(data, json_file)



# Сохраним сообщения в файл (JSON)


@app.route("/")
def hello_world():
  return render_template("form.html")


# API для получения сообщений
# /get_messages => {"messages": [...]}


@app.route("/get_messages")
def get_messages():
  return {"messages": all_messages}


def add_message(name, id_sender,  id, text):
  # time: подставить автоматически
  
  print(type(id_sender))
  new_message = {
    "name": name,
    "id_sender": id_sender,
    "id_user": id,
    "text": text,
    "time": datetime.now().strftime("%H:%M"),
  }
  # append - добавить элемент в список
  all_messages.append(new_message)
  save_messages()  # Сохраняем в файл

def add_message_warrning(name, id_sender,  id, text):
  # time: подставить автоматически
  
  new_message = {
    "name": name,
    "id_sender": id_sender,
    "id_user": id,
    "text": text,
    "time": datetime.now().strftime("%H:%M"),
  }
  # append - добавить элемент в список
  all_messages_warrning.append(new_message)
  save_messages_warrning()  # Сохраняем в файл
  

# API для отправки сообщений /send_message?sender=Mike&text=Hello
@app.route("/send_message")
def send_message():
  name = request.args["name"]
  id_sender = request.args["id_sender"]# ToDO: error here, sender vs name
  id = request.args["id_user"]
  text = request.args["text"]
  i=0
  wv=False
  while i!=1:
    if text!=warrning_vocabulare[i]:
      i=i+1
    if text == warrning_vocabulare[i]:
      i=1
      add_message_warrning(name, id_sender, id, text)
      break
    if i==1 and text!=warrning_vocabulare[i]:
      add_message(name, id_sender, id, text)
      
      

  return {"result": True}

app.route("/send_status")

  
app.run(host="0.0.0.0", port=80)
