import os, sys

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9./5)*celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*5./9
    return celsius


#____________________________________
def celsius_to_kelvin(celsius):
    return celsius+273.15

def kelvin_to_celsius(kelvin):
    return kelvin-273.15


#____________________________________
def fahrenheit_to_kelvin(fahrenheit):
    celcius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celcius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
