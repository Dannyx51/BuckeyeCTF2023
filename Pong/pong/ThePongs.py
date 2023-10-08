import pcapng

allData = b""

with open('./ThePings.pcapng', 'rb') as fp:
    scanner = pcapng.FileScanner(fp)
    
    count = 0
    for block in scanner:	
        if type(block) == pcapng.blocks.EnhancedPacket:
            # print("-"*40)
            # print(block, type(block))

            data = block.packet_data

            if len(data) != 98:

                arr = data.split(b"01234567")

                # print("-"*40)
                # print(data, len(data))
                allData += arr[1]

                print(len(allData))

        
                # count += 1
                # if count > 1:
                #     break

with open("test", "wb") as f:
    f.write(allData)