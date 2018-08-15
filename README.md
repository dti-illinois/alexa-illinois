# Alexa Skills in the University of Illinois at Urbana-Champaign
[![Build Status][travis-image]][travis-url] [![Deploy Status](https://img.shields.io/badge/deploy-partial-yellow.svg)](https://img.shields.io)  
Alexa skills that provides multiple student-related utilities to be deployed for echo dots in the University of Illinois at Urbana-Champaign campus. Funtionalities covers dining info, library info, EWS usage, course info, sports, mass transportation and so on. 

#### Notes: 
- This is an unofficial development and is not supported or controlled by the University of Illinois at Urbana-Champaign itself.
- These skills are currently being developed in progess, they are not guaranteed to function properly.

Feel free to submit an issue or contribute!

## Skills
- [Dining Information](#dining-information)  
- [Library Information](#library-information)  
- [Staff Information](#staff-information)  
- [Lab Usage](#lab-usage)  
- [Sports Schedule](#sports-schedule)  
- [CUMTD](#cumtd)  
- [Course Information](#course-information)  
- [Wireless Information](#wireless-information)  

## Dining Information
This skill can provide user with the menu of the 20 dining halls (supported hall list below) in the campus of the University of Illinois at Urbana-Champaign.

### Supported Language
- Invoke skill:  
   - Alexa, start menu checker.  
- Apply/Remove food filter:  
   - Vegan/Vegetarian/Gluten-free.  
- General query:  
   - {meal} in {hall} today/tomorrow?  
   - What's the {meal} in {hall} today/tomorrow?  
   - What's the {meal} at {hall} today/tomorrow?  
   - What is the {meal} in {hall} today/tomorrow?  
   - {meal} {date} in {hall}?  
   - What's the {meal} today/tomorrow in {hall}?  
   - What's the {meal} today/tomorrow at {hall}?  
   - What is the {meal} today/tomorrow in {hall}?  
- Activate interactive mode (it asks questions):  
   - Interactive.  
- Interactive mode: answer meal:  
   - {meal}.
- Interactive mode: answer hall:  
   - {hall}.
- Interactive mode: answer date:  
   - Today/Tomorrow.
- After a query, ask about the details:
   - Detail/Details.

### Supported dining halls
| Residence Hall | Dining Hall | Supported Names in the skill|
| -------------- | ----------- | --------------- |
| Lincoln Avenue (LAR) | Lincoln/Allen Dining Hall | LAR, LAR Dining Hall, LAR Hall | 
| Lincoln Avenue (LAR) | Field of Greens | Field of Greens |
| Lincoln Avenue (LAR) | Leafy! | Leafy! |
| Pennsylvania Avenue (PAR) | PAR Dining Hall | PAR, PAR Dining Hall, PAR Hall |
| Pennsylvania Avenue (PAR) | Penn Station | Penn Station |
| Illinois Street (ISR) | ISR Dining Hall | ISR, ISR Dining Hall, ISR Hall |
| Illinois Street (ISR) | CHOMPS | CHOMPS |
| Illinois Street (ISR) | Cocina Mexicana | Cocina Mexicana |
| Illinois Street (ISR) | Taste of Asia | Taste of Asia |
| Ikenberry | Ikenberry Dining Hall | Ikenberry, Ikenberry Dining Hall, Ikenberry Hall |
| Ikenberry | 57 North | 57 North |
| Ikenberry | Better Burger | Better Burger |
| Ikenberry | Caffeinator | Caffeinator |
| Ikenberry | Neo Soul Ingredient | Neo Soul Ingredient |
| Florida Avenue (FAR) | FAR Dining Hall | FAR, FAR Dining Hall, FAR Hall |
| Florida Avenue (FAR) | Cracked Egg Café | Cracked Egg Café |
| Florida Avenue (FAR) | Soul Ingredient | Soul Ingredient |
| Busey-Evans | Busey-Evans Dining Hall | Busey-Evans, Busey-Evans Dining Hall, Busey-Evans Hall |
| Busey-Evans | Busey Bean and Green | Busey Bean and Green |
| Busey-Evans | Oodles | Oodles |

## Library Information
This skill can provide user with the information and updated opening hours of 30+ libraries in the campus of the University of Illinois at Urbana-Champaign.

### Supported Language
- Invoke skill:  
   - Alexa, start library checker.  
- Ask general information about a Library:  
   - information {library}  
   - {library} information  
   - information of {library}  
- Ask opening hours of a specific date of a library:
   - {library} opening hours {date}  
   - {library} opening hours on {date}  
   - {library} {date} opening hours  
   - opening hours {library} {date}  
   - opening hours of {library} {date}  
   - opening hours of {library} on {date}  
   - what's the opening hours of {library} {date}  
   - what's the opening hours of {library} on {date}  
   - what's the {library} opening hours on {date}  
   - what is the opening hours of {library} {date}  
   - what is the opening hours of {library} on {date}  
   - what is the {library} opening hours on {date}  
- Ask opening hours of a library next seven days:
   - {library} next seven days  
   - next seven days {library}  
   - next seven days of {library}  

### Supported libraries
| ID | Library | Supported Names in the skill |
| ---------- | ------- | ---------------------------- |
| 1 | Grainger Library | Grainger, Grainger Library, Grainger Engineering Library Information Center |
| 3 | Mathematics Library | Mathematics Library |
| 5 | Communications Library | Communications Library |
| 6 | International and Area Studies Library | International and Area Studies Library |
| 9 | A.C.E.S. Library | A.C.E.S. Library, Funk Library |
| 11 | Social Sciences, Health, and Education Library | Social Sciences, Health, and Education Library |
| 12 | Architecture and Art Library | Architecture and Art Library, Ricker Library |
| 13 | University Archives | University Archives |
| 16 | Map Library | Map Library |
| 17 | Undergraduate Library | Undergraduate Library |
| 22 | Rare Book and Manuscript Library | Rare Book and Manuscript Library |
| 23 | Literatures and Languages Library | Literatures and Languages Library |
| 27 | Music and Performing Arts Library | Music and Performing Arts Library, M.P.A.L. |
| 29 | Law Library | Law Library |
| 31 | Illinois History and Lincoln Collections | Illinois History and Lincoln Collections |
| 34 | University High School Library | University High School Library |
| 37 | Center for Children's Books | Center for Children's Books |
| 44 | Illinois Fire Service Institute Library | Illinois Fire Service Institute Library |
| 50 | Interlibrary Loan and Document Delivery | Interlibrary Loan and Document Delivery |
| 56 | Residence Hall Libraries - Urbana | Residence Hall Libraries - Urbana |
| 57 | Scholarly Commons | Scholarly Commons |
| 59 | Sousa Archives & Center For American Music | Sousa Archives & Center For American Music |
| 73 | Veterinary Medicine Library | Veterinary Medicine Library |
| 75 | History, Philosophy, and Newspaper Library | History, Philosophy, and Newspaper Library |
| 76 | Chemistry Library | Chemistry Library |
| 80 | Main Library | Main Library |
| 81 | Student Life and Culture Archives | Student Life and Culture Archives, Archives Research Center |
| 82 | Residence Hall Libraries - Ikenberry | Residence Hall Libraries - Ikenberry |
| 83 | Oak Street Library | Oak Street Library |


## Staff Information
This skill can provide user with some information about staff, including professors, employees, in the campus of the University of Illinois at Urbana-Champaign.

### Supported Language
- Invoke skill:  
   - Alexa, start staff checker.  
- Input first name:
   - First name, {first name}.
- Input middlename:
   - Middle name, {middle name}.
- Input last name:
   - Last name, {last name}.
- Start the query:
   - Start/Begin/Query.

## Lab Usage
This skill provides user with computer usage information in EWS labs, ICS labs and residence halls in the campus of the University of Illinois at Urbana-Champaign.

### Supported Language
- Invoke skill:
   - Alexa, start lab checker.  
- Quick search for engineering workstation: 
   - Find me an engineering workstation.
   - Find me an engineering computer.
   - Find me an engineering lab.
   - Find me a workstation (recommended)
- Quick search for general use computer:
   - Find me a general computer.
   - Find me a general lab.
   - Find me a lab (recommanded)
- Search for a specific building:
   - How many available computers in {building name}
   - Information abount/on {building name}
   - Tell me about {building name}
   - {building name} (recommended)
- Search for a specific room in building:
   - Information on {building name} room {room number}
   - Tell me about {building name} room {room number}
   - {building name} room {room number} (recommended)

### Supported labs/buildings
| Buildings | Supported Names | Supported Rooms |
| --------- | --------------- | --------------- |
| Digital Computer Laboratory | Digital Computer Laboratory (Lab), DCL | 416, 426, 440, 520 |
| Electrical and Computer Engineering Building | Electrical and Computer Engineering Building, ECE Building, ECEB, ECE | 2022, 3022, 3070|
| Engineering Hall | Engineering Hall, EH | 406(B)1, 406(B)8 |
| Grainger Engineering Library | Grainger (Engineering) Library, Grainger, GELIB | 4th floor center, 4th floor east |
| Mechanical Engineering Library | Mechanical Engineering Laboratory (Lab), Mechanical Lab, MEL | 1001, 1009 |
| Siebel Center | Siebel Center, Sieble, SIEBL | (0)218, (0)220, (0)222, (0)403 |
| Transportation Building | Transportation Building, TB | 207, 302, 316 |
| Allen Residence Hall | Allen Residence Hall, ALN |
| Busey Evans | Busey Evans, BEH |
| Daniels | Daniels, DAN |
| English | English, ENG |
| Florida Avenue | Florida Avenue, FAR |
| Illini Hall | Illini Hall |
| Ikenberry Floor One | Ikenberry Floor One |
| Ikenberry Floor Two | Ikenberry Floor Two |
| Illinois Street | Illinois Street, ISR |
| Nevada | Nevada, NEV |
| Oregon | Oregon, OR |
| Orchard Downs | Orchard Downs, ORC |
| Pennsylvania Avenue | Pennsylvania Avenue, PAR |
| Sherman | Sherman, SHM |
| Undergrad | Undergrad, UG |
| Illini Union | Illini Union, UN |
| Wohlers | Wohlers, WH |

## Sports Schedule
This skill provides user with athletic schedule for 19 sports.

### Supported Language
- Invoke skill:
   - Alexa, start sports checker.
- Enter a sport section:
   - {sport}
- Search for past match information:
   - Recent/Past {n} matches
   - Recent/Past {n} games
   - Recent/Latest match
   - Recent/Latest game
- Search for future match information:
   - Coming/Future {n} matches
   - Coming/Future {n} games
   - Coming/Future match
   - Coming/Future game
- Search match information on a specific date:
   - Match/Game on {date}
   - {date} (recommanded)

### Supported Sports
| Sport |
| -- |
| Baseball |
| Football |
| Men's Basketball |
| Men's Croos Country |
| Men's Golf |
| Men's Gymnastics |
| Men's Tennis |
| Men's Track & Field |
| Soccer |
| Softball |
| Swimming & Diving |
| Volleyball |
| Women's Basketball |
| Women's Cross Country |
| Women's Golf |
| Women's Gymnastics |
| Women's Tennis |
| Women's Track & Firld |
| Wrestling |

## CUMTD
This skill is designed for device deployed at bus stop around the campus of the University of Illinois at Urbana Champaign. It provides user with routes, buses and itineraries information.

### Supported Language
- Invoke skill:
   - Alexa, start bus checker.
- Get stop name:
   - Which stop is this.
   - Tell me the stop.
   - Where am I.
   - Stop name.
- Get route on service today:
   - What lines go through this stop.
   - What routes go through this stop.
   - Tell me the routes.
   - Tell me the lines.
   - Route(s) on service.
   - Route(s)
- Get route on service by date:
   - Will bus/line {route ID} on service (on) {date}.
   - Whether bus/line {route ID} will be on service (on) {date}.
- Get remaining waiting time for a route:
   - When will/does bus/line {route ID} come.
- Get planned trip for a destination:
   - How to go do {destination stop name}.

### Note
- The code is hard coded to bus stop at County Market (E Stoughton & 4th St).
- User should use exact stop name to get a planned trip.

## Course Information
## Wireless Information

## Developers
[Wang Jikun](https://github.com/WagJK) - Dining info, library info, staff info <br>
[Feng Xiyang](https://github.com/andyfengHKU) - EWS usage, sports schedule, CUMTD <br>
[Xie Yuren](https://github.com/xyrng) - Course info <br>
[Liu LingHsi](https://github.com/andyfengHKU) - Wireless info <br>

## Disclaimer
This project is initially developed by Student Innovation Lab of TechService of the University of Illinois at Urbana-Champaign.

[travis-url]: https://travis-ci.org/WagJK/alexa-uiuc
[travis-image]: https://travis-ci.org/WagJK/alexa-uiuc.svg?branch=master
