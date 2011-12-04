import dummyprinter, string
d = dummyprinter.DummyPrinter()
d.write(string.ascii_lowercase, 10)
d.write("hello world! how are you today?", 10)
raw_input("press enter to quit")
