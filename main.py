import dropbox

class Transfer:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, dropbox_file_path):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), dropbox_file_path)

def main():
    access_token = "sl.ArOY2eamI-DPlXTVu12O-aaRQtUc0A07YDhg0NBJTUKCzX9vC-c3ivU29xDV8IVEWQxzbo9XX7y9tyW0BqTvRxwQArLegG-DxA6pfGvHxOiIU-caTzu_RKbdEn_WnbeNnXRQk8U1v3w"
    transfer_data = Transfer(access_token)
    file_from_path = input("Enter Your File to Tranfer:")
    dropbox_file_path = input("Enter your Dropbox Path: ")

    transfer_data.upload_file(file_from_path, dropbox_file_path)
    print("CHECK UR FILES!!!!")

main()