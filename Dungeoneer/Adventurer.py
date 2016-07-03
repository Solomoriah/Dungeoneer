# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2012 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import string, random
import Spells, Dice

# *******************************************************************************************************
# Table Definitions

# character classes are often represented as indexes
# 0 = cleric, 1 = fighter, 2 = magic-user, 3 = thief
classnames = ( "Cleric", "Fighter", "Magic-User", "Thief" )
primes = [ 2, 0, 1, 3 ]
statnames = (
    ( "STR", "Strength" ),
    ( "INT", "Intelligence" ),
    ( "WIS", "Wisdom" ),
    ( "DEX", "Dexterity" ),
    ( "CON", "Constitution" ),
    ( "CHR", "Charisma" ),
)

levels = (
    ( 0, 0, 0, 0 ),
    ( 1, 1, 1, 1 ),
    ( 2, 2, 1, 2 ),
    ( 3, 3, 2, 3 ),
    ( 4, 4, 3, 4 ),
    ( 5, 5, 4, 5 ),
    ( 6, 6, 5, 6 ),
    ( 7, 7, 6, 7 ),
    ( 8, 8, 7, 8 ),
    ( 9, 9, 8, 10 ),
    ( 11, 10, 9, 11 ),
)

# names are courtesy of the Dragonsfoot Book of Names available from www.dragonsfoot.org

