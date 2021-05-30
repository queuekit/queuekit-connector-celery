import click
import socketio


@click.command()
@click.option('-n', '--connector-name', default='Default connector', help='Name for the connector.')
@click.option('-a', '--api-key', help='QueueMetrics.io organization API key. Get this from https://dashboard.queuemetrics.io')
@click.option('-b', '--backend', default="wss://api.queuemetrics.io", help='QueueMetrics backend.')
@click.option('-o', '--broker-url', help='Celery broker URL.')
def main(connector_name, api_key, backend, broker_url):
    websocketUri = backend

    sio = socketio.Client()

    @sio.event
    def connect():
        print("Socket connected to", websocketUri)
        sio.emit('initialize-connector-connection', {
            'apiKey': api_key,
            'connectorType': 'celery',
            'connectorName': connector_name,
            'connectorVersion': '0.0.1'
        })

    @sio.event
    def connect_error(data):
        print("The connection failed!")

    @sio.event
    def disconnect():
        print("Socket disconnected from", websocketUri)

    print("Attempting to connect to", websocketUri)
    sio.connect(websocketUri)


if __name__ == '__main__':
    main()
