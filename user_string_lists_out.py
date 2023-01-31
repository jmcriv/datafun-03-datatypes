"""

PS C:\Users\JMC\Documents\datafun-03-datatypes> & C:/Users/JMC/AppData/Local/Programs/Python/Python311/python.exe c:/Users/JMC/Documents/datafun-03-datatypes/user_string_lists.py

Good morning! My name is Jim, and this program will focus on games I have played and string functions.
I have developed 5 lists with names of games - all grouped by their first letter - A, B, C, D, and M.


Here is LIST A
----------------------------------------
['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']

Here is LIST B
----------------------------------------
['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']

Here is LIST C
----------------------------------------
['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']

Here is LIST D
----------------------------------------
['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']

Here is LIST E
----------------------------------------
['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']


TASK 4 SECTION - String Lists 1. Using Python Built-in Functions:
=================================================================
We will be using the Len, Set, and Zip functions:

LIST A PROCESSING
-----------------
LEN A = NUMBER OF ITEMS IN LIST A = 8
SET A = {'Addoku', 'Alphacipher', 'ABC', 'Anagrid', 'Anakross', 'Acrostic', 'Anagrams', 'Acrofit'}

LIST B PROCESSING
-----------------
LEN B = NUMBER OF ITEMS IN LIST B = 6
SET B = {'Batoru', 'Backwards', 'Boggle', 'Boxwise', 'Bracer', 'Backtrack'}

LIST C PROCESSING
-----------------
LEN C = NUMBER OF ITEMS IN LIST C = 5
SET C = {'Calcudoku', 'CanCan', 'Campsite', 'Chopsticks', 'Campixu'}

LIST D PROCESSING
-----------------
LEN D = NUMBER OF ITEMS IN LIST D = 7
SET D = {'Dampfross', 'Dateline', 'Diagramless', 'Dominoes', 'Dingbats', 'DigitALL', 'Dilemma'}

LIST E PROCESSING
-----------------
LEN E = NUMBER OF ITEMS IN LIST E = 4
SET E = {'Masyu', 'MinuPlu', 'Majipiku', 'Magipic'}

ZIP = TUPLE of LIST A & LISTB
-----------------------------
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']
LA=['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']; LB=['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']

ZIP = TUPLE of LIST C & LIST D & LIST E
---------------------------------------
LC=['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']; LD=['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']; LE=['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']
LC=['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']; LD=['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']; LE=['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']
LC=['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']; LD=['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']; LE=['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']
LC=['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']; LD=['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']; LE=['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']


TASK 4 SECTION - String Lists 2. Random Lists:
==============================================
We will be using the Random Choice function to pick one random game from each list.

LIST A
['ABC', 'Acrofit', 'Acrostic', 'Addoku', 'Alphacipher', 'Anagrams', 'Anagrid', 'Anakross']

LIST B
['Backtrack', 'Backwards', 'Batoru', 'Boggle', 'Boxwise', 'Bracer']

LIST C
['Calcudoku', 'Campixu', 'Campsite', 'CanCan', 'Chopsticks']

LIST D
['Dampfross', 'Dateline', 'Diagramless', 'DigitALL', 'Dilemma', 'Dingbats', 'Dominoes']

LIST E
['Magipic', 'Majipiku', 'Masyu', 'MinuPlu']


Five random games I like to play are Alphacipher, Boggle, Chopsticks, Diagramless, and Masyu.


TASK 4 SECTION - String Lists 3. Get Unique Words:
==================================================
We will be using the Open, Read, Split, and Set functions.

OPEN TEXT FILE (text_names_in) AND PRINT CONTENTS
-------------------------------------------------
Michael Jackson
Prince
Madonna
U2
Bruce Springsteen
Run-D.M.C.
Van Halen
Public Enemy
Billy Joel
The Police
Phil Collins
Guns N' Roses
Def Leppard
Janet Jackson
George Michael/Wham
Whitney Houston
Metallica
N.W.A
Dire Straits
AC/DC
Rush
Iron Maiden
Judas Priest
Lionel Richie
Bon Jovi
Talking Heads
Genesis
R.E.M.
Duran Duran
Motley Crue
The Cure
Journey
John Mellencamp
Grandmaster Flash & The Furious Five
REO Speedwagon
Kool and the Gang
L.L. Cool J
Tina Turner
Queen
Beastie Boys
Ozzy Osbourne
The Smiths
Huey Lewis and the News
Bryan Adams
Hall & Oates
Pat Benatar
Eric B. & Rakim
Billy Idol
Peter Gabriel
INXS
Tom Petty & the Heartbreakers
Stevie Ray Vaughan & Double Trouble
Eurythmics
The Cars
Aerosmith
ZZ Top
The Rolling Stones
Heart
David Bowie
Elton John
Rod Stewart
Foreigner
Stevie Wonder
Toto
Bob Seger
The Pointer Sisters
DJ Jazzy Jeff & The Fresh Prince
Salt-N-Pepa
Fleetwood Mac
The Go-Go's
Paul McCartney
Pet Shop Boys
Don Henley
Paul Simon
Tracy Chapman
Cyndi Lauper
Depeche Mode
Sonic Youth
Pete Townshend
Culture Club
Gloria Estefan & Miami Sound Machine
De La Soul
Luther Vandross
Chicago
The Bangles
Thompson Twins
Yes
Men at Work
Pixies
Pink Floyd
Robert Palmer
Kenny Loggins
Whitesnake
Sade
Steve Winwood
Billy Ocean
Tears for Fears
Bobby Brown
Scorpions
Simply Red
B-52's
Boston
Rick James
Joan Jett
Stevie Nicks
Berlin
Sting
New Order
Poison
The Pretenders
Quiet Riot
RATT
The Clash
The Stone Roses
Squeeze
Styx
Frankie Goes to Hollywood
New Edition
Stray Cats
Paula Abdul
The Human League
Violent Femmes
Elvis Costello
A-Ha
Blondie
Eddie Money
Anita Baker
Sheena Easton
Loverboy
Asia
Skid Row
Tiffany
Debbie Gibson
Crosby Stills Nash (& Young)
Madness
Aretha Franklin
Afrika Bambaataa
UB 40
Patti LaBelle
Tone-Loc
Falco
Simple Minds
Earth Wind & Fire
KISS
The Jam
Marvin Gaye
Bananarama
New Kids on the Block
Billy Squier
Slayer
Adam Ant
Spandau Ballet
Milli Vanilli
The Jesus and Mary Chain
ABC
Cinderella
Bonnie Raitt
10,000 Maniacs
Accept
Eric Clapton
Kool Moe Dee
The Cult
The Fixx
Air Supply
Richard Marx
Bruce Hornsby & the Range
Starship
The Replacements
Fine Young Cannibals
Mr. Mister
Boogie Down Productions
Irene Cara
David Lee Roth
Twisted Sister
Corey Hart
Doug E. Fresh
Laura Branigan
Dio
Dokken
A Flock of Seagulls
Eddy Grant
HÃ¼sker DÃ¼
Black Flag
Dead Kennedys
George Thorogood
John Lennon
Terence Trent D'arby
Red Hot Chili Peppers
Rick Springfield
Paul Young
Black Sabbath
Howard Jones
Orchestral Manoeuvres in the Dark
Level 42
Europe
Tom Waits
Mike Oldfield
Chris De Burgh
Alan Parsons Project
John Farnham
Grandmaster Flash & The Furious Five
REO Speedwagon
Kool and the Gang
L.L. Cool J
Tina Turner
Queen
Beastie Boys
Ozzy Osbourne
The Smiths
Huey Lewis and the News
Bryan Adams
Hall & Oates
Pat Benatar
Eric B. & Rakim
Billy Idol
Peter Gabriel
INXS
Tom Petty & the Heartbreakers
Stevie Ray Vaughan & Double Trouble
Eurythmics
The Cars
Aerosmith
ZZ Top
The Rolling Stones
Heart
David Bowie
Elton John
Rod Stewart
Foreigner
Stevie Wonder
Toto
Bob Seger
The Pointer Sisters
DJ Jazzy Jeff & The Fresh Prince



OPEN TEXT FILE (text_names_in), READ CONTENTS, AND PRINT CONTENTS
-----------------------------------------------------------------
Michael Jackson
Prince
Madonna
U2
Bruce Springsteen
Run-D.M.C.
Van Halen
Public Enemy
Billy Joel
The Police
Phil Collins
Guns N' Roses
Def Leppard
Janet Jackson
George Michael/Wham
Whitney Houston
Metallica
N.W.A
Dire Straits
AC/DC
Rush
Iron Maiden
Judas Priest
Lionel Richie
Bon Jovi
Talking Heads
Genesis
R.E.M.
Duran Duran
Motley Crue
The Cure
Journey
John Mellencamp
Grandmaster Flash & The Furious Five
REO Speedwagon
Kool and the Gang
L.L. Cool J
Tina Turner
Queen
Beastie Boys
Ozzy Osbourne
The Smiths
Huey Lewis and the News
Bryan Adams
Hall & Oates
Pat Benatar
Eric B. & Rakim
Billy Idol
Peter Gabriel
INXS
Tom Petty & the Heartbreakers
Stevie Ray Vaughan & Double Trouble
Eurythmics
The Cars
Aerosmith
ZZ Top
The Rolling Stones
Heart
David Bowie
Elton John
Rod Stewart
Foreigner
Stevie Wonder
Toto
Bob Seger
The Pointer Sisters
DJ Jazzy Jeff & The Fresh Prince
Salt-N-Pepa
Fleetwood Mac
The Go-Go's
Paul McCartney
Pet Shop Boys
Don Henley
Paul Simon
Tracy Chapman
Cyndi Lauper
Depeche Mode
Sonic Youth
Pete Townshend
Culture Club
Gloria Estefan & Miami Sound Machine
De La Soul
Luther Vandross
Chicago
The Bangles
Thompson Twins
Yes
Men at Work
Pixies
Pink Floyd
Robert Palmer
Kenny Loggins
Whitesnake
Sade
Steve Winwood
Billy Ocean
Tears for Fears
Bobby Brown
Scorpions
Simply Red
B-52's
Boston
Rick James
Joan Jett
Stevie Nicks
Berlin
Sting
New Order
Poison
The Pretenders
Quiet Riot
RATT
The Clash
The Stone Roses
Squeeze
Styx
Frankie Goes to Hollywood
New Edition
Stray Cats
Paula Abdul
The Human League
Violent Femmes
Elvis Costello
A-Ha
Blondie
Eddie Money
Anita Baker
Sheena Easton
Loverboy
Asia
Skid Row
Tiffany
Debbie Gibson
Crosby Stills Nash (& Young)
Madness
Aretha Franklin
Afrika Bambaataa
UB 40
Patti LaBelle
Tone-Loc
Falco
Simple Minds
Earth Wind & Fire
KISS
The Jam
Marvin Gaye
Bananarama
New Kids on the Block
Billy Squier
Slayer
Adam Ant
Spandau Ballet
Milli Vanilli
The Jesus and Mary Chain
ABC
Cinderella
Bonnie Raitt
10,000 Maniacs
Accept
Eric Clapton
Kool Moe Dee
The Cult
The Fixx
Air Supply
Richard Marx
Bruce Hornsby & the Range
Starship
The Replacements
Fine Young Cannibals
Mr. Mister
Boogie Down Productions
Irene Cara
David Lee Roth
Twisted Sister
Corey Hart
Doug E. Fresh
Laura Branigan
Dio
Dokken
A Flock of Seagulls
Eddy Grant
HÃ¼sker DÃ¼
Black Flag
Dead Kennedys
George Thorogood
John Lennon
Terence Trent D'arby
Red Hot Chili Peppers
Rick Springfield
Paul Young
Black Sabbath
Howard Jones
Orchestral Manoeuvres in the Dark
Level 42
Europe
Tom Waits
Mike Oldfield
Chris De Burgh
Alan Parsons Project
John Farnham
Grandmaster Flash & The Furious Five
REO Speedwagon
Kool and the Gang
L.L. Cool J
Tina Turner
Queen
Beastie Boys
Ozzy Osbourne
The Smiths
Huey Lewis and the News
Bryan Adams
Hall & Oates
Pat Benatar
Eric B. & Rakim
Billy Idol
Peter Gabriel
INXS
Tom Petty & the Heartbreakers
Stevie Ray Vaughan & Double Trouble
Eurythmics
The Cars
Aerosmith
ZZ Top
The Rolling Stones
Heart
David Bowie
Elton John
Rod Stewart
Foreigner
Stevie Wonder
Toto
Bob Seger
The Pointer Sisters
DJ Jazzy Jeff & The Fresh Prince



USE SET, OPEN TEXT FILE (text_names_in), READ UNIQUE CONTENTS, OUTPUT UNIQUE TO NEW FILE, AND PRINT NEW FILE CONTENTS
       (FYI - Added duplicate items to end of INPUT file since there were no duplicates in the file.)
----------------------------------------------------------------------------------------------------------------------

Michael Jackson
Prince
Madonna
U2
Bruce Springsteen
Run-D.M.C.
Van Halen
Public Enemy
Billy Joel
The Police
Phil Collins
Guns N' Roses
Def Leppard
Janet Jackson
George Michael/Wham
Whitney Houston
Metallica
N.W.A
Dire Straits
AC/DC
Rush
Iron Maiden
Judas Priest
Lionel Richie
Bon Jovi
Talking Heads
Genesis
R.E.M.
Duran Duran
Motley Crue
The Cure
Journey
John Mellencamp
Grandmaster Flash & The Furious Five
REO Speedwagon
Kool and the Gang
L.L. Cool J
Tina Turner
Queen
Beastie Boys
Ozzy Osbourne
The Smiths
Huey Lewis and the News
Bryan Adams
Hall & Oates
Pat Benatar
Eric B. & Rakim
Billy Idol
Peter Gabriel
INXS
Tom Petty & the Heartbreakers
Stevie Ray Vaughan & Double Trouble
Eurythmics
The Cars
Aerosmith
ZZ Top
The Rolling Stones
Heart
David Bowie
Elton John
Rod Stewart
Foreigner
Stevie Wonder
Toto
Bob Seger
The Pointer Sisters
DJ Jazzy Jeff & The Fresh Prince
Salt-N-Pepa
Fleetwood Mac
The Go-Go's
Paul McCartney
Pet Shop Boys
Don Henley
Paul Simon
Tracy Chapman
Cyndi Lauper
Depeche Mode
Sonic Youth
Pete Townshend
Culture Club
Gloria Estefan & Miami Sound Machine
De La Soul
Luther Vandross
Chicago
The Bangles
Thompson Twins
Yes
Men at Work
Pixies
Pink Floyd
Robert Palmer
Kenny Loggins
Whitesnake
Sade
Steve Winwood
Billy Ocean
Tears for Fears
Bobby Brown
Scorpions
Simply Red
B-52's
Boston
Rick James
Joan Jett
Stevie Nicks
Berlin
Sting
New Order
Poison
The Pretenders
Quiet Riot
RATT
The Clash
The Stone Roses
Squeeze
Styx
Frankie Goes to Hollywood
New Edition
Stray Cats
Paula Abdul
The Human League
Violent Femmes
Elvis Costello
A-Ha
Blondie
Eddie Money
Anita Baker
Sheena Easton
Loverboy
Asia
Skid Row
Tiffany
Debbie Gibson
Crosby Stills Nash (& Young)
Madness
Aretha Franklin
Afrika Bambaataa
UB 40
Patti LaBelle
Tone-Loc
Falco
Simple Minds
Earth Wind & Fire
KISS
The Jam
Marvin Gaye
Bananarama
New Kids on the Block
Billy Squier
Slayer
Adam Ant
Spandau Ballet
Milli Vanilli
The Jesus and Mary Chain
ABC
Cinderella
Bonnie Raitt
10,000 Maniacs
Accept
Eric Clapton
Kool Moe Dee
The Cult
The Fixx
Air Supply
Richard Marx
Bruce Hornsby & the Range
Starship
The Replacements
Fine Young Cannibals
Mr. Mister
Boogie Down Productions
Irene Cara
David Lee Roth
Twisted Sister
Corey Hart
Doug E. Fresh
Laura Branigan
Dio
Dokken
A Flock of Seagulls
Eddy Grant
HÃ¼sker DÃ¼
Black Flag
Dead Kennedys
George Thorogood
John Lennon
Terence Trent D'arby
Red Hot Chili Peppers
Rick Springfield
Paul Young
Black Sabbath
Howard Jones
Orchestral Manoeuvres in the Dark
Level 42
Europe
Tom Waits
Mike Oldfield
Chris De Burgh
Alan Parsons Project
John Farnham


USE SET, OPEN, READ, and SPLIT functions to pull a text file's data starting with letter P. Using file text_names_in.
       (FYI - Added duplicate items to end of INPUT file since there were no duplicates in the file.)
---------------------------------------------------------------------------------------------------------------------

OUTPUT FILE CONTENT
['Prince\n']['Public Enemy\n']['Phil Collins\n']['Pat Benatar\n']['Peter Gabriel\n']['Paul McCartney\n']['Pet Shop Boys\n']['Paul Simon\n']['Pete Townshend\n']['Pixies\n']['Pink Floyd\n']['Poison\n']['Paula Abdul\n']['Patti LaBelle\n']['Paul Young\n']['Pat Benatar\n']['Peter Gabriel\n']

SET CONTENT
{'Prince\n', 'Pet Shop Boys\n', 'Pink Floyd\n', 'Patti LaBelle\n', 'Paul Young\n', 'Phil Collins\n', 'Peter Gabriel\n', 'Pat Benatar\n', 'Pixies\n', 'Poison\n', 'Paula Abdul\n', 'Pete Townshend\n', 'Public Enemy\n', 'Paul McCartney\n', 'Paul Simon\n'}

USE SPLIT functions to pull a text file's data and separate with commas.
------------------------------------------------------------------------

TEXT SIMPLE IN FILE BEFORE SPLIT
One fish
two fish
red fish
blue fish.


TEXT SIMPLE IN FILE AFTER SPLIT
['O', 'n', 'e', ' ', 'f', 'i', 's', 'h', '\n']
['t', 'w', 'o', ' ', 'f', 'i', 's', 'h', '\n']
['r', 'e', 'd', ' ', 'f', 'i', 's', 'h', '\n']
['b', 'l', 'u', 'e', ' ', 'f', 'i', 's', 'h', '.', '\n']


USE SORT and LEN
----------------

SORTED NAMES FROM TEXT FILE- SEQUENTIAL
['10,000 Maniacs\n', 'A Flock of Seagulls\n', 'A-Ha\n', 'ABC\n', 'AC/DC\n', 'Accept\n', 'Adam Ant\n', 'Aerosmith\n', 'Afrika Bambaataa\n', 'Air Supply\n', 'Alan Parsons Project\n', 'Anita Baker\n', 'Aretha Franklin\n', 'Asia\n', "B-52's\n", 'Bananarama\n', 'Beastie Boys\n', 'Berlin\n', 'Billy Idol\n', 'Billy Joel\n', 'Billy Ocean\n', 'Billy Squier\n', 
'Black Flag\n', 'Black Sabbath\n', 'Blondie\n', 'Bob Seger\n', 'Bobby Brown\n', 'Bon Jovi\n', 'Bonnie Raitt\n', 'Boogie Down Productions\n', 'Boston\n', 'Bruce Hornsby & the Range\n', 'Bruce Springsteen\n', 'Bryan Adams\n', 'Chicago\n', 'Chris De Burgh\n', 'Cinderella\n', 'Corey Hart\n', 'Crosby Stills Nash (& Young)\n', 'Culture Club\n', 'Cyndi Lauper\n', 'DJ Jazzy Jeff & The Fresh Prince\n', 'David Bowie\n', 'David Lee Roth\n', 'De La Soul\n', 'Dead Kennedys\n', 'Debbie Gibson\n', 'Def Leppard\n', 'Depeche Mode\n', 'Dio\n', 'Dire Straits\n', 'Dokken\n', 'Don Henley\n', 'Doug E. Fresh\n', 'Duran Duran\n', 'Earth Wind & Fire\n', 'Eddie Money\n', 'Eddy Grant\n', 'Elton John\n', 'Elvis Costello\n', 'Eric B. & Rakim\n', 'Eric Clapton\n', 'Europe\n', 'Eurythmics\n', 'Falco\n', 'Fine Young Cannibals\n', 'Fleetwood Mac\n', 'Foreigner\n', 'Frankie Goes to Hollywood\n', 'Genesis\n', 'George Michael/Wham\n', 'George Thorogood\n', 'Gloria Estefan & Miami Sound Machine\n', 'Grandmaster Flash & The Furious Five\n', "Guns N' Roses\n", 'Hall & Oates\n', 'Heart\n', 'Howard Jones\n', 'Huey Lewis and the News\n', 'HÃ¼sker DÃ¼\n', 'INXS\n', 'Irene Cara\n', 'Iron Maiden\n', 'Janet Jackson\n', 'Joan Jett\n', 'John Farnham', 'John Lennon\n', 'John Mellencamp\n', 'Journey\n', 'Judas Priest\n', 'KISS\n', 'Kenny Loggins\n', 'Kool Moe Dee\n', 'Kool and the Gang\n', 'L.L. Cool J\n', 'Laura Branigan\n', 'Level 42\n', 'Lionel Richie\n', 'Loverboy\n', 'Luther Vandross\n', 'Madness\n', 'Madonna\n', 'Marvin Gaye\n', 'Men at Work\n', 'Metallica\n', 'Michael Jackson\n', 'Mike Oldfield\n', 'Milli Vanilli\n', 'Motley Crue\n', 'Mr. Mister\n', 'N.W.A\n', 'New Edition\n', 'New Kids on the Block\n', 'New Order\n', 'Orchestral Manoeuvres in the Dark\n', 'Ozzy Osbourne\n', 'Pat Benatar\n', 'Patti LaBelle\n', 'Paul McCartney\n', 'Paul Simon\n', 'Paul Young\n', 'Paula Abdul\n', 'Pet Shop Boys\n', 'Pete Townshend\n', 'Peter Gabriel\n', 'Phil Collins\n', 'Pink Floyd\n', 'Pixies\n', 'Poison\n', 'Prince\n', 'Public Enemy\n', 'Queen\n', 'Quiet Riot\n', 'R.E.M.\n', 'RATT\n', 'REO Speedwagon\n', 'Red Hot Chili Peppers\n', 'Richard Marx\n', 'Rick James\n', 'Rick Springfield\n', 'Robert Palmer\n', 'Rod Stewart\n', 'Run-D.M.C.\n', 'Rush\n', 'Sade\n', 'Salt-N-Pepa\n', 'Scorpions\n', 'Sheena Easton\n', 'Simple Minds\n', 'Simply Red\n', 'Skid Row\n', 'Slayer\n', 'Sonic Youth\n', 'Spandau Ballet\n', 'Squeeze\n', 'Starship\n', 'Steve Winwood\n', 'Stevie Nicks\n', 'Stevie Ray Vaughan & Double Trouble\n', 'Stevie Wonder\n', 'Sting\n', 'Stray Cats\n', 'Styx\n', 'Talking Heads\n', 'Tears for Fears\n', "Terence Trent D'arby\n", 'The Bangles\n', 'The Cars\n', 'The Clash\n', 'The Cult\n', 'The Cure\n', 'The Fixx\n', "The Go-Go's\n", 'The Human League\n', 'The Jam\n', 'The Jesus and Mary Chain\n', 'The Pointer Sisters\n', 'The Police\n', 'The Pretenders\n', 'The Replacements\n', 'The Rolling Stones\n', 'The Smiths\n', 'The Stone Roses\n', 'Thompson Twins\n', 'Tiffany\n', 'Tina Turner\n', 'Tom Petty & the Heartbreakers\n', 'Tom Waits\n', 'Tone-Loc\n', 'Toto\n', 'Tracy Chapman\n', 'Twisted Sister\n', 'U2\n', 'UB 40\n', 'Van Halen\n', 'Violent Femmes\n', 'Whitesnake\n', 'Whitney Houston\n', 'Yes\n', 'ZZ Top\n']
COUNT OF NAMES IN TEXT_NAMES_3 (NORMAL SORT)
200

SORTED NAMES - REVERSE
['ZZ Top\n', 'Yes\n', 'Whitney Houston\n', 'Whitesnake\n', 'Violent Femmes\n', 'Van Halen\n', 'UB 40\n', 'U2\n', 'Twisted Sister\n', 'Tracy Chapman\n', 'Toto\n', 'Tone-Loc\n', 'Tom Waits\n', 'Tom Petty & the Heartbreakers\n', 'Tina Turner\n', 'Tiffany\n', 'Thompson Twins\n', 'The Stone Roses\n', 'The Smiths\n', 'The Rolling Stones\n', 'The Replacements\n', 'The Pretenders\n', 'The Police\n', 'The Pointer Sisters\n', 'The Jesus and Mary Chain\n', 'The Jam\n', 'The Human League\n', "The Go-Go's\n", 'The Fixx\n', 'The Cure\n', 'The Cult\n', 'The Clash\n', 'The Cars\n', 'The Bangles\n', "Terence Trent D'arby\n", 'Tears for Fears\n', 'Talking Heads\n', 'Styx\n', 'Stray Cats\n', 'Sting\n', 'Stevie Wonder\n', 'Stevie Ray Vaughan & Double Trouble\n', 'Stevie Nicks\n', 'Steve Winwood\n', 'Starship\n', 'Squeeze\n', 'Spandau Ballet\n', 'Sonic Youth\n', 'Slayer\n', 'Skid Row\n', 'Simply Red\n', 'Simple Minds\n', 'Sheena Easton\n', 'Scorpions\n', 'Salt-N-Pepa\n', 'Sade\n', 'Rush\n', 'Run-D.M.C.\n', 'Rod Stewart\n', 'Robert Palmer\n', 'Rick Springfield\n', 'Rick James\n', 'Richard Marx\n', 'Red Hot Chili Peppers\n', 'REO Speedwagon\n', 'RATT\n', 'R.E.M.\n', 'Quiet Riot\n', 'Queen\n', 'Public Enemy\n', 'Prince\n', 'Poison\n', 'Pixies\n', 'Pink Floyd\n', 'Phil Collins\n', 'Peter Gabriel\n', 'Pete Townshend\n', 'Pet Shop Boys\n', 'Paula Abdul\n', 'Paul Young\n', 'Paul Simon\n', 'Paul McCartney\n', 'Patti LaBelle\n', 'Pat Benatar\n', 'Ozzy Osbourne\n', 'Orchestral Manoeuvres in the Dark\n', 'New Order\n', 'New Kids on the Block\n', 'New Edition\n', 'N.W.A\n', 'Mr. Mister\n', 'Motley Crue\n', 'Milli Vanilli\n', 'Mike Oldfield\n', 'Michael Jackson\n', 'Metallica\n', 'Men at Work\n', 'Marvin Gaye\n', 'Madonna\n', 'Madness\n', 'Luther Vandross\n', 'Loverboy\n', 
'Lionel Richie\n', 'Level 42\n', 'Laura Branigan\n', 'L.L. Cool J\n', 'Kool and the Gang\n', 'Kool Moe Dee\n', 'Kenny Loggins\n', 'KISS\n', 'Judas Priest\n', 'Journey\n', 'John 
Mellencamp\n', 'John Lennon\n', 'John Farnham', 'Joan Jett\n', 'Janet Jackson\n', 'Iron Maiden\n', 'Irene Cara\n', 'INXS\n', 'HÃ¼sker DÃ¼\n', 'Huey Lewis and the News\n', 'Howard Jones\n', 'Heart\n', 'Hall & Oates\n', "Guns N' Roses\n", 'Grandmaster Flash & The Furious Five\n', 'Gloria Estefan & Miami Sound Machine\n', 'George Thorogood\n', 'George Michael/Wham\n', 'Genesis\n', 'Frankie Goes to Hollywood\n', 'Foreigner\n', 'Fleetwood Mac\n', 'Fine Young Cannibals\n', 'Falco\n', 'Eurythmics\n', 'Europe\n', 'Eric Clapton\n', 'Eric B. & Rakim\n', 'Elvis Costello\n', 'Elton John\n', 'Eddy Grant\n', 'Eddie Money\n', 'Earth Wind & Fire\n', 'Duran Duran\n', 'Doug E. Fresh\n', 'Don Henley\n', 'Dokken\n', 'Dire Straits\n', 'Dio\n', 'Depeche Mode\n', 'Def Leppard\n', 'Debbie Gibson\n', 'Dead Kennedys\n', 'De La Soul\n', 'David Lee Roth\n', 'David Bowie\n', 'DJ Jazzy Jeff & The Fresh Prince\n', 'Cyndi Lauper\n', 'Culture Club\n', 'Crosby Stills Nash (& Young)\n', 'Corey Hart\n', 'Cinderella\n', 'Chris De Burgh\n', 'Chicago\n', 'Bryan Adams\n', 'Bruce Springsteen\n', 'Bruce Hornsby & the Range\n', 'Boston\n', 'Boogie Down Productions\n', 'Bonnie Raitt\n', 'Bon Jovi\n', 'Bobby Brown\n', 'Bob Seger\n', 'Blondie\n', 'Black Sabbath\n', 'Black Flag\n', 'Billy Squier\n', 'Billy Ocean\n', 'Billy Joel\n', 'Billy Idol\n', 'Berlin\n', 'Beastie Boys\n', 'Bananarama\n', "B-52's\n", 'Asia\n', 'Aretha Franklin\n', 'Anita Baker\n', 'Alan Parsons Project\n', 'Air Supply\n', 'Afrika Bambaataa\n', 'Aerosmith\n', 'Adam Ant\n', 'Accept\n', 'AC/DC\n', 'ABC\n', 'A-Ha\n', 'A Flock of Seagulls\n', '10,000 Maniacs\n']
COUNT OF NAMES IN TEXT_NAMES_4 (REVERSE SORT)
200

PS C:\Users\JMC\Documents\datafun-03-datatypes> 



"""