names = ( "A'kk", "Aarkosh", "Aarne", "Aazad", "Aban", "Abbad", "Abbas", "Abednego", "Abniki", "Adar",
"Adib", "Adiba", "Adjo", "Aedan", "Aelyina", "Aengus", "Aeron", "Afaf", "Affan", "Afia",
"Afifa", "Afrikaisi", "Agon", "Ahlam", "Ailbe", "Ailill", "Aimo", "Aina", "Aino", "Aisheisha",
"Ajwad", "Akana", "Akaro", "Akhom", "Ako", "Akori", "Akorit", "Alan", "Alauna", "Alazon",
"Albarez", "Alderon", "Aleksanteri", "Aleksi", "Allam", "Allan", "Allanor", "Allsie", "Almas", "Aloli",
"Alopex", "Alquraishi", "Alroy", "Alsheimer", "Alu", "Aluvian", "Alva", "Amaco", "Amahte", "Amal",
"Amaya", "Ambalo", "Amenemhet", "Amenhotep", "Amenitra", "Amir", "Amira", "Amisi", "Ammar", "Amonit",
"Amvalo", "Anbar", "Ancarr", "Andar", "Anden", "Ander", "Andrax", "Andronicus", "Anemro", "Angus",
"Anhamant", "Anhuri", "Anhurit", "Aniq", "Anja", "Ankhesenamen", "Annika", "Annuka", "Anok", "Antar",
"Anu", "Aodhan", "Apoqulis", "Appppil", "Aramath", "Arborius", "Arcan", "Ardan", "Areej", "Arilea",
"Arkadeus", "Arlock", "Armas", "Armo", "Armstrong", "Arn", "Arolian", "Arregala", "Arrowind", "Art",
"Artaxus", "Artimoff", "Arto", "Arttu", "Arturo", "Arvo", "Arwa", "Arwarh", "Ashai", "Ashier",
"Ashraf", "Asif", "Asil", "Asir", "Askari", "Astacoe", "Athar", "Atheos", "Ati", "Auken",
"Aurelio", "Aurora", "Avar", "Avenida", "Aversa", "Awan", "Awi", "Awwab", "Axeblade", "Ayaz",
"Ayham", "Ayman", "Ayrseer", "Azhaar", "Azhar", "Azizah", "Azra", "Azus", "B'yak", "Baariq",
"Baba", "Badr", "Badriya", "Bahia", "Bahija", "Bahja", "Bai", "Baki", "Bakir", "Bakit",
"Bakker", "Bakkon", "Baligha", "Balorik", "Balt", "Banafrit", "Banan", "Banner", "bar'Kazor", "Baraka",
"Bari", "Barirah", "Barit", "Barlathotep", "Barros", "Bartholomer", "Bartleby", "Bartley", "Basha'ir", "Bashasha",
"Bashira", "Basil", "Basim", "Basima", "Bathallas", "Batul", "Baz", "Beatrijs", "bel Callan", "Belladonna",
"belTrajan", "Benipe", "Beorn", "Bergeroi", "Bergethus", "Betuke", "Biddleriggs", "BigPig", "Bilqis", "Bimblebomb",
"Bisi", "Biti", "Bjarnni", "Blackgem", "Blaise", "Blasto", "Blumbo", "Bofur", "Boki", "Bolen",
"Bork", "Bortoka", "Bower", "Bradan", "Brak", "Bral", "Brand", "Branna", "Breandan", "Brecca",
"Brenden", "Briar", "Bronn", "Brovus", "Bubu", "Buckley", "Budur", "Buikhu", "Burdalane", "Burok",
"Bushra", "Bweengar", "Bylo", "Cabhan", "Cabral", "Cadron", "Cagbral", "Calanor", "Cale", "Caledon",
"Calvin/Kalvin", "Canas", "Cander", "Canice", "Carantha", "Cardax", "Cark", "Carnby", "Carney", "Caronal",
"Carrick", "Cartmange", "Castenada", "Cathal", "Cearney", "Cearul", "Cellini", "Cellowyn", "Chadmister", "Chalcis",
"Chambers", "Chanda", "Charduush", "Chlorianna", "Cian", "Ciaran", "Cillian", "Cioffi", "Cirak", "Clarice",
"Clearie", "Climmie", "Clooney", "Clyte", "Coilin", "Coinneach", "Colita", "Colm", "Colmcille", "Colum",
"Columba", "Conan", "Conlaoch", "Conleth", "Connla", "Connor", "Cooley", "Cord", "Cordain", "Corethal",
"Cormac", "Corwin", "Coussan", "Crill", "Crine", "Cronan", "Crow", "Cumberground", "Cuo", "Cuthalion",
"Cybill", "Cynoweth", "Cynthia", "D'Avalon", "D'Haveral", "D'Nav", "Dain", "Dainna", "Daire", "Daithi",
"Dalaigh", "Dalal", "Dalgar", "Dao", "Dar", "Dara", "Darcy", "Dargon", "Darian", "Darius",
"Darkblade", "Daro", "Davanir", "Davin", "de Vries", "Deaglan", "Deathbreaker", "Delvalle", "Den", "Denari",
"denCadal", "Dendro", "Derbren", "Dergo", "Derik", "Dern", "Derry", "Dertucken", "Derwin", "Desmond",
"Devon", "Dholgir", "Dhonjen", "Diarmuid", "Diggins", "Dillon", "Din", "Dinoia", "Diwan", "Djabenusiri",
"Djadao", "DjaDja", "Djal", "Djeserit", "Donal", "Donar", "Donnamira", "Donncha", "Doomis", "Dorian",
"Dracul", "Dragoncrest", "Dragonfang", "Drake", "Drako", "Drashen", "Drithelm", "Drizzen", "Drogo", "Drumble",
"Du'Shkar", "Dubhlain", "Ducky", "Dumystor", "Durriyah", "Duvera", "Dwine", "Dye", "Eamon", "Earth-fast",
"Eastwoods", "Ebe", "Ebio", "Ebonrain", "Ecthelander", "Eero", "Effington", "Eirnin", "Eizenga", "Ekibe",
"Elden", "Elderon", "Eldfather", "Eldmother", "Eljas", "Elvengrond", "Embranglement", "Emmet", "Emu", "Emuishe",
"Enda", "Endil", "Endra", "Endrallion", "Ennis", "Enoch", "Ensio", "Eoghan", "Eohyl", "Eoras",
"Ephrata", "Erikmund", "Erkki", "Erno", "Eron", "Escrill", "Esho", "Esperanza", "Eujue", "Evenhood",
"Faber", "Fadwa", "Faelon", "Faiq", "Faiqa", "Faiza", "Fakih", "Faldren", "Fante", "Faolan",
"Faqih", "Farah", "Fargon", "Farha", "Faryal", "Fatema", "Fatih", "Faustimagus", "Feidhelm", "Felga",
"Fellbottom", "Felth", "Fen", "Feng", "Fengaris", "Fenix", "Ferdia", "Fergal", "Fergus", "Feringald",
"Fernelius", "Fero", "Finbar", "Finister", "Fintan", "Fionn", "Firdaus", "Flade", "Fleabo", "Forge",
"Forswunk", "Foutch", "Foxglove", "Frans", "Fredrik", "Frits", "Frizzle", "Furbottom", "Gabryl", "Galadhremin",
"Galadin", "Galahra", "Galyn", "Garag", "Gatlin", "Gautreau", "Gearoid", "Gedreka", "Gegor", "Geledeth",
"Germariliz", "Gerronalyde", "Ghada", "Ghunwah", "Gimbalim", "Gino", "Girn", "Glafira", "Glendon", "Gloramir",
"Goldenstaff", "Gore", "Goreic", "Gou", "Gowl", "Grandy", "Grantier", "Grasseyes", "Graveolent", "Greenleaf",
"Greensmith", "Greyforn", "Griff", "Grilloch", "Grog", "Grom", "Grond", "Gronnon", "Gruel", "Guilbeau",
"Gull", "Gulliver", "Gulnar", "Gurek", "Gwynhynyr", "Haaver", "Hafgar", "Hafsa", "Hagatha", "Haidar",
"Haitham", "Hajar", "Haji", "Halden", "Hallden", "Hamdan", "Hamu", "Hamza", "Hannes", "Hannu",
"Hardel", "Hare", "Harg", "Hariz", "Harri", "Hasan", "Hashim", "Havard", "Hawk", "Hawkeye",
"Hawwa", "Healingwinds", "Heath", "Hebony", "Hehepsit", "Hehepsu", "Heikki", "Heino", "Helka", "Hella",
"Hellspike", "Helmi", "Helo-os", "Hemlock", "Henk", "Henriikka", "Henrikki", "Henry", "Hermanni", "Hermiston",
"Hesekiel", "Highpocket", "Hildron", "Hilja", "Hillevi", "Hime", "Hind", "Hiplak", "Hisham", "Hiunelray",
"Hoelzel", "Hortenberry", "Hrog", "Hugh", "Huiley", "Humam", "Huriya", "Husain", "Husna", "Iabi",
"Ialu", "Ibenre", "Ibon", "Ibtihaj", "Ibtihal", "Ibtisam", "Iffat", "Iika", "Iines", "Iiro",
"Iisakki", "Ilham", "Iliff", "Illmillio", "Ilmari", "Ilona", "Ilse", "Ilthmier", "Ilusia", "Imad",
"Impi", "Inas", "Indira", "Inka", "Inkeri", "Intisar", "Iollan", "Iqbal", "Irisi", "Irja",
"Irma", "Ironhead", "Ironshield", "Isam", "Ishraq", "Islemount", "Ismo", "Itafe", "Itennu", "Ithimar",
"Itidal", "Itimad", "Itran", "Izlldorf", "Jaakko", "Jacob", "Jadren", "Jalal", "Jalmari", "Jamal",
"Jamil", "Jamila", "Jan", "Jang", "Janisak", "Janna", "Jansen", "Jari", "Jarlath", "Jasim",
"Jasmin", "Jawhara", "Jawwad", "Jax", "Jelanie", "Jesper", "Jolosh", "Jonathon", "Joonas", "Jorgos",
"Jos", "Joszef", "Joth", "Jouko", "Juha", "Jukka", "Juleis", "Justin", "Juwairiyah", "Jyri",
"Kahotep", "Kai", "Kaija", "Kalevi", "Kalle", "Kalythalas", "Kamenwati", "Kamil", "Kamila", "Kappo",
"Kargas", "Karjos", "Karn", "Karva", "Kauko", "Kaur", "Kausar", "Kazatelli", "Kchime", "Kebi",
"Kegroller", "Kellin", "Kelp", "Kemamonit", "Kemisi", "Kemnebi", "Kemosiri", "Kemreit", "Kemsa", "Kemse",
"Ken", "Kensen", "Kepi", "Kerning", "Kerttu", "Kettwig", "Kevan", "Khadeeja", "Khai", "Khait",
"Khansa", "Khawlah", "Khenti", "Khurin", "Kiara", "Kifi", "Kijoran", "Kimmin", "Kino", "Kiwu",
"Koebel", "Kohout", "Korben", "Kordon", "Korr", "Korrin", "Korvola", "Kothar", "Kratel", "Kray",
"Kremble", "Krezak", "Krimdabar", "Krisella", "Kristian", "Kryllan", "Kufu", "Kurbis", "Kyron", "Labib",
"Lacayan", "Lagramar", "Laila", "Laith", "Lalonde", "Lanasa", "Lanaxis", "Lance", "Lanefan", "Lanken",
"Lapierre", "Larilyne", "Laris", "Larn", "Lars", "Lasherr", "Lathan", "Laulunen", "Lee", "LeMoore",
"Lempi", "Leonidas", "Lerone", "Lerrad", "Lexington", "Liam", "Lilly", "Linden", "Linke", "Llkuth",
"Lochlan", "Logan", "Lohann", "Londenberg", "Longfoot", "Lonth", "Lorak", "Lorcan", "Lorendal", "Lottinville",
"Lucien", "Lugrom", "Lulua", "Lupinus", "Lynesius", "Lyssa", "Ma'ali", "Maarit", "Macabranse", "Macayan",
"Machette", "Magness", "Magnus", "Mahasin", "Mahdi", "Maimbled", "Maimuna", "Mainio", "Mais", "Maisa",
"Maisara", "Maisun", "Makar", "Makarim", "Malachi", "Malak", "Malaki", "Malcom", "Malika", "Maliki",
"Malise", "Malison", "Mammix", "Manal", "Manar", "Mandrax", "Mansur", "Manu", "Maram", "Marcus",
"Mariha", "Marillia", "Marja", "Marjaana", "Marjami", "Marjo", "Marjukka", "Marko", "Marlez", "Martti",
"Marvene", "Marwan", "Marya", "Maryam", "Masquit", "Matias", "Mauri", "Mawahib", "Maxamillion", "Maximus",
"Mayesa", "Maynard", "Mayovsky", "McElreath", "Mclimans", "Mdjai", "Mede", "Meelath", "Megaron", "Mehnit",
"Meldros", "Melkiresha", "Melodra", "Melum", "Menetnashte", "Meri", "Merit", "Meskenit", "Mesmer", "Meti",
"Metit", "Mhotep", "Mie", "Mika", "Mikael", "Mikko", "Ming", "Miradonna", "Miranda", "Miu",
"Mkalbuti", "Mkhai", "Mkhait", "Mkit", "Mkitiris", "Mnoti", "Moffle", "Mogrim", "Mohot", "Moonthorn",
"Mophat", "Mor", "Moreno", "Morg", "Morganish", "Moricantu", "Mosha", "Mosto", "Mshai", "Mtidja",
"Muaz", "Mume", "Muna", "Muniba", "Munira", "Munsif", "Muntasir", "Muntuhotep", "Murad", "Murtagh",
"Muslih", "Myr", "Nadar", "Nafre", "Nafretiri", "Nafretiti", "Nafrini", "Nafrit", "Nail", "Nane",
"Nanu", "Nardak", "Nathan", "Nazar", "Neal", "Neb", "Nebi", "Nebibi", "Nebibit", "Nebit",
"Nebt", "Nebtawi", "Nebti", "Neckritz", "Nehru", "Nel", "Neomund", "Neshmal", "Nevara", "Nevin",
"Nex", "Niall", "Niamh", "Nieto", "Nifen-Ankh", "Niina", "Niko", "Nildhevin", "Nimblefingers", "Nivek",
"Nodo", "Nofrotete", "Nollaig", "Nomti", "Northcrosse", "Nsu", "Nubi", "Nubit", "Nubiti", "Oakshield",
"Oakworthy", "Oba", "Occosleus", "Odhran", "Odji", "Odjit", "Ogg", "Ogunyli", "Oillyan", "Oisin",
"Oiva", "Olavi", "Onni", "Onyg", "Or", "Oran", "Orian", "Orin", "Orvokki", "Orzo",
"Oshairana", "Oskari", "Osmund", "Otto", "Oweyn", "Owyn", "Paavo", "Padraic", "Pallenstein", "Palz",
"Panahasi", "Paniwi", "Pantego", "Paranor", "Parrino", "Passel", "Peadar", "Pearse", "Pekka", "Penguin",
"Pete", "Petra", "Petri", "Phelp", "Phi", "Phillip", "Phireal", "Pirkko", "Plaisance", "Pollari",
"Popehn", "Porphyriel", "Proinsias", "Ptermtec", "Quaddy", "Que'flnrnl", "Queachy", "Quellius", "Queq", "Quickfoot",
"Quicksword", "Quinlan", "Quinlivan", "Raakel", "Radiant", "Radivarl", "Radugish", "Rae", "Rael", "Raeneriac",
"Ragnar", "Raimo", "Rakeisha", "Ralus", "Ramfthar", "Rami", "Rasilitip", "Rasui", "Rath", "Rathwynn",
"Ravenzen", "Redmond", "Redwood", "Reino", "Reko", "Relentine", "Rellellalora", "Relmorak", "Remmao", "Renaldo",
"Renger", "Ressinfyr", "Revlis", "Revum", "Riika", "Rikard", "Rikhard", "Riley", "Rimsa", "Rimson",
"Rindle", "Ristan", "Risto", "Riveness", "Robideau", "Rockthorn", "Rodedaugh", "Rodger", "Rogan", "Roma",
"Romali", "Ronan", "Rondor", "Rooks", "Roope", "Roth", "Rourke", "Ruari", "Ruuben", "Ryfilke",
"Sabber", "Sabe", "Sadji", "Sadric", "Saini", "Sakari", "Sakke", "Salidji", "Salomon", "Sampson",
"Sancherok", "Sanieqwa", "Santtu", "Sari", "Saris", "Sarpkin", "Saugus", "Saul", "Sautner", "Savanna",
"Savic", "Scales", "Seafi", "Seafoam", "Seamus", "Sean", "Sebi", "Seini", "Selene", "Semni",
"Senja", "Seppo", "Sera", "Serella", "Serioge", "Seti", "Severi", "Severn", "Shadrach", "Shai",
"Shai-nefer", "Shalam", "Shambla", "Shamise", "Shantefeire", "Sharana", "Sharshell", "Shashaiti", "She", "Shea",
"Sheba", "Shebi", "Shel'lecryn", "Shelanier", "Shemeit", "Sheni", "Shenti", "Shepsit", "Sheriti", "Shinicle",
"Sho", "Shobog", "Shoshana", "Shun", "Shushu", "Silbach", "Silja", "Silverblade", "Silvereye", "Silverleaf",
"Silversword", "Simo", "Simon", "Sinikka", "Sinuhe", "Sinvus", "Sisko", "Sisu", "Skarrakas", "Skaug",
"Skeeth", "Skor", "Skotia", "Skullspitter", "Skyboot", "Slade", "Slaugulond", "Slickbark", "Slimp", "Slone",
"Sloom", "Slyderia", "Smeke", "Snick", "Snugbreeches", "Sohvi", "Soini", "Sokkwi", "Sol", "Solan",
"Solomoriah", "Sothak", "Sparrow", "Spendler", "Spuddle", "Spyrcrist", "Stefan", "Steng", "Stiv", "Stonebrow",
"Stonefist", "Stormraven", "Strall", "Sulumyn", "Suoma", "Suten", "Suvi", "Swiftblade", "Syluz", "Taavetti",
"Taavi", "Tadhg", "Taelin", "Tagledash", "Tahvo", "Taisto", "Talimor", "Tameri", "Tanafriti", "Taneli",
"Tanja", "Tantlinger", "Taralthas", "Taravil", "Targas", "Tarixi", "Tarmo", "Tartaglia", "Tasil", "Tasseldale",
"Tauno", "Teenik", "Tenbar", "Teneyck", "Tennon", "Teodore", "Terger", "Tero", "Terron", "Terrox",
"Teuvo", "Tezzerell", "Thassius", "Thelone", "Thenraine", "Therandili", "Therion", "Thesis", "Thiric", "Thistle",
"Thistletoe", "Thomas", "Thoril", "Thorus", "Thrull", "Thunderhammer", "Thunderhead", "Thundra", "Thye", "Tiankhit",
"Tierney", "Tierza", "Tilbor", "Tinubiti", "Tinythalas", "Titinius", "Toivo", "Toliver", "Tomas", "Tor",
"Torag", "Torlo", "Torsti", "Toupin", "Trenellan", "Tuerezo", "Tular", "Tullamore", "Tuomas", "Tuomo",
"Turgan", "Turgon", "Turlach", "Turlough", "Twight", "Tybrin", "Udjai", "Ultan", "Umlaut", "Unger",
"Unwanted", "Ureel", "Urho", "Urias", "Uriel", "Urndale", "Uro", "Urshe", "Ursula", "Usko",
"Utmebar", "Vaino", "Valmore", "Valterri", "Valto", "Valvinder", "van Veen", "Vanamo", "Vanauken", "Vandel",
"Vandenbossette", "Vanguard", "Varl", "Vasha", "Vaught", "Vectrasik", "Veepo", "Vega", "Veikko", "Velox",
"Venieal", "Verseth", "Vesu", "Victran", "Vidor", "Vilden", "Vilhelmi", "Vilho", "Vilmar", "Vin",
"Voitto", "Vorbutin", "Vortiel", "Voxvax", "Vuokko", "Wakhakwi", "Wakhashem", "Wanderer", "Wat", "Wati",
"Wayland", "Wedfellow", "Weemhoff", "Wendel", "Westra", "Whilehead", "Whingle", "Wiles", "Willow", "Willum",
"Wimbly", "Wixem", "Wofare", "Wolfmoon", "Wolfram", "Wolvenmore", "Woodrider", "Woodrow", "Woserit", "Wrine",
"Wyllymyr", "Wynnich", "Yar", "Yato", "Yazzi", "Ynywyth", "Yrjana", "Yrjo", "Ysbrand", "Yuiel",
"Zaagan", "Zarine", "Zatelli", "Zeuth", "Zilas", "Zinnebor", "Zook", "Zorill", "Zyggy" )

