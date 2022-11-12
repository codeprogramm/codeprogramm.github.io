console.log("dsvsdvc");
// Загрузка и отображение сообщений
      function loadMessages() {
        $.get("/get_messages",
              (data) => {
                $("#chat_window").empty();
                var messages = data["messages"];
                for (var i in messages) {
                  var message = messages[i];
                  var name = message["sender"];
                  var text = message["text"];
                  var time = message["time"];
                  console.log(name, text, time);
                  var html = "<div> <b style='color:#1aad00;'>( " +name + ": )</b>" + "<b style='color:#c4beb7;'> " + text + " </b>" +  "<i style='color:#1aad00'>" + time + "</i> </div>";
                  var div = $(html); // div = визуальный элемент с сообщением

                  $("#chat_window").append(div);
                }
              }
           );
      }

      // Отправка сообщения
      function sendMessage() {
        var text = $("#text").val();
        $.get("/send_message", { "sender" : name, "text" : text});
        $("#text").val("");
        }

      // При загрузке страницы
      $(() => {
        
        // При нажатии клавиш в поле текст
        $("#text").on("keypress", (event) => {
          
          // При нажатии Enter, вызвать функцию sendMessage
          if (event.keyCode == 13) {
            document.write(" мспипас")
            sendMessage();
          }
      });

      // Каждую секунду вызывать loadMessages
      setInterval(loadMessages, 5000);
      });
