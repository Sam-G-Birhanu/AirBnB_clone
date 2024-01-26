#!/usr/bin/python3
import BaseModel>>> from models.base_model import BaseModel
>>> from models import storage
>>> all_objs = storage.all()
>>> print(all_objs)
{}
>>> m = BaseModel()
>>> print(all_objs)
{'BaseModel.071d5d09-5e10-4e7f-bbd4-527451514580': <models.base_model.BaseModel object at 0x7ffde1229250>}
>>> storage.save()
>>> storage.reload()
>>> print(storage.all())
{'BaseModel.071d5d09-5e10-4e7f-bbd4-527451514580': <models.base_model.BaseModel object at 0x7ffde11a4df0>}
>>>
