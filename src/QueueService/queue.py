from flask import Flask, request, jsonify
from azure.storage.queue import QueueServiceClient
from azure.core.exceptions import ResourceExistsError
from flask_cors import CORS
import json

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
CORS(app)
app.run(port=5001)

sas_token = r"sv=2022-11-02&ss=q&srt=sco&sp=rwdlacup&se=2024-06-30T18:34:35Z&st=2024-06-03T10:34:35Z&spr=https&sig=bfeO3soR92xBx8ZD0df%2BaI0F87Mj%2BPeDgK9bS8dD81k%3D"
queue_name = "calculadoraqueue"
service_url = "https://trainercloudshell.queue.core.windows.net"

queue_service_client = QueueServiceClient(account_url=service_url, credential=sas_token)

# Crea la cola si no existe
try:
    queue_service_client.create_queue(queue_name)
except ResourceExistsError:
    pass

queue_client = queue_service_client.get_queue_client(queue_name)

@app.route('/api/queue', methods=['POST'])
def enqueue():
    data = request.get_json()
    operacion = data.get('operacion')
    numero1 = data.get('numero1')
    numero2 = data.get('numero2')

    # Crea un mensaje con los datos recibidos
    message = {
        'operacion': operacion,
        'numero1': numero1,
        'numero2': numero2
    }

    # Convierte el mensaje a una cadena JSON y lo coloca en la cola
    queue_client.send_message(json.dumps(message))

    return jsonify({'status': 'Message enqueued'}), 200

@app.route('/api/queue', methods=['GET'])
def dequeue():
    # Recupera el último mensaje de la cola
    messages = queue_client.receive_messages()

    # Si hay mensajes en la cola, borra el último mensaje y devuelve su contenido
    for message in messages:
        # Elimina el mensaje de la cola
        queue_client.delete_message(message)
        break  # Solo procesa un mensaje por vez
    return jsonify({'status': 'Message dequeued'}), 200

if __name__ == '__main__':
    app.run(debug=True)