// mongoDb init script to populate cinematch (execute once thanks to mongo_data in yml)
// pass to "cinematch" database (created if not existent)
db = db.getSiblingDB('cinematch');

// ##############################################
// #                 FILM                        #
// ##############################################
db.films.insertMany([
  { _id: ObjectId("69207cbb8023c7de1f32a03c"), id: 1, titolo: '28 Years Later', stelle: 0, regista: 'Danny Boyle', uscita: '2025', genere: 'Horror', immagine: 'images/28-Years-Later.jpg', trama: "Il sequel della saga zombie ambientato 28 anni dopo l'epidemia originale." },
  { _id: ObjectId("69207cbb8023c7de1f32a03d"), id: 2, titolo: 'Arrival', stelle: 0, regista: 'Denis Villeneuve', uscita: '2016', genere: 'Fantascienza', immagine: 'images/arrival.jpg', trama: 'Una linguista viene reclutata per comunicare con misteriosi alieni atterrati sulla Terra.' },
  { _id: ObjectId("69207cbb8023c7de1f32a03e"), id: 3, titolo: 'Big Hero 6', stelle: 0, regista: 'Don Hall', uscita: '2014', genere: 'Animazione', immagine: 'images/big-hero-6.jpeg', trama: 'Un giovane genio e il suo robot Baymax formano una squadra di supereroi.' },
  { _id: ObjectId("69207cbb8023c7de1f32a05d"), id: 4, titolo: 'Your Name', stelle: 0, regista: 'Makoto Shinkai', uscita: '2016', genere: 'Animazione', immagine: 'images/your-name.jpg', trama: 'Due adolescenti scoprono di scambiarsi i corpi in modo misterioso e cercano di incontrarsi.' },
  { _id: ObjectId("69207cbb8023c7de1f32a040"), id: 5, titolo: 'Blade Runner 2049', stelle: 0, regista: 'Denis Villeneuve', uscita: '2017', genere: 'Fantascienza', immagine: 'images/bladerunner2049.jpg', trama: "Un blade runner scopre un segreto che potrebbe cambiare il futuro dell'umanità." },
  { _id: ObjectId("69207cbb8023c7de1f32a041"), id: 6, titolo: 'Coco', stelle: 0, regista: 'Lee Unkrich', uscita: '2017', genere: 'Animazione', immagine: 'images/coco.jpg', trama: 'Un ragazzo appassionato di musica intraprende un viaggio nel mondo dei morti per scoprire la sua famiglia.' },
  { _id: ObjectId("69207cbb8023c7de1f32a042"), id: 7, titolo: 'The Dark Knight', stelle: 0, regista: 'Christopher Nolan', uscita: '2008', genere: 'Azione', immagine: 'images/dark-knight.jpg', trama: "Batman affronta il Joker in una battaglia per l'anima di Gotham City." },
  { _id: ObjectId("69207cbb8023c7de1f32a043"), id: 8, titolo: 'Dune', stelle: 0, regista: 'Denis Villeneuve', uscita: '2021', genere: 'Fantascienza', immagine: 'images/dune.jpg', trama: 'Paul Atreides intraprende un viaggio epico sul pianeta desertico Arrakis.' },
  { _id: ObjectId("69207cbb8023c7de1f32a044"), id: 9, titolo: 'Elio', stelle: 0, regista: 'Adrian Molina', uscita: '2025', genere: 'Animazione', immagine: 'images/elio.jpg', trama: "Un ragazzo viene scambiato per l'ambasciatore della Terra da esseri alieni." },
  { _id: ObjectId("69207cbb8023c7de1f32a045"), id: 10, titolo: 'Finding Nemo', stelle: 0, regista: 'Andrew Stanton', uscita: '2003', genere: 'Animazione', immagine: 'images/finding-nemo.jpg', trama: "Un pesce pagliaccio attraversa l'oceano per ritrovare suo figlio Nemo." },
  { _id: ObjectId("69207cbb8023c7de1f32a046"), id: 11, titolo: 'Frozen', stelle: 0, regista: 'Chris Buck', uscita: '2013', genere: 'Animazione', immagine: 'images/frozen.jpg', trama: 'Due sorelle devono salvare il loro regno da un inverno eterno.' },
  { _id: ObjectId("69207cbb8023c7de1f32a047"), id: 12, titolo: 'Gladiator', stelle: 0, regista: 'Ridley Scott', uscita: '2000', genere: 'Azione', immagine: 'images/gladiator.jpg', trama: "Un generale romano tradito cerca vendetta come gladiatore nell'arena." },
  { _id: ObjectId("69207cbb8023c7de1f32a048"), id: 13, titolo: 'Guardians of the Galaxy', stelle: 0, regista: 'James Gunn', uscita: '2014', genere: 'Azione', immagine: 'images/guardians.jpg', trama: 'Un gruppo di disadattati cosmici deve salvare la galassia da una minaccia mortale.' },
  { _id: ObjectId("69207cbb8023c7de1f32a049"), id: 14, titolo: 'How to Train Your Dragon', stelle: 0, regista: 'Dean DeBlois', uscita: '2010', genere: 'Animazione', immagine: 'images/how-to-train-your-dragon.jpg', trama: 'Un giovane vichingo fa amicizia con un drago, cambiando le regole del suo villaggio.' },
  { _id: ObjectId("69207cbb8023c7de1f32a04a"), id: 15, titolo: 'Inception', stelle: 0, regista: 'Christopher Nolan', uscita: '2010', genere: 'Fantascienza', immagine: 'images/inception.jpg', trama: "Un ladro specializzato nell'estrazione di segreti dai sogni deve compiere l'innesto di un'idea." },
  { _id: ObjectId("69207cbb8023c7de1f32a04b"), id: 16, titolo: 'The Incredibles', stelle: 0, regista: 'Brad Bird', uscita: '2004', genere: 'Animazione', immagine: 'images/incredibles.jpg', trama: 'Una famiglia di supereroi nascosti deve tornare in azione per salvare il mondo.' },
  { _id: ObjectId("69207cbb8023c7de1f32a04c"), id: 17, titolo: 'Inglourious Basterds', stelle: 0, regista: 'Quentin Tarantino', uscita: '2009', genere: 'Azione', immagine: 'images/inglorious-basterds.jpg', trama: 'Un gruppo di soldati ebrei americani semina il terrore tra i nazisti nella Francia occupata.' },
  { _id: ObjectId("69207cbb8023c7de1f32a04d"), id: 18, titolo: 'Inside Out', stelle: 0, regista: 'Pete Docter', uscita: '2015', genere: 'Animazione', immagine: 'images/inside-out.jpg', trama: 'Le emozioni di una ragazzina lottano per aiutarla ad affrontare un grande cambiamento.' },
  { _id: ObjectId("69207cbb8023c7de1f32a04e"), id: 19, titolo: 'Interstellar', stelle: 0, regista: 'Christopher Nolan', uscita: '2014', genere: 'Fantascienza', immagine: 'images/interstellar.jpg', trama: "Un gruppo di esploratori viaggia attraverso un wormhole per salvare l'umanità." },
  { _id: ObjectId("69207cbb8023c7de1f32a04f"), id: 20, titolo: 'Kubo and the Two Strings', stelle: 0, regista: 'Travis Knight', uscita: '2016', genere: 'Animazione', immagine: 'images/kubo.jpg', trama: "Un giovane narratore deve trovare un'armatura leggendaria per sconfiggere uno spirito vendicativo." },
  { _id: ObjectId("69207cbb8023c7de1f32a050"), id: 21, titolo: 'The Lion King', stelle: 0, regista: 'Roger Allers', uscita: '1994', genere: 'Animazione', immagine: 'images/lion-king.jpg', trama: 'Un giovane leone deve reclamare il suo posto come re della savana.' },
  { _id: ObjectId("69207cbb8023c7de1f32a051"), id: 22, titolo: 'Mad Max: Fury Road', stelle: 0, regista: 'George Miller', uscita: '2015', genere: 'Azione', immagine: 'images/madmax.jpg', trama: 'In un mondo post-apocalittico, una donna ribelle cerca la libertà attraverso il deserto.' },
  { _id: ObjectId("69207cbb8023c7de1f32a052"), id: 23, titolo: 'The Martian', stelle: 0, regista: 'Ridley Scott', uscita: '2015', genere: 'Fantascienza', immagine: 'images/martian.jpg', trama: 'Un astronauta abbandonato su Marte deve sopravvivere in attesa dei soccorsi.' },
  { _id: ObjectId("69207cbb8023c7de1f32a053"), id: 24, titolo: 'The Matrix', stelle: 0, regista: 'Lana Wachowski', uscita: '1999', genere: 'Fantascienza', immagine: 'images/matrix.jpg', trama: 'Un hacker scopre che la realtà è una simulazione controllata dalle macchine.' },
  { _id: ObjectId("69207cbb8023c7de1f32a054"), id: 25, titolo: 'Monsters, Inc.', stelle: 0, regista: 'Pete Docter', uscita: '2001', genere: 'Animazione', immagine: 'images/monsters-inc.jpg', trama: 'Due mostri scoprono che le risate dei bambini sono più potenti delle urla.' },
  { _id: ObjectId("69207cbb8023c7de1f32a055"), id: 26, titolo: 'My Hero Academia: Rising', stelle: 0, regista: 'Kenji Nagasaki', uscita: '2019', genere: 'Animazione', immagine: 'images/myheroacademia-rising.jpg', trama: 'La classe 1-A affronta una nuova minaccia mentre si preparano al festival culturale.' },
  { _id: ObjectId("69207cbb8023c7de1f32a056"), id: 27, titolo: 'Pulp Fiction', stelle: 0, regista: 'Quentin Tarantino', uscita: '1994', genere: 'Thriller', immagine: 'images/pulp-fiction.jpg', trama: 'Le vite di criminali di Los Angeles si intrecciano in storie di violenza e redenzione.' },
  { _id: ObjectId("69207cbb8023c7de1f32a057"), id: 28, titolo: 'Ratatouille', stelle: 0, regista: 'Brad Bird', uscita: '2007', genere: 'Animazione', immagine: 'images/ratatouille.jpg', trama: 'Un topo con il sogno di diventare chef si allea con un giovane cuoco a Parigi.' },
  { _id: ObjectId("69207cbb8023c7de1f32a058"), id: 29, titolo: 'Real Steel', stelle: 0, regista: 'Shawn Levy', uscita: '2011', genere: 'Azione', immagine: 'images/real-steel.jpg', trama: "Un ex pugile e suo figlio costruiscono un robot da combattimento per competere nell'arena." },
  { _id: ObjectId("69207cbb8023c7de1f32a059"), id: 30, titolo: 'Sorry Baby', stelle: 0, regista: 'Eva Victor', uscita: '2025', genere: 'Drammatico', immagine: 'images/sorry-baby.jpg', trama: 'Una donna affronta il suo passato traumatico cercando giustizia e guarigione.' },
  { _id: ObjectId("69207cbb8023c7de1f32a05a"), id: 31, titolo: 'Spirited Away', stelle: 0, regista: 'Hayao Miyazaki', uscita: '2001', genere: 'Animazione', immagine: 'images/spirited-away.jpg', trama: 'Una ragazza entra in un mondo magico per salvare i suoi genitori trasformati in maiali.' },
  { _id: ObjectId("69207cbb8023c7de1f32a05b"), id: 32, titolo: 'Tenet', stelle: 0, regista: 'Christopher Nolan', uscita: '2020', genere: 'Fantascienza', immagine: 'images/tenet.jpg', trama: 'Un agente segreto deve manipolare il flusso del tempo per prevenire la Terza Guerra Mondiale.' },
  { _id: ObjectId("69207cbb8023c7de1f32a05c"), id: 33, titolo: 'Toy Story', stelle: 0, regista: 'John Lasseter', uscita: '1995', genere: 'Animazione', immagine: 'images/toy-story.jpg', trama: "I giocattoli di un bambino prendono vita e affrontano la gelosia e l'amicizia." }
]);

