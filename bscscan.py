#!env python2
# encoding: utf-8

import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_WARNING, ICON_INFO

log = Workflow3.logger


def main(wf):
    log.debug("Execution started")
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`
    import string

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...
    # this is the address/keyword input by the user
    query = sys.argv[1].lower()
    log.debug("Query: " + query)

    # Set defaults
    title = "No results found"
    icon = ICON_WARNING
    url = False

    if query == "d" or query == "da" or query == "dai":
        title = "View Dai on BscScan"
        icon = "img/dai.png"
        url = "https://bscscan.com/token/0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3"

    elif query == "u" or query == "us" or query == "usd" or query == "usdc":
        title = "View USD Coin on BscScan"
        icon = "img/usdc.png"
        url = "https://bscscan.com/token/0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"

    elif (
        query == "usdt"
        or query == "t"
        or query == "te"
        or query == "tet"
        or query == "teth"
        or query == "tethe"
        or query == "tether"
    ):
        title = "View Tether on BscScan"
        icon = "img/tether.png"
        url = "https://bscscan.com/token/0x55d398326f99059fF775485246999027B3197955"

    elif len(query) == 66 or len(query) == 64:
        title = "View transaction '" + query + "'"
        icon = "icon.png"
        url = "https://bscscan.com/tx/" + query

    elif len(query) == 42 or len(query) == 40:
        title = "View address '" + query + "'"
        icon = "icon.png"
        url = "https://bscscan.com/address/" + query

    # Add an item to Alfred feedback
    wf.add_item(
        title=title,
        icon=icon,
        arg=url,  # argument to pass to Alfred
        valid=not not url,  # tells Alfred item is actionable
    )

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == "__main__":
    # Create a global `Workflow3` object
    wf = Workflow3(update_settings={
                   "github_slug": "muyinliu/alfred-bscscan-search"})
    log = wf.logger

    # Check for updates
    # http://www.deanishe.net/alfred-workflow/guide/update.html#guide-updates
    if wf.update_available:
        wf.add_item('New version available',
                    'Action this item to install the update',
                    autocomplete='workflow:update',
                    icon=ICON_INFO)

    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
