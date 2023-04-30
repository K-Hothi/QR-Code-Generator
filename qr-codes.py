import qrcode

def CreateFile():
    with open("Example-File.txt", "a") as file:
        file.write("This is an example file.txt. \n")
        file.write("Try to make a QR code of the text in this file!")

def ConvertToQrCode():
    while True:
        try:
            file = input("Enter file to convert: ")

            with open(f"{file}", "r") as data:
                img = qrcode.make(data.read())
                img.save(f"codes/{file.split('.')[0]}-QR.png")

            break
        except:
            print()
            print("File not found, try again")
            print()

#Create a demo file to practice and debug with when the project gets bigger
command = input("Would you like to practice with a demo file? (Y/N): ")
if(command == "Y"):
    CreateFile()

#Run the method to covert text to qr codes
ConvertToQrCode()
