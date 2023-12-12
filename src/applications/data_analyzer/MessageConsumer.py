#!/usr/bin/env python3
import pika, sys, os, json
from data_analyzer.AnalyzeData import AnalyzeData

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='auctions')

    def callback(ch, method, properties, body):
        body = json.loads(body) 
        AnalyzeData(body.auction_auid, body.auction_price, body.auction_zip_code, body.auction_sqft)
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='auctions', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)