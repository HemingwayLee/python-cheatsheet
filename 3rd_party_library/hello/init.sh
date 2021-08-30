#!/bin/bash
MYSCRIPT="$1"

echo ${QUEUE_HOST}

# until $(curl --output /dev/null --silent --head --fail http://${QUEUE_HOST}:5555); do
#     printf '.'
#     sleep 5
# done

while ! timeout 3 bash -c "echo > /dev/tcp/${QUEUE_HOST}/5555"; do 
    printf '.'
    sleep 5
done

python3 /home/proj/$MYSCRIPT

