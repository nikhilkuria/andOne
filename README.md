# andOne

#### Set up and Installation
TODO

#### Commands

andOne supports the following commands

##### Team

###### Roster

`team roster <team name>`

```
team roster gsw
team roster atlanta
team roster houston
```

`<team name>`

Can be any of the following

* City name
  - `Houston, Dallas, Boston`
* Franchise name
  - `Lakers, Warriors`
* Code of a Team
  - `OKC, CLE`

![Alt Text](https://media.giphy.com/media/WwZgsK4LcH3BllPK0Y/giphy.gif)

##### Player

###### Year On Year

`player year-on-year <player name> <stat-names>`

```
player year-on-year "Paul George"
player year-on-year "Russel Westbrook" stat-names=["AVG TURNOVERS"]
```

`<player name>`

Should be the first name followed by the last
ex : Paul George, Russel Westbrook

`<stat-names>`

This is optional. If this field is left blank, all the stats will be displayed.

You can choose a subset of the available stats

* GAMES PLAYED
* GAMES STARTED
* MINUTES
* AVG POINTS
* AVG ASSISTS
* AVG REBOUNDS
* AVG STEALS
* AVG BLOCKS
* AVG TURNOVERS
* AVG PERSONAL FOULS

ex : ["AVG PERSONAL FOULS", "AVG BLOCKS"]

![Alt Text](https://media.giphy.com/media/EEzGzZhpGF6Ktewc45/giphy.gif)
