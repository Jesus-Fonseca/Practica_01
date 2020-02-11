# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:23:12 2020

@author: PC
"""

bicyles = ['trek','cannodale','redline','specialized']
print (bicyles)

bicyles = ['trek','cannodale','redline','specialized']
print (bicyles[1])

bicyles = ['trek','cannodale','redline','specialized']
print (bicyles[0].title())

print ('Nombres')
names = ['Carlos','Irving','Diego','Armando','Francisco','Daniel','Eduardo']
for i in range(len(names)):
    print (names[i])

print ('Mensaje')
names = ['Carlos','Irving','Diego','Armando','Francisco','Daniel','Eduardo']
mensaje = ['Hola','Que onda?','Nos vemos luego','Luego te veo','Que tal?','Que paso?','Cómo te va?']
for i in range (7):
	print(names[i])
	print(mensaje[i])

print ('Deseos')
deseos = ['Tener un millon de pesos','Tener un avion','Tener una empresa','Tener una mansión','Viajar','Eskiar','Bucear','Saltar de paracidas','Tener un lambo','Tener una pscina','Tener un jacuzzi','Aprender a cocinar','Aprender a hablar aleman','Ganar un torneo de futbol','Que mi equipo sea campeon']
for i in range (15):
	print (i+1)
	print(deseos[i])
    
print ('T-shirt')
def make_shirt(size_shirt,text_shirt):
	print ('Quiero una playera talla '+size_shirt+'.')
	print ('Quiero que mi playera lleve el texto '+text_shirt.title()+'.')
make_shirt(size_shirt='mediana',text_shirt='Hola mundo')

print ('Playeras grandes')
def make_shirt(size_shirt='grande', text_shirt='I <3 Python'):
	print ('Quiero una playera talla '+size_shirt+'.')
	print ('Quiero que mi playera lleve el texto '+text_shirt.title()+'.')
make_shirt()
make_shirt(size_shirt='mediana')
make_shirt(size_shirt='pequeña',text_shirt='Programador')

print ('Ciudades')
def describe_city(name_city,country_city='Canada'):
	print (name_city +' esta en '+ country_city + '.' )
describe_city(name_city='Ottawa')
describe_city(name_city='Toronto')
describe_city(name_city='Bruselas',country_city='Belgica')

print ('Clase restaurant')
class Restaurant ():
	def __init__ (self,name,type):
		self.restaurant_name = name
		self.cuisine_type = type

	def describe_restaurant(self):
			print ("El nombre del restaurante es " + self.restaurant_name.title())
			print ("El tipo de comida es " + self.cuisine_type.title())
	def open_restaurant(self):
			print ("El restaurante es " + str('abierto'))

my_restaurant = Restaurant ('Salads life','comida vegana')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print ('Clase tres restaurantes')
my_restaurant = Restaurant ('MC Donald','comida rápida')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant ('Sushitoo','comida japonesa')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant ('Tak majal','comida hindu')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print ('Clase usuarios')
class User():
	def __init__(self,first,second):
		self.first_name = first
		self.second_name = second
	def describe_user (self):
		print ("Primer apellido: " + self.first_name.title())
		print ("Segundo apellido: " + self.second_name.title())
	def greet_user (self):
		print ("Bienvenido " + self.first_name.title() + " " + self.second_name.title())

usuario = User ('Lopez','Valencia')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Beltran','Guzman')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Sanchez','Rodriguez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Perez','Dominguez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Flores','Aguilar')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Zenil','Perez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Neri','Garcia')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Acosta','Alcoser')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Prado','Hernandez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Morua','Alvarez')
usuario.describe_user()
usuario.greet_user()