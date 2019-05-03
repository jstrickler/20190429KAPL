#!/usr/bin/env python
import sys
file_name = 'DATA/wombats.txt'

try:
    with open(file_name) as wombats_in:
        for line in wombats_in:
            print(line.rstrip())
except FileNotFoundError as err:
    print(err)


values = 5.3, 4, 9.7, 0, 53, 8.2, 0, 3.3, 9.7, 8, "123", 7.1

for v in values:
    try:
        result = 23.1 / v
    except ZeroDivisionError as err:
        #  log or stop or take other action
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception:
        # print(type(err), err, file=sys.stderr)
        pass  # HIGHLY unrecommended
    else:
        print(result)
    finally:  # no matter what
        print("X")




