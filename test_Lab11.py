# Tests for Lab11
# Print The Number of Times a Letter Character Appears in a Phrase

import os.path
import sys
from Lab11 import main
from tud_tests import *

def test_Lab11():

    try:
        exists = os.path.exists("Lab11.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input([t The little train that could])
    main()
    output = get_display_output()

    assert output == [
        5
        ]

    try:
        exists = os.path.exists("Lab11.py")
        assert exists == True
    except:
        sys.exit()

    # Test 2
    set_keyboard_input([s Suzy saw a silly seal])
    main()
    output = get_display_output()

    assert output == [
        3
        ]
        
    # Test 3
    set_keyboard_input([N Monday morning])
    main()
    output = get_display_output()

    assert output == [
        0
        ]