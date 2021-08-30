import zmq
import os

host = os.environ['QUEUE_HOST']
print(host)

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server", flush=True)
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{host}:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s ..." % request, flush=True)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message), flush=True)