// ##############################################
// #                  UTENTI                      #
// ##############################################
db.utenti.insertMany([
  {
    _id: ObjectId("692080526d5043ce82a7b6c0"),
    username: "emanuele",
    email: "emanuele@gmail.com",
    password: "scrypt:32768:8:1$fkN15sVjKE9pu11g$4aa706565bdae989c3c689e39afaec2b303af6f06450a1ceee6f9f769111b9f18d6a0bf6844d2460772030049d04b288b9c30a9b3d1c3d8ca925a36da9330c6e",
    filmVisti: [
      { film_id: ObjectId("69207cbb8023c7de1f32a03c"), voto: 4, stato: "visto", recensione: "Thriller mozzafiato, atmosfera intensa." },
      { film_id: ObjectId("69207cbb8023c7de1f32a03d"), voto: 4, stato: "visto", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a042"), voto: 5, stato: "visto", recensione: "Capolavoro di azione e regia." },
      { film_id: ObjectId("69207cbb8023c7de1f32a043"), voto: 4, stato: "visto", recensione: "Ottimo sviluppo dei personaggi." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04a"), voto: 3, stato: "visto", recensione: "Divertente ma con qualche lentezza." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04e"), voto: 3, stato: "visto", recensione: "Buona idea di fondo, finale prevedibile." },
      { film_id: ObjectId("69207cbb8023c7de1f32a051"), voto: 4, stato: "visto", recensione: "Grande suspense e ritmo incalzante." },
      { film_id: ObjectId("69207cbb8023c7de1f32a052"), voto: 3, stato: "visto", recensione: "Discreto ma non memorabile." },
      { film_id: ObjectId("69207cbb8023c7de1f32a053"), voto: 2, stato: "visto", recensione: "Non ha soddisfatto le aspettative." },
      { film_id: ObjectId("69207cbb8023c7de1f32a056"), voto: 3, stato: "visto", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a05b"), voto: 1, stato: "visto", recensione: "Deludente, trama confusa." },
      { film_id: ObjectId("69207cbb8023c7de1f32a047"), voto: 2, stato: "visto", recensione: "Qualche scena memorabile ma poco altro." },
      { film_id: ObjectId("69207cbb8023c7de1f32a048"), voto: 3, stato: "visto", recensione: "Simpatica avventura, semplice ma efficace." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04c"), voto: 4, stato: "visto", recensione: "Ottimi effetti speciali." },
      { film_id: ObjectId("69207cbb8023c7de1f32a058"), voto: 0, stato: "da vedere", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a045"), voto: 0, stato: "da vedere", recensione: "Ho sentito recensioni positive, voglio confermare." },
      { film_id: ObjectId("69207cbb8023c7de1f32a040"), voto: 5, stato: "visto", recensione: "Fantastico, visivamente incredibile." },
      { film_id: ObjectId("69207cbb8023c7de1f32a041"), voto: 0, stato: "da vedere", recensione: "Sembra una storia commovente." }
    ]
  },
  {
    _id: ObjectId("6920805c6d5043ce82a7b6c1"),
    username: "marco",
    email: "marco@gmail.com",
    password: "scrypt:32768:8:1$i5cFlyJPdnbUyID2$020c4d3c4bbdcef5801c6c3faec76d86fcd6d596b9e356d2e84a15cd3a6c33ee0378bc944e1a0b0febdb30d2eed828ecb55b2bbafeb4c7909690a7dca634ee60",
    filmVisti: [
      { film_id: ObjectId("69207cbb8023c7de1f32a042"), voto: 1, stato: "visto", recensione: "Non il mio genere ma valido." },
      { film_id: ObjectId("69207cbb8023c7de1f32a053"), voto: 3, stato: "visto", recensione: "Discreto, niente di speciale." },
      { film_id: ObjectId("69207cbb8023c7de1f32a056"), voto: 2, stato: "visto", recensione: "Un po' lento ma interessante." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04a"), voto: 2, stato: "visto", recensione: "Avventura carina ma breve." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04e"), voto: 4, stato: "visto", recensione: "Molto divertente." },
      { film_id: ObjectId("69207cbb8023c7de1f32a05b"), voto: 3, stato: "visto", recensione: "Buon ritmo, finale soddisfacente." },
      { film_id: ObjectId("69207cbb8023c7de1f32a043"), voto: 0, stato: "da vedere", recensione: "Sembra epico, non vedo l'ora." },
      { film_id: ObjectId("69207cbb8023c7de1f32a040"), voto: 0, stato: "da vedere", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a052"), voto: 0, stato: "da vedere", recensione: "Ho letto ottime recensioni." },
      { film_id: ObjectId("69207cbb8023c7de1f32a051"), voto: 0, stato: "da vedere", recensione: "Apparentemente spettacolare." }
    ]
  },
  {
    _id: ObjectId("692080686d5043ce82a7b6c2"),
    username: "sara",
    email: "sara@gmail.com",
    password: "scrypt:32768:8:1$iKm6EsQLSsqpPqFC$07ceaa27515ed6de4dbca8bce0a2d0b28f39a00b5a67938e8b8f430b1feb437adb034e900323f66b36b35a32ea276765fc1bf0a16bee08a39716f6ddd278f1f0",
    filmVisti: [
      { film_id: ObjectId("69207cbb8023c7de1f32a041"), voto: 4, stato: "visto", recensione: "Molto emozionante." },
      { film_id: ObjectId("69207cbb8023c7de1f32a045"), voto: 4, stato: "visto", recensione: "Storia intensa, bella animazione." },
      { film_id: ObjectId("69207cbb8023c7de1f32a046"), voto: 2, stato: "visto", recensione: "Carino ma non memorabile." },
      { film_id: ObjectId("69207cbb8023c7de1f32a049"), voto: 2, stato: "visto", recensione: "Animazione bella, trama leggera." },
      { film_id: ObjectId("69207cbb8023c7de1f32a04d"), voto: 5, stato: "visto", recensione: "Assolutamente da vedere!" },
      { film_id: ObjectId("69207cbb8023c7de1f32a050"), voto: 5, stato: "visto", recensione: "Mi ha fatto emozionare molto." },
      { film_id: ObjectId("69207cbb8023c7de1f32a054"), voto: 0, stato: "da vedere", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a057"), voto: 0, stato: "da vedere", recensione: "Non vedo l'ora di guardarlo!" },
      { film_id: ObjectId("69207cbb8023c7de1f32a05a"), voto: 0, stato: "da vedere", recensione: "" },
      { film_id: ObjectId("69207cbb8023c7de1f32a05c"), voto: 0, stato: "da vedere", recensione: "Apparentemente molto interessante." }
    ]
  }
]);
