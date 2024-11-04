with open('some.bin', 'rb') as bin_fh:
    bin_fh.seek(100)
    data = bin_fh.read(5)
    print(data)
    bin_fh.seek(0)
    data = bin_fh.read(10)
    print(data)
                                        # __exit__


