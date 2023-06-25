from collections import namedtuple
import json


City = namedtuple(typename='City', field_names='name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)
print(tokyo.population)

Coordinate = namedtuple('Coordinate', 'latitude longitude')
delhi_data = City('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))

uberlandia_data = ('Uberlândia', 'BR', 0.711, Coordinate( -18.9113, -48.2622))
uberlandia = City._make(uberlandia_data)

print(delhi_data)
# print(uberlandia)
# print(uberlandia._asdict())

print(json.dumps(uberlandia._asdict()))
