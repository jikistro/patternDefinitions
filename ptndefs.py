"""
Patterns Definitions:

Module with predefined patterns.
"""


IP4_ADDR = r"""
              [0-9]{1,3}
            \.[0-9]{1,3}
            \.[0-9]{1,3}
            \.[0-9]{1,3}
           """
#
# IEEE 802 compliant ethernet address
#
ETH_ADDR = r"""
            [0-9a-f]{2}
            [-:.]?
            [0-9a-f]{2}
            [-:.]?
            [0-9a-f]{2}
            [-:.]?
            [0-9a-f]{2}
            [-:.]?
            [0-9a-f]{2}
            [-:.]?
            [0-9a-f]{2}
            (?i)
           """
EMAIL_ADDR = r"^[^\d]\w+@[a-z]+\.[a-z]{2,4}"
WEB_ADDR = r"(www\.)?([^\d]\w+\.)+[a-z]{2,4}"

HTML_TAG = r"<[^<]+?>"