hitdice = (
    ( 6, 1 ),
    ( 8, 2 ),
    ( 4, 1 ),
    ( 4, 2 ),
)

statbonuses = (
    0, 0, 0,
    -3,
    -2, -2,
    -1, -1, -1,
    0, 0, 0, 0,
    1, 1, 1,
    2, 2,
    3
)

meleeweapons = [
    [ 0,
        [ 3, "Warhammer", 1, "1d6" ],
        [ 8, "Mace", 1, "1d8" ],
        [ 1, "Maul", 2, "1d10" ]
    ],
    [ 0,
        [ 2, "Great Axe", 2, "1d10" ],
        [ 7, "Battle Axe", 1, "1d8" ],
        [ 6, "Shortsword", 1, "1d6" ],
        [ 14, "Longsword", 1, "1d8" ],
        [ 2, "Scimitar", 1, "1d8" ],
        [ 2, "Two-Handed Sword", 2, "1d10" ],
        [ 1, "Pole Arm", 2, "1d10" ],
        [ 2, "Spear", 2, "1d6" ]
    ],
    [ 0,
        [ 1, "Dagger", 1, "1d4" ],
        [ 1, "Walking Staff", 2, "1d4" ]
    ],
    [ 0,
        [ 7, "Battle Axe", 1, "1d8" ],
        [ 6, "Shortsword", 1, "1d6" ],
        [ 14, "Longsword", 1, "1d8" ],
        [ 2, "Scimitar", 1, "1d8" ]
    ]
]

