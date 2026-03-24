import pickle
import os

def guardar(v, fd):
    a = open(fd, "wb")
    for obj in v:
        pickle.dump(obj, a)
    a.close()

def cargar(fd):
    v = []
    if not os.path.exists(fd):
        return v

    a = open(fd, "rb")
    tam = os.path.getsize(fd)

    while a.tell() < tam:
        v.append(pickle.load(a))

    a.close()
    return v