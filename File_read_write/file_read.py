#!/usr/bin/python3
fi = open ( "/tmp/test.txt", 'w' )

with open ( "/tmp/test.txt", 'w' ) as f:
    f.write("Hello how are you")
    print(f.closed)
print(f.closed)
