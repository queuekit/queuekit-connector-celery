import click


@click.command()
@click.option('-n', '--connector-name', default='Default connector', help='Name for the connector.')
@click.option('-a', '--api-key', help='QueueMetrics.io organization API key. Get this from https://dashboard.queuemetrics.io')
@click.option('-h', '--host', default="localhost", help='Redis host.')
@click.option('-p', '--port', default="6379", help='Redis port.')
@click.option('-d', '--database', default="0", help='Redis database.')
@click.option('-w', '--password', help='Redis password.')
@click.option('--tls', help='Use a TLS connection to Redis.')
@click.option('-u', '--uri', help='Redis URI.')
@click.option('-s', '--sentinels', help='Comma-seperated list of sentinel host/port pairs.')
@click.option('-m', '--master', help='Name of master node used in sentinel configuration')
@click.option('-b', '--backend', default="wss://api.queuemetrics.io", help='QueueMetrics backend.')
def main(connector_name, api_key, host, port, database, password, tls, uri, sentinels, master, backend):
    click.echo(f"Hello {connector_name}!")


if __name__ == '__main__':
    main()