meleeweaponbonus = [
    0,
    [ 40, "+1" ],
    [ 10, "+2" ],
    [  5, "+3" ],
    [  2, "+4" ],
    [  1, "+5" ],
    [ 17, "+1, +2 vs. Special Enemy" ],
    [ 10, "+1, +3 vs. Special Enemy" ]
]

armortypes = [
    [ 0,
        [  9, "Leather Armor", 13, 30 ],
        [ 19, "Chain Mail", 15, 20 ],
        [ 15, "Plate Mail", 17, 20 ]
    ],
    [ 0,
        [  9, "Leather Armor", 13, 30 ],
        [ 19, "Chain Mail", 15, 20 ],
        [ 15, "Plate Mail", 17, 20 ]
    ],
    [ 0,
        [  1, "", 11, 40 ]
    ],
    [ 0,
        [  1, "Leather Armor", 13, 30 ]
    ]
]

defaultarmor = [
    [ "Plate Mail", 17, 20 ],
    [ "Plate Mail", 17, 20 ],
    [ "", 11, 40 ],
    [ "Leather Armor", 13, 30 ]
]

armorbonus = [
    0,
    [ 50, 1 ],
    [ 30, 2 ],
    [ 10, 3 ]
]

ringprobonus = [
    0,
    [ 9, 1 ],
    [ 4, 2 ],
    [ 1, 3 ]
]

