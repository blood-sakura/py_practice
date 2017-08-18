#!/usr/bin/env python

def counter(startAt=0):
    count = startAt
    while True:
        val = yield count
        if val is not None:
            count = val
        else:
            count += 1

# count= counter(5)
# print count.next()
# print count.next()
# print count.send(9)
# print count.next()
# count.close()

numbers = (count for count in counter(5) if count < 20)
for i in numbers:
    print i