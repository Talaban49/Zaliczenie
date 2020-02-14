'''
    Klasa definiująca wektor w przestrzeni R3 
    oraz implementująca jego funkcjonalności.
    Wektor z przestrzeni R1 oraz R2 zostanie rzutowany 
    na odpowiednia przestrzeń poprzez wypełnienie brakujących
    wersorów zerami.
'''

class Vector3D:
    def __init__(self, x=0, y=0, z=0, *args, **kwargs):
        self.__flag = False
        try:
            assert isinstance(x,int) or isinstance(x, float)
            self.__x = x
            assert isinstance(y,int) or isinstance(y, float)
            self.__y = y
            assert isinstance(z,int) or isinstance(z, float)
            self.__z = z
            self.__flag = True

        except AssertionError:
            print('Błąd inicjalizacji instancji!!!')
 
    def __str__(self):
        if self.__flag:
            return f'({self.__x}, {self.__y}, {self.__z})'

    def __add__(self, component):
        if self.__flag and isinstance(component, Vector3D):
            return Vector3D(self.__x + component.__x, self.__y + component.__y, self.__z + component.__z)

    def __sub__(self, component):
        if self.__flag and isinstance(component, Vector3D):
            return Vector3D(self.__x - component.__x, self.__y - component.__y, self.__z - component.__z)

    def __rmul__(self, component):
        if self.__flag and (isinstance(component, int) or isinstance(component, float)):
            return Vector3D(component * self.__x, 
                            component * self.__y,
                            component * self.__z)

    def __mul__(self, component):
        if self.__flag and (isinstance(component, int) or isinstance(component, float)):
            return Vector3D(component * self.__x, 
                            component * self.__y,
                            component * self.__z)

        if self.__flag and isinstance(component, Vector3D):
            return Vector3D(self.__y * component.__z - self.__z * component.__y, 
                            self.__z * component.__x - self.__x * component.__z, 
                            self.__x * component.__y - self.__y * component.__x)

    def __matmul__(self, vector):
        if self.__flag and isinstance(vector, Vector3D):
            return self.__x * vector.__x + self.__y * vector.__y + self.__z * vector.__z

    def __eq__(self, vector):
        if self.__flag and isinstance(vector, Vector3D):
            return self.__x == vector.__x and self.__y == vector.__y and  self.__z == vector.__z
        return False

    def __getitem__(self,index):
        temporary = [self.__x, self.__y, self.__z]

        try: 
            assert isinstance(index,int) and -len(temporary) <= index <= (len(temporary) - 1)
            return temporary[index]

        except AssertionError:
            print('Niepoprawny indeks!!!')

    def lenghtOfVector(self):
        if self.__flag:
            return (self.__x**2 + self.__y**2 + self.__z**2)**(1/2)


def main():
    u = Vector3D(1,1,1,"dasdasd",3213123,l=32131)
    v = Vector3D(1,1,-3)
    r = Vector3D(2,-1,1)
    z = Vector3D(1,2,3)
    print(u.lenghtOfVector())
    print(f'v={v}')
    print(f'u={u}')
    print(f'r={r}')
    print(f'u+v={u + v}')
    print(f'u-v={u - v}')
    print(f'u x v={u * v}')
    print(f'u x 3={u * 3}')
    print(f'3 x v={3 * v}')
    print(f'u o v = {u @ v}')
    print(f'r o (v x u) = {r @ (u*v)}')
    print(z[3])
    print(z[2])
    print(z[1])
    print(z[0])
    print(z[-1])
    print(z[-2])
    print(z[-3])
    print(z[-4])
    print(z["sadasdasd"])

if __name__ == '__main__':
    main()