potiontable = [
    0,
    [ 3, "Clairaudience", -1 ],
    [ 4, "Clairvoyance", -1 ],
    [ 3, "Control Animal", -1 ],
    [ 3, "Control Dragon", -1 ],
    [ 3, "Control Giant", -1 ],
    [ 3, "Control Human", -1 ],
    [ 3, "Control Plant", -1 ],
    [ 3, "Control Undead", -1 ],
    [ 7, "Delusion", -1 ],
    [ 3, "Diminution", -1 ],
    [ 4, "ESP", -1 ],
    [ 4, "Fire Resistance", -1 ],
    [ 4, "Flying", -1 ],
    [ 4, "Gaseous Form", -1 ],
    [ 4, "Giant Strength", -1 ],
    [ 4, "Growth", -1 ],
    [ 4, "Healing", -1 ],
    [ 5, "Heroism", 1 ],
    [ 4, "Invisibility", -1 ],
    [ 4, "Invulnerability", -1 ],
    [ 4, "Levitation", -1 ],
    [ 4, "Longevity", -1 ],
    [ 2, "Poison", -1 ],
    [ 3, "Polymorph Self", -1 ],
    [ 8, "Speed", -1 ],
    [ 3, "Treasure Finding", -1 ]
]

scrolltable = [
    [ 0,
        [  3, (0, 1), ],
        [  3, (0, 2), ],
        [  2, (0, 3), ],
        [  1, (0, 4), ],
        [  5, "Cursed Scroll" ],
        [  6, "Scroll of Protection from Elementals" ],
        [ 10, "Scroll of Protection from Lycanthropes" ],
        [  5, "Scroll of Protection from Magic" ],
        [ 13, "Scroll of Protection from Undead" ],
        [ 10, "Map to Treasure Type A" ],
        [  4, "Map to Treasure Type E" ],
        [  3, "Map to Treasure Type G" ],
        [  8, "Map to 1d4 Magic Items" ]
    ],
    [ 0,
        [  5, "Cursed Scroll" ],
        [  6, "Scroll of Protection from Elementals" ],
        [ 10, "Scroll of Protection from Lycanthropes" ],
        [  5, "Scroll of Protection from Magic" ],
        [ 13, "Scroll of Protection from Undead" ],
        [ 10, "Map to Treasure Type A" ],
        [  4, "Map to Treasure Type E" ],
        [  3, "Map to Treasure Type G" ],
        [  8, "Map to 1d4 Magic Items" ]
    ],
    [ 0,
        [  6, (2, 1), ],
        [  5, (2, 2), ],
        [  5, (2, 3), ],
        [  4, (2, 4), ],
        [  3, (2, 5), ],
        [  2, (2, 6), ],
        [  1, (2, 7), ],
        [  5, "Cursed Scroll" ],
        [  6, "Scroll of Protection from Elementals" ],
        [ 10, "Scroll of Protection from Lycanthropes" ],
        [  5, "Scroll of Protection from Magic" ],
        [ 13, "Scroll of Protection from Undead" ],
        [ 10, "Map to Treasure Type A" ],
        [  4, "Map to Treasure Type E" ],
        [  3, "Map to Treasure Type G" ],
        [  8, "Map to 1d4 Magic Items" ]
    ],
    [ 0,
        [  5, "Cursed Scroll" ],
        [  6, "Scroll of Protection from Elementals" ],
        [ 10, "Scroll of Protection from Lycanthropes" ],
        [  5, "Scroll of Protection from Magic" ],
        [ 13, "Scroll of Protection from Undead" ],
        [ 10, "Map to Treasure Type A" ],
        [  4, "Map to Treasure Type E" ],
        [  3, "Map to Treasure Type G" ],
        [  8, "Map to 1d4 Magic Items" ]
    ]
]

