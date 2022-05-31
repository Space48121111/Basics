import object

if __name__ == '__main__':
    r = float(input('Give me a radius: '))
    s = object.Sphere(r)
    print('The vol of the sphere is ', s.vol())
    print('The surface of the sphere is ', s.surface())








# end
