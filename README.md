# Create a QR-Code

## Usage

1. Enter your secret message into the file 'qr_aim.txt' and save it
2. Execute the python file 'qr.py' with the command 'python3 qr.py'
3. After the script started enter the name of the '.png' file in which the QR-Code is going to be saved
4. Hit 'Enter' 
5. If you type 'ls' you will notice that there is a new file with the name you entered and with the extension '.png' - this is your QR-Code
6. You can open this image and scan the QR-Code and you will see the message you entered into the 'qr_aim.txt' file

## Example

My secret message is: 'Hello, what's up?'. After I saved the text file I run the python script by entering 'python3 qr.py'. Now there is the prompt to enter the name of the QR-Code. I entered the name 'testQR' and hit 'Enter'. Once the script is finished I enter 'ls' to see, if my QR-Code was created and saved. I see another file called 'testQR.png' which is the QR-Code I wanted. If I open the PNG-File I am able to scan the QR-Code and read the message. 
