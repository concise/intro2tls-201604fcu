git clone https://github.com/concise/intro2tls-201604fcu.git

cd intro-to-tls-april-2016

git checkout testdata

make

./run-example-server

sudo tcpdump -i lo -w /tmp/captured-packets.pcap host 127.0.0.1 and port 4430

./run-example-client
#
# or:
#
#   1. open new Firefox
#   2. import self-signed-certs/rootca.crt
#   3. navigate to https://localhost:4430/
#

mkdir /tmp/tcp-flows

cd /tmp/tcp-flows

tcpflow -r /tmp/captured-packets.pcap

# There should be two files in the directory /tmp/tcp-flows containing the TCP
# traffic, one for client-to-server and another one for server-to-client.
