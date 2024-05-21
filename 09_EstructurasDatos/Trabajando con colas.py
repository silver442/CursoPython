import queue

# cola de tipo FIFO
miCola=queue.Queue(4)

# cola LIFO
# miCola=queue.LifoQueue()

# cola priority
# miCola=queue.PriorityQueue()

# agregar elementos
miCola.put("Madrid")
miCola.put("Bogotá")
miCola.put("México DF")
miCola.put("Lima")

print(miCola.full()) #True si la cola esta lleva

print(miCola.get()) # get saca elementos

print("A continuación se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:
    print(elemento)