miscmagictable = [
    0,
    [ 4, "Amulet of Proof against Detection and Location" ],
    [ 2, "Bag of Devouring" ],
    [ 6, "Bag of Holding" ],
    [ 5, "Boots of Levitation" ],
    [ 5, "Boots of Speed" ],
    [ 5, "Boots of Traveling and Leaping" ],
    [ 1, "Bowl Commanding Water Elementals" ],
    [ 1, "Brazier Commanding Fire Elementals" ],
    [ 6, "Broom of Flying" ],
    [ 1, "Censer Commanding Air Elementals" ],
    [ 3, "Cloak of Displacement" ],
    [ 4, "Crystal Ball" ],
    [ 2, "Crystal Ball with Clairaudience" ],
    [ 1, "Drums of Panic" ],
    [ 1, "Efreeti Bottle" ],
    [ 7, "Elven Boots" ],
    [ 7, "Elven Cloak" ],
    [ 2, "Flying Carpet" ],
    [ 7, "Gauntlets of Ogre Power" ],
    [ 2, "Girdle of Giant Strength" ],
    [ 6, "Helm of Reading Languages and Magic" ],
    [ 1, "Helm of Telepathy" ],
    [ 1, "Helm of Teleportation" ],
    [ 1, "Horn of Blasting" ],
    [ 9, "Medallion of ESP" ],
    [ 1, "Mirror of Life Trapping" ],
    [ 5, "Rope of Climbing" ],
    [ 3, "Scarab of Protection" ],
    [ 1, "Stone Commanding Earth Elementals" ]
]

# *******************************************************************************************************
# Functions

def makename():
    if Dice.D(1, 100) <= 25:
        # 2 names
        return "%s %s" % (random.choice(names), random.choice(names))
    else:
        # 1 name
        return random.choice(names)

