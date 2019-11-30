# Konsum
Strichlisten Application im Fablab Karlsruhe. WIP

### Vorrausetzungen

Datenbank zum Speichern von den Konsumdaten  
sqlalchemy um Konsumdaten zu lesen oder zu schreiben  
termcolor für so farbigen Konsolen fu  
Display um zeugs zu sehen  
Getränketastatur  
Kobold zur Verwaltung des Goldspeichers

### Installation

  * pip3 install -r requirements.txt

  * mariadb-server installieren und user einrichten
  * datenbank schema importieren

```
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
‖                                                  logged in:  David                                                  ‖
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

 verfügbare Konsumgüter                                                    Konsumkorb [7.7]:

  0: 0.10 Gold einzahlen  10: Becks                20:                      4x Fritz Cola          
  1: 1 Gold einzahlen     11: Rothaus              21:                      6x Krümel              
  2: 10 Gold einzahlen    12: Krümel               22:                     
  3: Premium Cola         13: Kaka                 23:                     
  4: Premium Fanta        14: Geschirr             24:                     
  5: Fritz Cola           15: Lukas3               25:                     
  6: Fritz Orange         16:                      26:                     
  7: Fritz Pfirsich       17:                      27:                     
  8: Fritz Apfel          18:                      28:                     
  9: Warsteiner           19:                      29:                     

 Info: Konsumgut 12 hinzugefügt
 Input: 12

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 letzter Kuhhandel: vorgestern 1x Getränke, 2x Süßkram für  22.22€
 dein Goldspeicher: 13.37€  | AVG: 23.42€ day 2.0€ week 23.2€ month
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
```
