# -*- coding: utf-8 -*-

# “NikkyBot”
# Copyright ©2012-2014 Travis Evans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from _table import *

# General patterns used for all personalities, including 'nikky'

patterns = (
# Legal forms:
# pattern regexp, priority, action
# pattern regexp, priority, action, allow repeat?
# pattern regexp, last reply, priority, action, allow repeat?

## Basics ##

(r"\b(hi|hello|hey|sup|what's up|welcome)\b", 0,
    R(
        Markov_forward('{1}'),
        Markov_forward('{1} {0}'),
        '{1}, {0}',
    ),
),
(r"\b(how are you|how are we|how's your|how is your)\b", 0,
    R(
        Markov_forward('ok'),
        Markov_forward('okay'),
        Markov_forward('good'),
        Markov_forward('bad')
    ),
),
(r"\b(good night|goodnight|g'?night)\b", 0,
    R(
        Markov_forward('night'),
        Markov_forward('night {0}'),
    )
),
(r"\b(bye|bye bye|goodbye|good bye|see you later|night|good night|g'night)\b",
0,
    R(
        Markov_forward('bye'),
        Markov_forward('bye {0}')
    ),
),
(r"\b(congratulations|congrats|congradulations)", 1,
    R(
        Markov_forward('Thanks'),
        Markov_forward('thx'),
    )
),
(r'\b(thanks|thank you)\b', 1,
    R(
        Markov_forward("you're welcome"),
        'np'
    )
),
(r'\b(wb|welcome back|welcoem back)\b', 1,
    R(
        Markov_forward('Thanks'),
        Markov_forward('thx'),
    )
),
(r"\*\*\*yes/no\*\*\*", -99,
    R(
        Markov_forward('yes'),
        Markov_forward('no'),
        Markov_forward('maybe'),
        Markov_forward('yeah'),
        Markov_forward('probably'),
        Markov_forward('yes'),
        Markov_forward('only if'),
        Markov_forward('only when'),
        Markov_forward('as long as'),
        Markov_forward('whenever'),
        Markov_forward('of course')
    )
),

## General ##

(r"which", 1,
    R(
        Markov_forward('this'),
        Markov_forward('that'),
        Markov_forward('the'),
        Markov_forward('those'),
        Markov_forward('these'),
        Markov_forward('all of'),
        Markov_forward('all the'),
    ),
),
(r"^anything else", 1,
    S(
        R('', Recurse('***yes/no***')),
        '\n',
        Recurse("what's"),
    ),
),
(r"^(what do you|what is going|what's going)", -2, Recurse('for what')),
(r"(^(what|what's|whats)|for what|for which)", 1,
    R(
        Markov_forward('a'),
        Markov_forward('an'),
        Markov_forward('the'),
        Markov_forward("It's a"),
        Markov_forward("It's an"),
        Markov_forward("It's the"),
        Markov_forward("It is a"),
        Markov_forward("It is an"),
        Markov_forward("It is the"),
        Recurse('how many'),
    ),
),
(r"^(who is|who's|what is|what's|how's|how is) (the |a |an |your |my )?(.*?)\?*$", 0,
    R(
        Markov_forward('{3} is'),
        Markov_forward('{3}'),
        Markov_forward('A {3} is'),
        Markov_forward('An {3} is'),
        Markov_forward('The {3} is'),
        Markov_forward('A {3}'),
        Markov_forward('An {3}'),
        Markov_forward('The {3}'),
        Recurse("what's"),
    ),
),
(r"^(who are|who're|what are|what're|how're|how are) (.*?)\?*$", 0,
    R(
        Markov_forward('{2} are'),
        Markov_forward("They're"),
        Markov_forward('They are'),
    ),
),
(r"^(what are|what're) .*ing\b", -1,
    Recurse("what's"),
),
(r'^where\b', 0,
    R(
        Markov_forward('in'),
        Markov_forward('on'),
        Markov_forward('on top of'),
        Markov_forward('inside of'),
        Markov_forward('inside'),
        Markov_forward('under'),
        Markov_forward('behind'),
        Markov_forward('outside'),
        Markov_forward('over'),
        Markov_forward('up'),
        Markov_forward('beyond'),
    )
),
(r'^when\b', 1,
    R(
        'never',
        'forever',
        'right now',
        'tomorrow',
        'now',
        Markov_forward('never'),
        Markov_forward('tomorrow'),
        Markov_forward('as soon as'),
        Markov_forward('whenever'),
        Markov_forward('after'),
        Markov_forward('before'),
        Markov_forward('yesterday'),
        Markov_forward('last'),
        Markov_forward('next'),
    )
),
(r'^how (long|much longer|much more time)\b', -2,
    R(
        'never',
        'forever',
        Markov_forward('until'),
        Markov_forward('as soon as'),
        Markov_forward('whenever'),
    )
),
(r'^how\b', 1,
    R(
        Markov_forward('by'),
        Markov_forward('via'),
        Markov_forward('using'),
        Markov_forward('use'),
        Markov_forward('only by'),
        Markov_forward('only by using'),
        Markov_forward('just use'),
    )
),
(r'\bwho (are you|is {0})\b', -1,
    R(
        Markov_forward("I'm"),
        Markov_forward("I am"),
    ),
),
(r'\b(why|how come)\b', 0,
    R(
        Markov_forward('because'),
        Markov_forward('because your'),
        Markov_forward('because you'),
        Markov_forward('because of'),
        Markov_forward('because of your')
    )
),
(r'\bwhat does it mean\b', 1,
    Markov_forward('it means')
),
(r'\b(who|what) (does|do|did|should|will|is) (\S+) (.*?)\?*$', -1,
    R(
        Recurse('which'),
        Markov_forward('{3} {4}'),
        Markov_forward('{3} {4}s'),
    ),
),
(r'\bcontest\b', 1,
    R(
        Recurse("I'm entering"),
        Recurse("You'll lose"),
        Recurse('My entry'),
        Markov_forward('Contests'),
        Markov('contest')
    )
),
(r'\b(how much|how many|what amount)\b', -2,
    R(
        Markov_forward('enough'),
        Markov_forward('too many'),
        Markov_forward('more than you'),
        Markov_forward('not enough'),
    )
),
(r"^(is|isn't|are|am|does|should|can|do)\b", 2, Recurse('***yes/no***')),
(r'^(do you think|what about|really)\b', 0, R(Recurse('***yes/no***'))),
(r"^(is|are|am|should|can|do|does|which|what|what's|who|who's)(?: \S+)+[ -](.*?)\W+or (.*)\b", -1,
    S(
        R(
            'both',
            'neither',
            'dunno',
            S('{2}', R('--', '? ', ': ', '\n'), Recurse('what do you think of {2}')),
            S('{3}', R('--', '? ', ': ', '\n'), Recurse('what do you think of {3}'))
        ),
        '\n',
        R('', Markov_forward('because', [' ']), Markov_forward('since', [' '])),
    ),
),
(r'\bwhat time\b', 0,
    R(
        Markov_forward('time for'),
        Markov_forward("it's time"),
    ),
),
(r"\b(will|should|can|going to|won't|wouldn't|would|can't|isn't|won't) (\w+)\b", 5,
    R(
        Markov_forward('and'),
        Markov_forward('and just'),
        Markov_forward('and then'),
        Markov_forward('and then just'),
        Markov_forward('or'),
        Markov_forward('or just'),
        Markov_forward('yes and'),
        Markov_forward('yes or'),
        Markov_forward('yeah and'),
        Markov_forward('yes and'),
        Markov_forward('yes and just'),
        Markov_forward('yes or just'),
        Markov_forward('yeah and just'),
        Markov_forward('yes and just'),
        Markov_forward('and {2}'),
        Markov_forward('and just {2}'),
        Markov_forward('and then {2}'),
        Markov_forward('and then just {2}'),
        Markov_forward('or {2}'),
        Markov_forward('or just {2}'),
        Markov_forward('yes and {2}'),
        Markov_forward('yes or {2}'),
        Markov_forward('yeah and {2}'),
        Markov_forward('yes and {2}'),
        Markov_forward('yes and just {2}'),
        Markov_forward('yes or just {2}'),
        Markov_forward('yeah and just {2}'),
        Markov_forward('yes and just {2}'),
        Markov_forward('why'),
    ),
),
(r"(?:is(?: it)?|it's|i'm|i am)\b ([^][.;,!?(){{}}]+)", -5,
    R(
        Recurse('{1}'),
        Recurse('{1}'),
        Recurse('{1}'),
    ),
),

## Meta ##

(r'(Do )?you (like|liek) (.*)(.*?)\W?$', -1,
    R(
        Recurse('what do you think about {3}'),
        Recurse('yes'),
        S(
            R('', 'No, but ', 'Yes, and '),
            Markov_forward('I like'),
        ),
        Markov_forward("I'd rather"),
        'of course'
    )
),
(r'^(\S+ (u|you|{0})$|(\bWe |\bI )\S+ (u|you|{0}))', 5,
    S(
        R('Great\n', 'gee\n', 'thanks\n', 'Awesome\n'),
        R(
            Markov_forward('I wish you'),
            Markov_forward('I hope you'),
            Markov_forward('I hope your'),
            Markov_forward('You deserve'),
            Markov_forward("You don't deserve"),
        ),
    ),
),
(r'\b({0} is|you are|{0} must|you must) (a |an |)(.*)', 1,
    R(
        Markov_forward('I am'),
        Markov_forward("I'm"),
        Markov_forward('I am really'),
        Markov_forward("I'm really"),
        Markov_forward('I am actually'),
        Markov_forward("I'm actually"),
    )
),
(r"\b(what do you think|how do you feel|(what is|what's|what are) your (thought|thoughts|opinion|opinions|idea|ideas)) (about |of |on )(a |the |an )?(.*?)\W?$", -3,
    R(
        Markov_forward('{6} is'),
        Markov_forward('{6}'),
        Markov_forward('better than'),
        Markov_forward('worse than'),
    ),
),
(r"\bis (.*) (any good|good)", -3, Recurse('what do you think of {1}')),
(r"^(what do you think|what do you know|how do you feel|(what is|what's|what are) your (thought|thoughts|opinion|opinions|idea|ideas)) (about |of |on )me\W?$", -3,
    R(
        Markov_forward('you'),
        Recurse('what do you think of {0}')
    )
),
(r"^(how is|how's|do you like|you like|you liek) (.*?)\W?$", -3,
    Recurse('what do you think of {2}')
),
(r"\btell (me|us) about (.*)", -2, Recurse('{2}')),

)