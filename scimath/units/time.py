#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Travis N. Vaught
# Date: 05/22/2005
# Description: Define units of time
#
# Derived from: units/time.py [pyre system]
#               Michael A.G. Aivazis
#               California Institute of Technology
#               (c) 1998-2003
#
# Symbols defined: pico-, nano-, micro-, milli- ...second [and aliases]
#                  minute, hour, day, year
#
#------------------------------------------------------------------------------

#############################################################################
# Imports:
#############################################################################

from SI import second
from SI import pico, nano, micro, milli

#############################################################################
# Definitions:
#############################################################################
# Definitions of common time units
# Data taken from Appendix F of Halliday, Resnick, Walker,
#     "Fundamentals of Physics", fourth edition, John Willey and Sons, 1993

second.label = 'second'
picosecond = pico*second
picosecond.label = 'picosecond'
nanosecond = nano*second
nanosecond.label = 'nanosecond'
microsecond = micro*second
microsecond.label = 'microsecond'
millisecond = milli*second
millisecond.label = 'millisecond'

# other common units

minute = 60 * second
hour = 60 * minute
day = 24 * hour
year = 365.25 * day

#############################################################################
# Aliases:
#############################################################################

s = sec = second
ps = picosecond
ns = nanosecond
us = microsecond
ms = msec = millisecond

us = usec = microsecond

# plural aliases
seconds = second
microseconds = microsecond
milliseconds = millisecond

#### EOF ######################################################################