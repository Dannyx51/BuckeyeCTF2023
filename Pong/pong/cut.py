

bytes = open("test", "rb").read()

#cut = b'<?xpacket end="w"?>'

start = bytes.find(b"IDAT")


end = bytes.find(b"IEND")

print(start, end)