# *******************************************************************************************************
# Object Constructors

class Character:

    def __init__(self, level, clas, actuallevel = 0):

        self.name = makename()
        self.noapp = 1

        self.clas = clas
        self.classname = classnames[self.clas]

        self.spells = None

        self.level = level
        if not actuallevel:
            if Dice.D(1, 100) <= 30:
                self.level = max(Dice.D(1, self.level), Dice.D(1, self.level))
            self.level = levels[self.level][clas]

        self.stats = [
            Dice.D(3, 6), Dice.D(3, 6), Dice.D(3, 6),
            Dice.D(3, 6), Dice.D(3, 6), Dice.D(3, 6)
        ]

        # boost prime if it's not good.
        self.stats[primes[clas]] = max(self.stats[primes[clas]], Dice.D(3, 6), 9)
        # boost constitution if it's not good.
        self.stats[4] = max(self.stats[4], Dice.D(3, 6))

        self.race = "Human"

        if Dice.D(1, 100) <= 25:
            # this character will be a demi-human if the stats allow
            eligible = []
            if self.stats[4] >= 9:
                if self.clas != 2:
                    eligible.append("Dwarf")
            if self.stats[1] >= 9:
                eligible.append("Elf")
            if self.stats[3] >= 9:
                if self.clas != 2:
                    eligible.append("Halfling")
            if eligible:
                race = random.choice(eligible)
                if race == "Dwarf":
                    if self.stats[5] > 17:
                        self.stats[5] = 17
                if race == "Elf":
                    if self.stats[4] > 17:
                        self.stats[4] = 17
                if race == "Halfling":
                    if self.stats[0] > 17:
                        self.stats[0] = 17
                self.race = race

        self.hp = self.rollhp()

        self.movement = 40
        self.morale = 9

        self.armor = ""
        self.armorvalue = 0
        self.meleeweapon = "Pointy Stick"
        self.damage = "1d6"

        self.shield = ""
        self.shieldvalue = 0
        self.ringpro = 0
        self.potion = ""
        self.scroll = ""

        self.calc()

    def rollhp(self):
        hp = 0
        for i in range(min(self.level, 9)):
            roll = Dice.D(1, hitdice[self.clas][0]) + statbonuses[self.stats[4]]
            hp = hp + max(roll, 1)
        if self.level > 9:
            hp = hp + (hitdice[self.clas][1] * (self.level - 9))
        return hp

    def calc(self):
        self.ac = self.armorvalue + self.shieldvalue + statbonuses[self.stats[3]] + self.ringpro

    # generate items for an adventurer NPC
    def outfit(self):

        a = genarmor(self.clas, self.level)
        self.armor = a[0]
        self.armorvalue = a[1]
        self.movement = a[2]

        m = genmeleeweapon(self.clas, self.level)
        self.meleeweapon = m[0]
        self.damage = m[2]

        if m[1] < 2:
            s = genshield(self.clas, self.level)
            self.shield = s[1]
            self.shieldvalue = s[2]

        if self.clas == 2:
            if Dice.D(1, 100) < min(95, self.level * 4):
                self.ringpro = Dice.tableroller(ringprobonus)[1]

        self.potion = genpotion(self.clas, self.level)
        self.scroll = genscroll(self.clas, self.level)

        if self.clas == 0 or self.clas == 2: # generate spells
            self.spells = Spells.genspells(self.clas, self.level)

        self.calc()

def statstring(stats, abbrev = 0):
    rc = []
    for i in range(6):
        sb = statbonuses[stats[i]]
        if not abbrev or sb != 0:
            rc.append(statnames[i][0])
            rc.append(str(stats[i]))
            if sb > 0:
                rc.append("(+%d)" % sb)
            elif sb < 0:
                rc.append("(%d)" % sb)
    return string.join(rc, " ")

def genmeleeweapon(cclass, level):

    # choose a weapon type
    wpn = Dice.tableroller(meleeweapons[cclass])

    # is it magical?
    chance = 5
    if cclass == 2:
        chance = 3
    bonus = ""
    damage = wpn[3]
    if Dice.D(1, 100) < min(95, level * chance):
        row = Dice.tableroller(meleeweaponbonus)
        bonus = " " + row[1]
        damage = damage + bonus

    return [ wpn[1] + bonus, wpn[2], damage ]

def genpotion(cclass, level):
    rc = [ 0, "", 0 ]
    if Dice.D(1, 100) < (level * 2):
        rc = Dice.tableroller(potiontable)
        while rc[2] != -1 and rc[2] != cclass:
            rc = Dice.tableroller(potiontable)
    return rc[1]

def genscroll(cclass, level):
    if Dice.D(1, 100) < (level * 3):
        scroll = Dice.tableroller(scrolltable[cclass])[1]
        if type(scroll) is tuple:
            scrollspells = Spells.genscroll(scroll[0], scroll[1])
            scroll = "Scroll of %s Spells: %s" \
                   % (classnames[cclass], string.join(scrollspells, ", "))
        return scroll
    return ""

