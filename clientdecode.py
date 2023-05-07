from clienttorosencprovider import ClientToRosEncProvider

# Just a test script that can be used to check if the encryption/decryption is correct.

# To use it, you can get a hex stream from the client response in Wireshark and use decrypt function.
# By default it uses platfrom key from PS3, you can change it in encprovider.py.

message = bytearray.fromhex("5a7e9185a96944a68fb2c489c7fc9a47e06ea044d140d6e79026652f641870a8c6ad79a35e730dedd803d743ec7cd8e0a6b5c89ebbbcc66f8466ec171578a82e2eeff2ddbf8c0c0d5d981201ce9b840270b225fe6129089911c014833e7d330a42f4dd07425ed432797b9b3e105d5cd3fcb1c661f71016ecea11cf52e93df446ed4e53c82c78a3d0886f742a37edbd01867886842634af49cffb7281c5499a8d82d62b927698ba0c7358edc828bca0b34def7684000cf12eb7e240714620caf2eb725eca0c10b54e380f9504916b6eb96f5b8971a1b84a1347e32af9977afb821acf73b510cc8e93620c6f6b9147e4f958cd5551cf7669806747a1729df5e62efa36936c44adba3044dfed0dfec10e7cc0acc07d548fa992da33373181432229d591f473fae1faa9fedacac78726837a62020cc7696477d8569b95a9fed3f0ff160fb186cf78abd31d898f3bdae6f2552f741f49b84df9f38ef3cc13b2144faf45e42c09ebbbe2d2ea66f493b9aafd2954638c60ccf234e5026b571912bb40ea299fd7a0f107b8872d3fc003fd7d594ce80729aa54a97956428e14f9111338e395222e491efa7d0c202797291051259a9261f87cda4e7063de4043a9d20444804ca5a036674618c9be85fe78a95745b072aac692")

body = ClientToRosEncProvider().decrypt(message)

print(body)