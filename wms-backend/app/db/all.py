"""
Tüm moduller içinden modeller buraya import edilir. db oluşturmak için ve kullanmak için gerekli
 olanlar da olur. bakıcaz daha orayı düşünmedim. ben şimdi
"""
from .base_class import Base

from ..modules.auth.models import *
from ..modules.wms.models import *
