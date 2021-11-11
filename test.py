import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self,access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A7W-kOTI5hxCMqRtoulWZrlPFzsaF25NIQUg64E6vQDR_LYzxZec1S4sBrxqpac8RZRd4MTdnfoQ9fSuEk4aGf_5eAcP7v3bT_YBnsZw0c0iN82dgaxeH4mGrWeb-J08cifcRmE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved :)")

main()