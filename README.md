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
Below are the supported phrases to use this skill:
- Invoking Skill: Alexa, start menu checker
...
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
## Staff Information
## Lab Usage
This skill provides user with computer usage information in EWS labs, ICS labs and residence halls in the campus of the University of Illinois at Urbana-Champaign.
### User Guide
- Invoking skill
>> Alexa, start lab checker.
- Quick search for engineering workstation: Find me a (engineering) workstation.
- Quick search for general use computer: Find me a lab.
### Supported labs/buildings
| EWS Buildings | Supported Names | Supported Rooms |
| --------- | --------------- | --------------- |
| Digital Computer Laboratory | Digital Computer Laboratory (Lab), DCL | 416, 426, 440, 520 |
| Electrical and Computer Engineering Building | Electrical and Computer Engineering Building, ECE Building, ECEB, ECE | 2022, 3022, 3070|
| Engineering Hall | Engineering Hall, EH | 406(B)1, 406(B)8 |
| Grainger Engineering Library | Grainger (Engineering) Library, Grainger, GELIB | 4th floor center, 4th floor east |
| Mechanical Engineering Library | Mechanical Engineering Laboratory (Lab), Mechanical Lab, MEL | 1001, 1009 |
| Siebel Center | Siebel Center, Sieble, SIEBL | (0)218, (0)220, (0)222, (0)403 |
| Transportation Building | Transportation Building, TB | 207, 302, 316 |

| Buildings | Supported Names |
| --------- | --------------- |
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
## CUMTD
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
