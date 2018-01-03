import sqlite3
baglanti=sqlite3.connect('pizza.db')
baglanti.row_factory=sqlite3.Row

isaretci=baglanti.cursor()

isaretci.execute('CREATE TABLE siparis ( pizza VARCHAR(50), boyut VARCHAR(50), kenar VARCHAR(50), icecek VARCHAR(50))')

baglanti.commit()
baglanti.close()
