# Chershire Network Tool

## Description
Chershire is a network tool that combines a simple command and control (C2) server with a client, and includes a teardrop attack implementation using Scapy. This tool is for educational and authorized testing purposes only.

## Features
- ASCII art display
- C2 server functionality
- Client connection and command execution
- Teardrop attack implementation

## Components
1. Server (`start_chershire`)
2. Client (`connect_chershire`)
3. Teardrop attack function

## Requirements
- Python 3.x
- Scapy library

## Installation
1. Clone the repository:

git clone https://github.com/yourusername/chershire.git
text
2. Install required libraries:

pip install scapy
text

## Usage

### Starting the Server
Run the script with the server functionality:

python chershire_server.py
text

### Connecting a Client
Run the client script on the target machine:

python chershire_client.py
text

### Teardrop Attack
The `teardrop` function can be called with a target IP address to perform a teardrop attack.

## Warning
This tool is for educational and authorized testing purposes only. Misuse of this tool may be illegal and unethical. Always obtain proper authorization before testing on any network or system you do not own.

## Disclaimer
The creators and contributors of this tool are not responsible for any misuse or damage caused by this program. Use at your own risk.

## License
[Insert your chosen license here]

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
- Steven van Zelst
