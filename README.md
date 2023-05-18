# Projects computer networks

# File Transfer Simulation Project

Our project aims to simulate the process of transferring files between two computers over a network. It consists of a server component and a client component. The server waits for client connections and receives file data, while the client initiates the transfer and sends files to the server. For easy to use, we use one PC as both client and server, that is, they have the same IP but different ports.

![diagram_exchange.png](./assets/diagram_exchange.png)

# Running

- In the same PC, on 2 different terminal/cmd
    - Run `python server.py` on one terminal
    - Run `python client.py` on the other
- **Note**: In the repo, I create a `./hello.txt` with a small size but the rate of send/receiving is small as well. For large files, we can reach by the same mechanism with a higher rate