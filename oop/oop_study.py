#!/usr/bin/python3.6


#object --> state, behaviour  1 state --> 1 behaviour --> function --> method 

#How many objects can be in the class ?

#Practically we need min 1 object, and Max there, is no restiction  

#Where we keep object and fucntion that place called clause. 

#one name memeory space called class 

#class -> template, behaviour{Blueprint}

class Laptop:
      brand = 'Dell'   [variable -> atrributes]
      Color = 'Black'  [variable -> atrributes]
      
      def calculator(a,b) [function -> method]
          return a+b          [function -> method]
    
      def browser()
          pass 

#variable -> atrributes 
#function -> method
#objects -> instances

#class vodafone: # memeory space  Document Name

#executiove = vodafone() 

#manager = vodafone()   

#object name 
#representative referecence name of the object 
#object represents class
#object is instance of class 

# class variable  - is applicable for class and all the instance present inside the class. 
# instance variable - For each instance, memeory copy will be created 

# contructor - is useful for initialising object sepcific information .... Contructor will be called automatically whenevet you creating objects