def genarmor(cclass, level):

    if cclass == 2:
        return defaultarmor[cclass]

    # is it magical?  (overrides armor type choice)
    chance = 5
    if cclass == 2:
        chance = 4
    if Dice.D(1, 100) < min(95, level * chance):
        typ = Dice.tableroller(armortypes[cclass])
        row = Dice.tableroller(armorbonus)
        return [ "%s +%d" % (typ[1], row[1]), typ[2] + row[1], min(typ[3] + 10, 40) ]

    return defaultarmor[cclass]

def genshield(cclass, level):

    if cclass > 1:
        return [ 0, "", 0 ]

    arm = [ 0, "Shield", 1 ]

    # is it magical?
    if Dice.D(1, 100) < min(95, level * 5):
        row = Dice.tableroller(armorbonus)
        arm[1] = "%s +%d" % (arm[1], row[1])
        arm[2] = arm[2] + row[1]

    return arm

def hitpointblock(hplst):

    if type(hplst) is int:
        hplst = [ hplst ]

    rc = [ ]

    for hp in hplst:

        row = [ "<p class='HitPointBlock'>HP %d" % hp ]

        # hit point boxes
        n = hp // 5
        r = hp % 5

        for i in range(n):
            row.append("&#9744;" * 5)

        row.append("&#9744;" * r)

        rc.append(string.join(row, " "))

    return string.join(rc, "\n")

def showcharacter(character):

    res = []

    res.append("<p>")
    if character.name:
        res.append("<b>" + character.name + "</b><p class='MonsterStats'>")
    else:
        res.append("%d " % character.noapp)
    res.append("%s %s %d," % (character.race, character.classname, character.level))
    res.append("AC %d," % character.ac)
    if type(character.hp) is int:
        res.append("HP %d," % character.hp)
    res.append("#At 1, Dam %s\n" % character.damage)
    res.append("(%s)" % statstring(character.stats))
    if character.spells is not None:
        res.append("<p class='Text Body'>Spells:")
        res.append(string.join(character.spells, ", "))
    items = []
    if character.armor:
        items.append(character.armor)
    if character.shield:
        items.append(character.shield)
    items.append(character.meleeweapon)
    if character.ringpro > 0:
        items.append("Ring of Protection +%d" % character.ringpro)
    if character.potion:
        items.append("Potion of %s" % character.potion)
    if character.scroll:
        items.append(character.scroll)
    if items:
        res.append("<p class='Text Body'>Equipment:")
    res.append(string.join(items, ", "))

    return string.join(res, "\n")
    
def block(character):

    res = [ "<p>" ]

    rcl = "%s %s %d" % (character.race, character.classname, character.level)
    if character.name:
        res.append("<b>%s:</b> %s," % (character.name, rcl))
    else:
        res.append("<b>%d %s:</b>" % (character.noapp, rcl))
    res.append("AC %d, #At 1, Dam %s, Mv %d', Ml %d" 
        % (character.ac, character.damage, character.movement, character.morale))
    ss = statstring(character.stats, 1).strip()
    if ss:
        res.append("<p class='Text Body'>(%s)" % ss)
    if character.spells is not None:
        res.append("<p class='Text Body'>Spells:")
        res.append(string.join(character.spells, ", "))
    items = []
    if character.armor:
        items.append(character.armor)
    if character.shield:
        items.append(character.shield)
    items.append(character.meleeweapon)
    if character.ringpro > 0:
        items.append("Ring of Protection +%d" % character.ringpro)
    if character.potion:
        items.append("Potion of %s" % character.potion)
    if character.scroll:
        items.append(character.scroll)
    if items:
        res.append("<p class='Text Body'>Equipment:")
    res.append(string.join(items, ", "))

    res.append(hitpointblock(character.hp))

    return string.join(res, "\n")
    
def showparty(party):

    res = []

    for character in party:
        res.append(block(character))

    return string.join(res, "\n")

def miscitems(totlvl):

    items = []

    if Dice.D(1, 100) <= totlvl: # misc. magic item
        items.append(Dice.tableroller(miscmagictable)[1])
        if Dice.D(1, 100) <= (totlvl / 2): # another misc. magic item
            items.append(Dice.tableroller(miscmagictable)[1])
            if Dice.D(1, 100) <= (totlvl / 4): # yet another misc. magic item
                items.append(Dice.tableroller(miscmagictable)[1])

    return items

def showitems(items):
    if items:
        return "<p><b>Additional Miscellaneous Magic:</b> %s" % string.join(items, ", ")
    return ""

def generate(level):

    ftrs = Dice.D(1, 3)
    thfs = Dice.D(1, 2)
    clrs = Dice.D(1, 2)
    mus = Dice.D(1, 2) - 1

    party = []

    for i in range(clrs):
        party.append(Character(level, 0))

    for i in range(ftrs):
        party.append(Character(level, 1))

    for i in range(mus):
        party.append(Character(level, 2))

    for i in range(thfs):
        party.append(Character(level, 3))

    totlvl = 0

    for character in party:
        character.outfit()
        totlvl += character.level

    items = miscitems(totlvl)

    return "%s\n%s" % (showparty(party), showitems(items))

def single(klass, level):

    character = Character(level, klass, actuallevel = 1)
    character.outfit()

    return showparty([ character ])

if __name__ == "__main__":
    print generate(5)

# end of file.
