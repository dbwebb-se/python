#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""To display an ascii painting made up of several smaller parts."""

import option
import painting


def main():
    """Main function where it all starts."""
    options = option.parse_options()
    if not options["silent"]:
        print(__doc__)
    if options["verbose"]:
        print(options)

    art = painting.create_from_file(
        options["filename"],
        verbose=options["verbose"]
    )
    print(art)


if __name__ == "__main__":
    main()
