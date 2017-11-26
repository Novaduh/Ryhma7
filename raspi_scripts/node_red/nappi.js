/* Tämä koodi laskee painikkeiden painallusten määrän. Koodi hakee liitetystä teksti tiedostosta arvon ja lisää siihen yhden lisään, 
joka painalluksella.*/
var count = context.get('Arvo')||0; //Haetaan arvo teksti tiedostosta
count += 1;                         //Lisätään saatuun arvoon yksi lisää
context.set('Arvo',count);          //Tallennetaan uusi arvo takaisin tiedostoon
msg.count = count;                  //Asetetaan uusi arvo Node-rediin tarkasteltavaksi
msg.payload = count;                
return msg;
